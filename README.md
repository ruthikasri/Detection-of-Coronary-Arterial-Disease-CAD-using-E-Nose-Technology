# 🫀 Detection of Coronary Arterial Disease (CAD) Using E-Nose Technology

An **IoT and Machine Learning based healthcare project** that detects the risk level of **Coronary Arterial Disease (CAD)** using breath analysis data from MQ gas sensors, cloud connectivity, and real-time mobile visualization.

---

## 📌 Project Overview

Coronary Arterial Disease (CAD) is one of the leading causes of death worldwide. Early detection plays a crucial role in prevention and management. This project proposes a **non-invasive, cost-effective CAD screening system** using:

* Electronic Nose (E-Nose) concept
* IoT (ESP32 + Firebase)
* Machine Learning (KNN)
* Cloud Dashboard (Adafruit IO)
* Android Mobile App (MIT App Inventor)

---

## 🎯 Objectives

* To collect breath-based gas sensor data using MQ sensors
* To transmit real-time sensor data to the cloud
* To classify CAD risk levels using a Machine Learning model
* To visualize results on a dashboard and Android application
* To provide automated health prescriptions based on prediction

---

## 🧠 System Architecture

1. **Hardware Layer**

   * ESP32 Microcontroller
   * MQ Gas Sensor 1 (MQ1)
   * MQ Gas Sensor 2 (MQ2)

2. **Cloud Layer**

   * Firebase Realtime Database (data storage & communication)

3. **Machine Learning Layer**

   * Python-based KNN classifier

4. **Visualization Layer**

   * Adafruit IO Dashboard (live graphs & status)
   * Android App (MIT App Inventor)

---

## 🛠 Technologies Used

### Hardware

* ESP32
* MQ Series Gas Sensors

### Software & Tools

* Arduino IDE
* Python
* Firebase Realtime Database
* Adafruit IO
* MIT App Inventor

### Machine Learning

* Scikit-learn
* K-Nearest Neighbors (KNN)
* Pandas, NumPy

---

## 📂 Project Structure

```
CAD-Detection-Using-E-Nose/
│   |__ Block Diagra.png
|   |__ Circuit Diagram.png
|
├── Arduino_Code/
│   └── esp32_mq_firebase.ino
│
├── Python_ML/
│   ├── pred.py
│   └── mq_dual_sensor_dataset.xlsx
│
├── Mobile_App/
│   └── CAD_Detection_App.apk
│
├── Dashboard_Screenshots/
│   └── adafruit_dashboard.png
│
└── README.md
```

---

## ⚙️ Working Methodology

1. MQ sensors capture breath VOC values
2. ESP32 reads sensor data and uploads it to Firebase
3. Python script fetches live data from Firebase
4. KNN model predicts CAD risk level:

   * **Normal**
   * **Need Consideration**
   * **Severe**
5. Prediction & prescription are:

   * Sent to Adafruit IO dashboard
   * Displayed in Android mobile application

---

## 📊 Output Results

* Live sensor graphs on Adafruit IO
* CAD status display (Normal / Need Consideration / Severe)
* Auto-generated health prescription
* Android APK showing results in real time

---

## 📱 Mobile Application

* Developed using **MIT App Inventor**
* Fetches data from Firebase
* Displays CAD result and health advice
* Simple and user-friendly UI

---

## 🧪 Machine Learning Model

* Algorithm: **K-Nearest Neighbors (KNN)**
* Input features: MQ1, MQ2 values
* Output labels: CAD risk categories
* Dataset: Custom dual MQ sensor dataset

---

## ⚠️ Disclaimer

This system is intended **only for preliminary screening and educational purposes**. It is **not a substitute for professional medical diagnosis**.

---

## 🚀 Future Enhancements

* Integration of ECG / SpO₂ sensors
* Use of advanced ML models (SVM, Random Forest)
* Mobile app with patient history
* Clinical data validation

---

## 👩‍💻 Author

**Ruthika Sri**
B.E – Electronics and Communication Engineering

---

## ⭐ Acknowledgment

Thanks to open-source IoT platforms and ML libraries that made this project possible.

---

⭐ *If you like this project, don’t forget to star the repository!*
