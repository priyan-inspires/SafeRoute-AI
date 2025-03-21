# SafeRoute-AI
# 🚗 Road Accident Detection System

An AI-powered accident detection system using **OpenCV**, **Twilio**, and **geolocation APIs** to monitor vehicle collisions and automatically send **SOS alerts** with the **live location** to emergency contacts.

## 📌 Project Overview
This project uses **computer vision** to detect vehicle collisions in real-time through a webcam. If a potential accident is detected, an **emergency message** containing the **current location** is sent via **SMS** to pre-defined recipients using **Twilio**.

## 🛠️ Features
- 📷 **Real-Time Vehicle Detection**: Monitors live video feed for vehicle collisions.
- 📍 **Location Sharing**: Sends live GPS location using **geocoder**.
- 📲 **Automated SOS Alerts**: Uses **Twilio API** to send emergency messages.
- 🟢 **Customizable Alerts**: Supports multiple emergency contacts.
- 🛑 **User Control**: Press **'q'** to exit the system.

## 📂 Project Structure
```
├── accident_detection.py    # Main code for vehicle detection & SOS alert
├── haarcascade_car.xml      # Pre-trained model for vehicle detection
└── README.md                # Project documentation
```

## 🔧 Installation

1. **Clone the Repository:**
```bash
git clone https://github.com/yourusername/road-accident-detection.git
cd road-accident-detection
```

2. **Set Up a Virtual Environment (Optional but Recommended):**
```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

3. **Install Dependencies:**
```bash
pip install opencv-python twilio geocoder
```

## 🚀 Usage

1. **Configure Twilio Credentials:**
Replace the following placeholders in `accident_detection.py`:

```python
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_number = 'your_twilio_number'
recipient_number1 = 'recipient_phone_number'
recipient_number2 = 'recipient_phone_number'
```

2. **Run the Program:**
```bash
python accident_detection.py
```

3. **Exit the Program:**
Press **'q'** to quit the monitoring.

## 📊 How It Works
1. Captures live video using **OpenCV**.
2. Detects vehicles using **Haar Cascade Classifier**.
3. If **multiple vehicles** are detected (potential accident), it:
   - Retrieves the current location via **geocoder**.
   - Sends an **SOS message** with location to specified contacts via **Twilio**.

## 📌 Customization
- **Threshold Adjustment:** Modify the condition `if len(vehicles) > 1` to fine-tune accident detection sensitivity.
- **Location Accuracy:** Ensure the system has internet access for accurate geolocation.
- **More Contacts:** Add additional recipient numbers in the `to` field.

## 📜 Requirements
- Python 3.8+
- OpenCV
- Twilio
- Geocoder

## 📧 Contact
Feel free to reach out if you have any questions or suggestions!

👨‍💻 **Author:** Shanmugapriyan J

⭐ **If you find this project useful, please give it a star!**


