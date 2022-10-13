import os
import re


class Config:
    ADMIN = os.environ.get("ADMINS", "5516320714 1970096110")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", 10670890))
    CHAT = int(os.environ.get("CHAT", "-1001768257900"))
    LOG_GROUP = os.environ.get("LOG_GROUP", "-1001768257900")
    if LOG_GROUP:
        LOG_GROUP = int(LOG_GROUP)
    else:
        LOG_GROUP = None
    STREAM_URL = os.environ.get("STREAM_URL", "https://www.liveradio.ie/stations/np-24-radio")
    API_HASH = os.environ.get("API_HASH", "b8c18624a9a4b397e9989c30904de9d2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5691474077:AAEzVyiiKbfwM5xmADq2b9s4rIJrAiUWmy8") 
    SESSION = os.environ.get("SESSION_STRING", "BAAo9iBSkC1vIhki5uuwwDBhrX7_XWUB-k0Ui_QUXvzU64Nk24wVqE2zam9-oAUMiqKNfV-SHdWMcoaYogxqYu94aRWvEcCTaMt1F7Og3ju0IyFEaR0uwHI6rJ3w8OgJyvX7lFSJ0gYbpIfedArstzJsdbsufsGfQuFCsj_2Q4hlmNKOgbPgJDPSIF0xme36r0cZF9hNv3vbmTMrRRJnFZdLoCeyfceVhX5eBF7tlZXCDSWUrE2O5xwDUVuSUEd8mHBPZH0N5LWWHeO1YkMjEA_x4-WOguxrLHlLLvzBI3OzRbxvWJ31Cys3doMqGQ3C2ZZI3VZBT8ELP5zKk-qHRezka4P1RAA")

