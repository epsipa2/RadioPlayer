import os
import re


class Config:
    ADMIN = os.environ.get("ADMINS", "1548967589 1391755824")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", 6775322))
    CHAT = int(os.environ.get("CHAT", "-1001130413114"))
    LOG_GROUP = os.environ.get("LOG_GROUP", "-1001475839216")
    if LOG_GROUP:
        LOG_GROUP = int(LOG_GROUP)
    else:
        LOG_GROUP = None
    STREAM_URL = os.environ.get("STREAM_URL", "https://radioindia.net/radio/hungamanow/icecast.audio")
    API_HASH = os.environ.get("API_HASH", "89ca2ba997c610e24f82bf4f6c3e777b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1911917540:AAFe-i9h9sOB4erAxk5NhBXz9xEgzRbvJI8") 
    SESSION = os.environ.get("SESSION_STRING", "BAAo9iBSkC1vIhki5uuwwDBhrX7_XWUB-k0Ui_QUXvzU64Nk24wVqE2zam9-oAUMiqKNfV-SHdWMcoaYogxqYu94aRWvEcCTaMt1F7Og3ju0IyFEaR0uwHI6rJ3w8OgJyvX7lFSJ0gYbpIfedArstzJsdbsufsGfQuFCsj_2Q4hlmNKOgbPgJDPSIF0xme36r0cZF9hNv3vbmTMrRRJnFZdLoCeyfceVhX5eBF7tlZXCDSWUrE2O5xwDUVuSUEd8mHBPZH0N5LWWHeO1YkMjEA_x4-WOguxrLHlLLvzBI3OzRbxvWJ31Cys3doMqGQ3C2ZZI3VZBT8ELP5zKk-qHRezka4P1RAA")

