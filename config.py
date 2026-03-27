import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Tokens (nom nom nom, tasty 🤤😝)
TOKEN = os.getenv("DISCORD_TOKEN")
LOGGING_DEBUG_MODE = os.getenv("LOGGING_DEBUG_MODE", False)
if not TOKEN:
    raise SystemExit("Set DISCORD_TOKEN in .env")

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# Database paths
HDDB_PATH = str(BASE_DIR / "databases" / "haiku_detection.db")
HWDDB_PATH = str(BASE_DIR / "databases" / "haiku_words.db")

# Bot settings
COMMAND_PREFIX = "!!"
