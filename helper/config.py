from flask import Flask
from decouple import config

# Flask App Initialization
app = Flask(__name__)

try:
    # Config Variables
    APP_ID = config("APP_ID", "21188057")
    API_HASH = config("API_HASH", "8564fab8db759bb04b1907bd12ed98ef")
    BOT_TOKEN = config("BOT_TOKEN", "8169313125:AAHQ6ELfV2kisRxB3XHdIOwlDaSonZfzAb0")
    OWNER = config("OWNER_ID", "8102446291")
    LOG = config("LOG_CHANNEL", "-1002289024376")
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("Something went wrong")
    LOGS.info(str(e))
    exit(1)

# Flask Route for Health Check or Basic Info
@app.route('/')
def home():
    return "The bot is running successfully on port 8080."

if __name__ == "__main__":
    # Start Flask Server on port 8080
    app.run(host="0.0.0.0", port=8080)
