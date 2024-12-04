

from . import *

try:
    APP_ID = config("APP_ID", "21188057")
    API_HASH = config("API_HASH", "8564fab8db759bb04b1907bd12ed98ef")
    BOT_TOKEN = config("BOT_TOKEN", "8169313125:AAHQ6ELfV2kisRxB3XHdIOwlDaSonZfzAb0")
    OWNER = config("OWNER_ID", "8102446291")
    LOG = config("LOG_CHANNEL", "-1002289024376")
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
