# server/train.py
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1. This function looks at a URL and counts suspicious things
def get_features(url):
    return [
        len(url),                   # Feature 1: Length (Phishing URLs are usually long)
        url.count('.'),             # Feature 2: Dots (e.g., paypal.com.user-login.php has many)
        1 if '@' in url else 0,     # Feature 3: Has '@' symbol
        url.count('/'),             # Feature 4: Slashes (deep folder structure)
        1 if not url.startswith('https') else 0 # Feature 5: Not HTTPS
    ]

# 2. We teach the AI with some examples (0 = Safe, 1 = Phishing)
data = [
    # Safe sites
    ("google.com", 0), ("youtube.com", 0), ("amazon.in", 0), ("github.com", 0),
    # Phishing sites (Fake examples)
    ("secure-login.paypal.com.account-update.php", 1),
    ("http://192.168.1.5/login", 1),
    ("amazon-support-security-alert.com", 1)
]

# 3. Prepare the data
X = [get_features(url) for url, label in data] # The features
y = [label for url, label in data]             # The answers

# 4. Train the model
print("Training the AI model...")
model = RandomForestClassifier()
model.fit(X, y)

# 5. Save the brain to a file
joblib.dump(model, "phishing_model.pkl")
print("Success! Model saved as 'phishing_model.pkl'")