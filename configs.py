# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 6682330))
    API_HASH = os.environ.get("API_HASH", "a1c264a07c3d7e1eedc83c746a4a9777")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5575527838:AAF5kKxE3my_sMa3rlPS1ekhytcKNA_LKwk")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Footer-Bot")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1002092818514))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1669772418))
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://tanujairam:tanujairam@whatsapp.yixkzgb.mongodb.net/?retryWrites=true&w=majority&appName=Whatsapp")
    START_TEXT = """Hi {name},I am a anjumani footer bot join my channel https://t.me/anjumani_zone!

Don't use my bot or you will get ban !!
"""


 
