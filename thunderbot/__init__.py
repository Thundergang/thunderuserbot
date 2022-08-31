#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

from requests import get
import pylast
import asyncio
from distutils.util import strtobool as sb
from logging import basicConfig, getLogger, INFO, DEBUG
import os
import sys
from telethon.sessions import StringSession
from telethon import TelegramClient
import time

from dotenv import load_dotenv
load_dotenv("config.env")

APP_ID = int(os.environ.get("APP_ID", 6))
API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
STRING_SESSION = os.environ.get("STRING_SESSION") or None
session_name = str(STRING_SESSION)
bot = TelegramClient(StringSession(session_name), APP_ID, API_HASH)

TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "thunderuserbot")
CHANNEL_ID = os.environ.get("PRIVATE_GROUP_ID", None)
ENV = os.environ.get("ENV", False)
""" PPE initialization. """

CONSOLE_LOGGER_VERBOSE = sb(
    os.environ.get(
        "CONSOLE_LOGGER_VERBOSE",
        "False"))

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(
        format="✘ %(asctime)s ✘ - ⫸ %(name)s ⫷ - ⛝ %(levelname)s ⛝ - ║ %(message)s ║",
        level=INFO)
LOGS = getLogger(__name__)

CONFIG_CHECK = os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

if CONFIG_CHECK:
    LOGS.info(
        "Please remove the line mentioned in the first hashtag from the config.env file"
    )
    quit(1)

# Logging channel/group configuration.
BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID", None)
try:
    BOTLOG_CHATID = int(BOTLOG_CHATID)
except BaseException:
    pass

# Userbot logging feature switch.
BOTLOG = sb(os.environ.get("BOTLOG", "False"))
UB_BLACK_LIST_CHAT = os.environ.get("UB_BLACK_LIST_CHAT", None)
SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)
ALL_FEDS = os.environ.get("ALL_FEDS", None)
MASSFBAN_GROUP_ID = os.environ.get("MASSFBAN_GROUP_ID", None)
MAX_MESSAGE_SIZE_LIMIT = os.environ.get("MAX_MESSAGE_SIZE_LIMIT", "4095")
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

# Console verbose logging
CONSOLE_LOGGER_VERBOSE = sb(
    os.environ.get(
        "CONSOLE_LOGGER_VERBOSE",
        "False"))

# SQL Database URI
DB_URI = os.environ.get("DB_URI")

# OCR API key
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

# remove.bg API key
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

# Chrome Driver and Headless Google Chrome Binaries
CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)

# For bit.ly plugin
BITLY_TOKEN = os.environ.get("BITLY_TOKEN", None)

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)

# Anti Spambot Config
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))

ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

# Youtube API key
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

# Default .alive name
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)

AUTOPIC_FONT_COLOUR = os.environ.get("AUTOPIC_FONT_COLOUR", None)

# Time & Date - Country and Time Zone
COUNTRY = str(os.environ.get("COUNTRY", ""))

TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

# Clean Welcome
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# CUSTOM PMPERMIT
CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)

# Last.fm Module
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)

LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = pylast.md5(LASTFM_PASSWORD_PLAIN)
if not LASTFM_USERNAME == "None":
    lastfm = pylast.LastFMNetwork(api_key=LASTFM_API,
                                  api_secret=LASTFM_SECRET,
                                  username=LASTFM_USERNAME,
                                  password_hash=LASTFM_PASS)
else:
    lastfm = None

# Google Drive Module
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./Extras/downloads")
G_BAN_LOGGER_GROUP = os.environ.get("G_BAN_LOGGER_GROUP", None)
# importing ones
LOGGER = True
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
#SUDO_USERS = set(
#    int(x) for x in os.environ.get(
#        "SUDO_USERS", "").split())
SUDO_USERS = os.environ.get("SUDO_USERS", None)
WHITELIST_USERS = set(
    int(x) for x in os.environ.get(
        "WHITELIST_USERS",
        "1344584512").split())
BLACKLIST_USERS = set(
    int(x) for x in os.environ.get(
        "BLACKLIST_USERS", "").split())
DEVLOPERS = set(
    int(x) for x in os.environ.get(
        "DEVLOPERS",
        "1261589721").split())
THUNDER_OWNER = set(
    int(x) for x in os.environ.get(
        "THUNDER_OWNER",
        "1524091402").split())
SUPPORT_USERS = set(
    int(x) for x in os.environ.get(
        "SUPPORT_USERS", "").split())
ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
CUSTOM_ALIVE = os.environ.get("CUSTOM_ALIVE", None)
CUSTOM_ALIVE_EMOJI = os.environ.get("CUSTOM_ALIVE_EMOJI", None)
CUSTOM_AFK = os.environ.get("CUSTOM_AFK", None)
CUSTOM_STICKER_PACK_NAME = os.environ.get("CUSTOM_STICKER_PACK_NAME", None)
BOT_PIC = os.environ.get("BOT_PIC", None)
PMBOT_START_MSSG = os.environ.get("PMBOT_START_MSSG", None)
LESS_SPAMMY = os.environ.get("LESS_SPAMMY", None)
TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
NO_SONGS = bool(os.environ.get("NO_SONGS", False))
DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
MAX_FLOOD_IN_P_M_s = os.environ.get("MAX_FLOOD_IN_P_M_s", "3")
MAX_SPAM = os.environ.get("MAX_FLOOD_IN_P_M_s", "3")
AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
PMSECURITY = os.environ.get("PMSECURITY", "ON")
CMD_HNDLR = os.environ.get("CMD_HNDLR", r"\.")
SUDO_HNDLR = os.environ.get("SUDO_HNDLR", r"\!")
AUTOPIC_TEXT = os.environ.get(
    "AUTOPIC_TEXT",
    "Autopic.\n Thunderuserbot by Thundergang.")
AUTO_PIC_FONT = os.environ.get("AUTOPIC_FONT", "thundergangfont.ttf")
if AUTH_TOKEN_DATA is not None:
    os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    t_file = open(TEMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
    t_file.write(AUTH_TOKEN_DATA)
    t_file.close()
LOAD_MYBOT = os.environ.get("LOAD_MYBOT", "True")
PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", None)
if PRIVATE_GROUP_ID is not None:
    try:
        PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
    except ValueError:
        raise ValueError(
            "Invalid Private Group ID. Make sure the ID starts with -100.")
# importing ends
StartTime = time.time()
thunderversion = "2.0"

CMD_LIST = {}
CMD_HELP = {}
INT_PLUG = ""
LOAD_PLUG = {}
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
ISAFK = False
AFKREASON = None
