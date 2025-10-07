# Detection-of-Coronary-Arterial-Disease-CAD-using-E-Nose-Technology

This project presents an innovative **IoT + Machine Learning** approach for detecting **Coronary Artery Disease (CAD)** by analyzing **Volatile Organic Compounds (VOCs)** from a patient’s breath using **Electronic Nose (E-Nose)** sensors.

---

## 🩺 Overview
Coronary Artery Disease (CAD) is one of the leading causes of death worldwide.  
This project proposes a **non-invasive diagnostic system** using semiconductor gas sensors (MQ-4 and MQ-7) and a microcontroller (ESP32) to analyze VOCs like **acetone, benzene, and toluene** exhaled in breath samples.

The VOC data is transmitted via Wi-Fi to the **ThingSpeak IoT cloud**, processed with **Python and Machine Learning**, and visualized in **Power BI** for CAD detection and trend prediction.

---

## ⚙️ System Architecture
```

MQ-4 / MQ-7 Sensors → ESP32 Microcontroller → ThingSpeak Cloud → Python ML Model → Power BI Visualization

````

---

## 🧩 Tech Stack

| Layer | Technologies Used |
|--------|-------------------|
| **Sensors** | MQ-4 (Methane, Toluene), MQ-7 (Carbon Monoxide) |
| **Microcontroller** | ESP32 with Wi-Fi & Bluetooth |
| **Programming Languages** | Python, C++ (Arduino IDE) |
| **IoT Platform** | ThingSpeak Cloud |
| **Machine Learning** | Scikit-learn, NumPy, Pandas |
| **Visualization** | Power BI, ThingSpeak Charts |
| **Forecasting** | Time Series Analysis (Python) |

---

## 🧠 Methodology

1. **Data Acquisition**
   - MQ-4 and MQ-7 sensors capture gas concentrations from breath samples.
   - ESP32 converts analog sensor values into digital signals.

2. **Data Transmission**
   - ESP32 sends sensor data to **ThingSpeak Cloud** via Wi-Fi for storage and visualization.

3. **Machine Learning Analysis**
   - A Python-based ML model classifies breath data into **CAD** or **Healthy** categories.
   - Time series forecasting predicts upcoming trends in VOC levels.

4. **Visualization**
   - **ThingSpeak** for real-time gas trends.
   - **Power BI** for VOC analysis and CAD detection dashboards.

---

## 📈 Results
- Real-time tracking of VOC gases (Acetone, Benzene, Toluene).
- Power BI dashboards for patient data analytics.
- Accurate classification between CAD and healthy samples using machine learning.
- Time series forecasting predicting disease progression trends.

---

## 🧩 Future Enhancements
- Include more sensors (MQ-2, MQ-135) for expanded biomarker detection.  
- Integrate advanced deep learning models for improved accuracy.  
- Develop a web/mobile dashboard for patient monitoring and alerts.  

---

## 🧾 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/E-Nose-CAD-Detection.git
   cd E-Nose-CAD-Detection
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Upload firmware to ESP32:

   * Open `firmware/esp32_code.ino` in **Arduino IDE**.
   * Configure your **Wi-Fi SSID**, **Password**, and **ThingSpeak API keys**.
   * Upload to the ESP32 board.

4. Run the ML model:

   ```bash
   python ml_model/model_training.py
   ```

5. Open Power BI and load `visualization/powerbi_dashboard.pbix` to view analytics.

---

## 🧰 Repository Structure

```
E-Nose-CAD-Detection/
│
├── README.md
├── requirements.txt
├── firmware/
│   ├── esp32_code.ino
│   └── thingspeak_config.txt
├── ml_model/
│   ├── model_training.py
│   ├── model.pkl
│   └── signal_processing.py
├── visualization/
│   ├── powerbi_dashboard.pbix
│   ├── timeseries_forecasting.py
│   └── screenshots/
│       ├── acetone_graph.png
│       ├── benzene_graph.png
│       └── toluene_graph.png
├── data/
│   ├── cad_samples.csv
│   └── healthy_samples.csv
└── docs/
    ├── project_report.pdf
    ├── presentation_slides.pptx
    └── references.txt
```

---

## 👩‍💻 Contributor

**Ruthika Sri C M**
Department of Biomedical Engineering
**Vel Tech High Tech Dr. Rangarajan Dr. Sakunthala Engineering College**, Chennai, India
📧 *[[youremail@example.com](mailto:youremail@example.com)]*

---

## 📚 Reference

Based on the research paper:
**“Detection of Coronary Arterial Disease Using E-Nose Technology”**
Vel Tech Multi Tech, 2023.

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).

````

---

## 🧩 **requirements.txt**

Save this as `requirements.txt` in the same folder as your README:

```txt
# Core Python Libraries
numpy==1.26.4
pandas==2.2.2
scikit-learn==1.5.0
matplotlib==3.9.0

# IoT and Data Processing
requests==2.32.3
json5==0.9.14

# Visualization & Forecasting
plotly==5.23.0
statsmodels==0.14.2
seaborn==0.13.2

# Optional (for Power BI or API integrations)
flask==3.0.3
joblib==1.4.2
````

---

✅ **Next Step:**

1. Copy both files (`README.md` + `requirements.txt`) into your project folder.
2. Commit and push them to your GitHub repository:

   ```bash
   git add README.md requirements.txt
   git commit -m "Added README and dependencies for E-Nose CAD Detection"
   git push origin main
   ```

---

Would you like me to generate a matching **MIT License file** and **.gitignore** (for Python + Arduino projects) next?
They make your repository look professional and clean.
