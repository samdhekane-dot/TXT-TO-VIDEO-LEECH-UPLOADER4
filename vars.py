

from os import environ

API_ID = int(environ.get("API_ID", "32344313"))
API_HASH = environ.get("API_HASH", "e2b8eeecfb90695cfbeead46a590ae97")
BOT_TOKEN = environ.get("BOT_TOKEN", "8026664937:AAF9UH9VxK9LGRcZje4cSfxE2ojsXOnVzFY")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "ZCYT_2026Course")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/ZCYT_2026Course")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "6419066600").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "8398501681"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")






