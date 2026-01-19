#include <WiFi.h>
#include <Firebase_ESP_Client.h>

// =============================
// WIFI CONFIG
// =============================
#define WIFI_SSID "--------"
#define WIFI_PASSWORD "-------"

// =============================
// FIREBASE CONFIG
// =============================
#define API_KEY "--------------"
#define DATABASE_URL "-------------------"

// =============================
// MQ SENSOR PINS
// =============================
#define MQ1_PIN 34   // GPIO 34
#define MQ2_PIN 35   // GPIO 35

// =============================
// FIREBASE OBJECTS
// =============================
FirebaseData fbdo;
FirebaseAuth auth;
FirebaseConfig config;

// =============================
// SETUP
// =============================
void setup() {
  Serial.begin(115200);

  // Connect to WiFi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println("\n✅ WiFi Connected");

  // Firebase config
  config.api_key = API_KEY;
  config.database_url = DATABASE_URL;

  // Anonymous login
  if (Firebase.signUp(&config, &auth, "", "")) {
    Serial.println("✅ Firebase Auth Success");
  } else {
    Serial.printf("❌ Firebase Auth Failed: %s\n", config.signer.signupError.message.c_str());
  }

  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);

  Serial.println("🔥 Firebase Ready");
}

// =============================
// LOOP
// =============================
void loop() {
  // Read MQ sensors (ADC 0–4095)
  int mq1Value = analogRead(MQ1_PIN);
  int mq2Value = analogRead(MQ2_PIN);

  Serial.print("MQ1: ");
  Serial.print(mq1Value);
  Serial.print(" | MQ2: ");
  Serial.println(mq2Value);

  // Send to Firebase
  if (Firebase.RTDB.setInt(&fbdo, "/sensorData/mq1", mq1Value)) {
    Serial.println("✅ MQ1 sent");
  } else {
    Serial.println("❌ MQ1 failed: " + fbdo.errorReason());
  }

  if (Firebase.RTDB.setInt(&fbdo, "/sensorData/mq2", mq2Value)) {
    Serial.println("✅ MQ2 sent");
  } else {
    Serial.println("❌ MQ2 failed: " + fbdo.errorReason());
  }

  Serial.println("------------------------");
  delay(3000);  // send every 3 seconds
}
