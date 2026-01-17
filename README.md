# PhishGuard: AI-Powered Real-Time Phishing Detector 🛡️

**PhishGuard** is a full-stack browser security extension that detects malicious URLs in real-time. Unlike static blacklists that are often outdated, PhishGuard uses a **Machine Learning (Random Forest)** model to analyze the lexical structure of URLs and flag zero-day phishing attacks instantly.

## 🚀 Key Features
- **Real-Time Detection:** Analysis happens in <200ms using a lightweight AI model.
- **Zero-Day Protection:** Detects new phishing sites that aren't yet in any blacklist.
- **Privacy Focused:** Only the URL string is analyzed; no user data is stored.
- **Visual Risk Score:** Provides a clear "Safe" or "Phishing" verdict with a probability percentage.

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, JavaScript (Chrome Extension Manifest V3)
- **Backend:** Python, Flask (REST API)
- **Machine Learning:** Scikit-Learn (Random Forest Classifier), Pandas, NumPy
- **Serialization:** Joblib

## 📂 Project Structure
```bash
PhishGuard/
├── extension/          # Chrome Extension Source Code
│   ├── manifest.json
│   ├── popup.html
│   └── popup.js
├── server/             # Python Backend & ML Model
│   ├── app.py          # Flask API
│   ├── train.py        # Model Training Script
│   └── phishing_model.pkl
└── README.md
