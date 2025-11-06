ReVo-Server (FastAPI) — Ready for Render deployment
==================================================

What this project contains
--------------------------
- main.py                 : FastAPI app with endpoints (/, /add_user, /get_users)
- firebase_admin_setup.py : Reads FIREBASE_CONFIG env var and initializes Firestore
- requirements.txt        : Python dependencies for Render
- Procfile                : Render start command (gunicorn with uvicorn worker)
- .gitignore

IMPORTANT — Option B (secure): Using Render environment variable
----------------------------------------------------------------
You chose Option B: store your Firebase service account JSON securely in Render's environment.

1) On Firebase Console:
   - Go to Project Settings → Service accounts
   - Click "Generate new private key"
   - Open the downloaded JSON file in a text editor and copy its entire content.

2) On Render:
   - Create a new Web Service and connect your GitHub repo containing this project.
   - After creating (or while creating), go to the Service -> Environment.
   - Add a new environment variable:
     Key  : FIREBASE_CONFIG
     Value: (paste the entire JSON text you copied from the service account file)

3) Code notes:
   - firebase_admin_setup.py reads FIREBASE_CONFIG and initializes Firestore.
   - Do NOT commit your config.json to GitHub.
   - If the FIREBASE_CONFIG var is missing or invalid, the app will raise an error on startup.

4) Endpoints
   - GET  /                  -> health check
   - POST /add_user          -> add a new user (JSON body)
       Example body:
       {
         "username": "player1",
         "email": "player1@example.com",
         "gold": 100,
         "skins": {"ak47": "gold_skin"}
       }
   - GET  /get_users         -> returns list of users

5) Deploy Steps (Android-friendly)
   - Push this folder to a GitHub repo from your Android (use GitHub app or Acode).
   - On Render, create a Web Service -> connect repo -> use Python environment.
   - Build Command:  pip install -r requirements.txt
   - Start Command:  (Procfile is used by Render automatically) or:
                     gunicorn main:app -k uvicorn.workers.UvicornWorker
   - Add FIREBASE_CONFIG env var (paste service account JSON)
   - Deploy. Render will provide a URL like https://your-service.onrender.com

6) Test locally (optional, Termux on Android)
   - If you want to test locally on Termux, create a file config.json with the service account,
     then set environment variable:
       export FIREBASE_CONFIG="$(cat config.json)"
     Then run:
       pip install -r requirements.txt
       python main.py
   - Access http://127.0.0.1:5000

Support
-------
Reply here if you want:
- The repo packaged as a ZIP download (I already created it for you)
- Changes to endpoints (login, store, inventory)
- A version using Flask instead of FastAPI
