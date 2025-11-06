import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

# Expect full JSON content of service account in the environment variable FIREBASE_CONFIG
firebase_config_str = os.environ.get("FIREBASE_CONFIG")
if not firebase_config_str:
    raise RuntimeError("FIREBASE_CONFIG environment variable not found. Add your Firebase service account JSON as the value.")

try:
    firebase_config = json.loads(firebase_config_str)
except Exception as e:
    raise RuntimeError(f"Failed to parse FIREBASE_CONFIG JSON: {e}")

cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred)
db = firestore.client()
