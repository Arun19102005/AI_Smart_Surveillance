# 🚨 AI Smart Surveillance System

## 📌 Overview

The **AI Smart Surveillance System** is a real-time intelligent monitoring solution that uses **Artificial Intelligence and Computer Vision** to detect suspicious activities such as weapon threats and violent behaviour through CCTV cameras.

Traditional CCTV systems only record footage and require continuous human monitoring. Our system automates this process by detecting dangerous activities and instantly sending alerts to authorities.

When a threat is detected, the system automatically:

* Captures the evidence image
* Identifies the current location
* Sends an alert notification with the image
* Updates a live monitoring dashboard

This helps authorities respond faster and improves public safety.

---

# 🎯 Objectives

The main objectives of this project are:

* Detect suspicious activities in real time
* Identify weapons such as knives and guns
* Detect violent behaviour such as fights
* Automatically alert authorities
* Provide a centralized monitoring dashboard
* Improve response time in emergency situations

---

# 🧠 Key Features

### 🔍 Real-Time Object Detection

Uses **YOLOv8 AI model** to detect dangerous objects such as:

* Knife
* Gun
* Fight activity
* Suspicious behaviour

### 📸 Automatic Evidence Capture

When a threat is detected, the system captures an image of the incident.

### 📩 Instant Telegram Alert

The system automatically sends an alert message with:

* Detection image
* Time of incident
* Live location link

### 📍 Live Location Tracking

The system detects the current location and generates a **Google Maps link**.

### 📊 Smart Monitoring Dashboard

A real-time dashboard displays:

* Total alerts
* Latest alert
* Alert timeline
* Alert location map
* Detection image
* Alert history records

---

# 🏗 System Architecture

Camera → AI Detection Model → Threat Detection → Image Capture → Telegram Alert → Dashboard Update

---

# 🛠 Technologies Used

| Technology       | Purpose                           |
| ---------------- | --------------------------------- |
| Python           | Core programming language         |
| YOLOv8           | Real-time object detection        |
| OpenCV           | Camera input and image processing |
| Streamlit        | Dashboard development             |
| Telegram Bot API | Instant alert notifications       |
| Geocoder         | Location detection                |
| CSV              | Alert data storage                |

---

# ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Smart-Surveillance-System.git
cd AI-Smart-Surveillance-System
```

---

### 2️⃣ Install Required Libraries

```bash
pip install ultralytics
pip install opencv-python
pip install streamlit
pip install playsound
pip install geocoder
pip install requests
pip install plotly
pip install streamlit-autorefresh
```

---

### 3️⃣ Configure Telegram Bot

Create a Telegram bot and update the following values in **main.py**

```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
```

---

### 4️⃣ Run the Detection System

```bash
python main.py
```

---

### 5️⃣ Run the Monitoring Dashboard

```bash
python -m streamlit run dashboard.py
```

---

# 📊 Dashboard Features

The dashboard provides a **real-time control center** for monitoring alerts.

It displays:

* Total alerts detected
* Latest threat detection time
* Daily alert statistics
* Alert timeline chart
* Location of incidents on a map
* Detection images
* Alert records

---

# 📁 Project Structure

```
AI-Smart-Surveillance-System
│
├── main.py
├── dashboard.py
├── alerts.csv
├── requirements.txt
│
├── alerts
│   ├── alert_2026-03-10_10-01-30.jpg
│
└── README.md
```

---

# 🚀 Future Improvements

* Multi-camera surveillance system
* Crowd density monitoring
* Suspicious behaviour detection
* Integration with police control rooms
* AI crime prediction system
* Mobile application for alerts

---

# 🔐 Use Cases

This system can be deployed in:

* Smart cities
* Airports
* Railway stations
* Shopping malls
* Public events
* Government buildings
* Schools and universities

---

# 📷 Example Alert Message

```
🚨 AI SURVEILLANCE ALERT

Threat Detected: Knife

Time: 2026-03-10 14:32:01

Location:
https://maps.google.com/?q=13.0827,80.2707
```

---

# 👨‍💻 Author

**Arun**

**Rayaan**

**Saravanan**

**Araving Krishna**

AI & Computer Vision Project

---

# 📄 License

This project is created for **educational and research purposes**.
