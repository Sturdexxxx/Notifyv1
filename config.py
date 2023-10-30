from os import environ
import os
import logging
from logging.handlers import RotatingFileHandler

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5417821247:AAFVtQDdpcnXcCt7aWQdBcl13ABuvZlOtXg") #drm
APP_ID = int(os.environ.get("APP_ID", "3393749"))
API_HASH = os.environ.get("API_HASH", "a15a5954a1db54952eebd08ea6c68b71")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001693231644"))
LOG_ID = int(os.environ.get("LOG_ID", "-1001956515516"))
OWNER_ID = int(os.environ.get("OWNER_ID", "5531584953"))
PORT = os.environ.get("PORT", "8080")
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Jayanna:Jayanna2023@yash.tm1c2bd.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "New_Divya_Spandana")
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001239856060"))
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "10"))
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI store private files for @EclipseAnime and other users can access it from special link.")

try:
    ADMINS = []
    for x in os.environ.get("ADMINS", "5531584953 1943966786 5395870942").split():
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"
ADMINS.append(OWNER_ID)
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
     level=logging.INFO,
     format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
     datefmt='%d-%b-%y %H:%M:%S',
     handlers=[
         RotatingFileHandler(
             LOG_FILE_NAME,
             maxBytes=50000000,
             backupCount=10
         ),
         logging.StreamHandler()
     ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫𝐊𝐒
<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}</b>
"""
