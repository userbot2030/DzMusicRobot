class Config(object):
    LOGGER = True

    API_ID = 16452568
    API_HASH = "f936697c5c9e5bffd433babef7a4e4c9"
    TOKEN = "6049689032:AAH_Nmx-icacIb5FEAolpLdyiUnZjH11SU4"
    OWNER_ID = 1337085565
    EVENT_LOGS = ()
    SUPPORT_CHAT = "envSample"
    DATABASE_URL = "postgres://xgjapvne:JAVP4wiquJr5a-99moi-XV4EYxBZ4F3X@hansken.db.elephantsql.com/xgjapvne"
    MONGO_DB_URI = "mongodb+srv://elia:chan@elia.peyngcs.mongodb.net/?retryWrites=true&w=majority"
    START_IMG = ""
    CASH_API_KEY = ""
    TIME_API_KEY = ""

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
