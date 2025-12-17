

from os import environ

API_ID = int(environ.get("API_ID", "29141829"))
API_HASH = environ.get("API_HASH", "25020d00fbcfd406fc9979d24d761bff")
BOT_TOKEN = environ.get("BOT_TOKEN", "8201565286:AAFUe4J2GsmcPd1Jp4U6l2hJiEHBUOoo_CE")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "roxybasicneedbot1")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/roxybasicneedbot1")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "5323404314").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "5323404314"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")





