import pandas as pd
import pyrebase
import time
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from Adafruit_IO import Client

# ==============================
# FIREBASE CONFIG
# ==============================
firebaseConfig = {
    xxxxxxxxxxxxxxxxxxx
  xxxxxxxxxxxxxxxxxxxxxx
  xxxxxxxxxxxxxxxxxxxxx
}

# ==============================
# ADAFRUIT IO CONFIG
# ==============================
ADAFRUIT_IO_USERNAME = "-----------"
ADAFRUIT_IO_KEY = "-------------"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Feeds in Adafruit IO
mq1_feed = aio.feeds('mq1')
mq2_feed = aio.feeds('mq2')
pred_feed = aio.feeds('prediction')       # For label only
presc_feed = aio.feeds('prescription')   # For paragraph/advice

print("Connected to Adafruit IO")

# ==============================
# ADVICE DICTIONARY
# ==============================
advice_dict = {
    "severe": "Consult_a_cardiologist_immediately_Avoid_smoking_and_alcohol_if_you_have_any_addiction_Follow_prescribed_medication_strictly_Monitor_BP_and_sugar_daily_Reduce_stress_and_get_proper_sleep"
    ,
    "need_consider": "Schedule_a_medical_check-up_Improve_diet_and_exercise_regularly_Reduce_salt_and_sugar_intake_Quit_smoking_and_limit_alcohol_if_you_have_any_adiction_Manage_stress_with_yoga_or_meditation"
    ,
    "normal": "Maintain_a_healthy_lifestyle_Exercise_regularly_Eat_a_balanced_diet_Get_annual_health_checkups_Avoid_unhealthy_habits"
}

# ==============================
# LOAD DATASET
# ==============================
df = pd.read_excel("mq_dual_sensor_dataset.xlsx")

X = df[["MQ_Value_1", "MQ_Value_2"]]
y = df["Result"]

# Encode labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# ==============================
# TRAIN KNN MODEL
# ==============================
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

print("KNN model trained")

# ==============================
# FIREBASE INITIALIZE
# ==============================
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

print("Connected to Firebase")

# ==============================
# LIVE PREDICTION LOOP
# ==============================
while True:
    try:
        # Read sensor data
        sensor_data = db.child("sensorData").get().val()

        if sensor_data is None:
            print("⚠ No sensor data")
            time.sleep(3)
            continue

        mq1 = sensor_data.get("mq1")
        mq2 = sensor_data.get("mq2")

        if mq1 is None or mq2 is None:
            print("⚠ Incomplete MQ data")
            time.sleep(3)
            continue

        print(f"Firebase → MQ1:{mq1}  MQ2:{mq2}")

        # ==============================
        # SEND INPUT DATA TO ADAFRUIT IO
        # ==============================
        aio.send_data(mq1_feed.key, mq1)
        aio.send_data(mq2_feed.key, mq2)

        # ==============================
        # KNN PREDICTION
        # ==============================
        input_data = [[mq1, mq2]]
        pred_encoded = knn.predict(input_data)
        pred_label = label_encoder.inverse_transform(pred_encoded)[0]

        # Get advice list
        pred_advice = advice_dict.get(pred_label, [])

        print(f"Prediction → {pred_label}")
        print(f"Prescription → {pred_advice}")

        # ==============================
        # SEND TO ADAFRUIT IO
        # ==============================
        # Prediction label
        aio.send_data(pred_feed.key, pred_label)

        # Prescription as paragraph string
        if(pred_label=="severe"):
            aio.send_data(presc_feed.key, "Consult a cardiologist immediately Avoid smoking and alcohol if you have any addiction Follow prescribed medication strictly Monitor BP and sugar daily Reduce stress and get proper sleep")
        if(pred_label=="need_consider"):
            aio.send_data(presc_feed.key, "Schedule a medical check-up Improve diet and exercise regularly Reduce salt and sugar intake Quit smoking and limit alcohol if you have any adiction Manage stress with yoga or meditation")
        if(pred_label=="normal"):
            aio.send_data(presc_feed.key, "Maintain a healthy lifestyle Exercise regularly Eat a balanced diet Get annual health checkups Avoid unhealthy habits")

        # ==============================
        # UPDATE FIREBASE
        # ==============================
        db.child("sensorData").update({
            "result": pred_label,
            "prescription": pred_advice
        })

        print("Firebase & Adafruit updated\n")

        time.sleep(5)

    except Exception as e:
        print("❌ Error:", e)
        time.sleep(5)
