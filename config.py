from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN") # your discord bot's token here!
PREFIX = os.environ.get("BOT_PREFIX") # your bot's prefix.
ERROR_CHANNEL = os.environ.get("ERROR_CHANNEL") # all the error's caused by command and events, etc will send here.
