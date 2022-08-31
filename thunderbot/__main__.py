#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

import os
import glob
from thunderbot import bot
from sys import argv
from telethon import TelegramClient
from thunderbot.utils import load_module, start_mybot, load_pmbot
from pathlib import Path
import telethon.utils
from thunderbot import CMD_HNDLR, PRIVATE_GROUP_ID
from dotenv import load_dotenv
load_dotenv("config.env")

APP_ID = int(os.environ.get("APP_ID", 6))
API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
STRING_SESSION = os.environ.get("STRING_SESSION", None)
TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
THUND = PRIVATE_GROUP_ID
BOTNAME = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
LOAD_MYBOT = os.environ.get("LOAD_MYBOT", "True")
logo = """
       $$$$$$"
      .$$$$$$"
     .$$$$$$"
    4$$$$$$$$$$$$$"
   z$$$$$$$$$$$$$"
   """ """"3$$$$$"
         z$$$$P
        d$$$$"
      .$$$$$"
     z$$$$$"
    z$$$$P
   d$$$$$$$$$$"
  *******$$$"
       .$$$"
      .$$"
     4$P"
    z$"
   zP
  z"
 /    ThunderGang


████████╗██╗  ██╗██╗   ██╗███╗   ██╗██████╗ ███████╗██████╗ 
╚══██╔══╝██║  ██║██║   ██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
   ██║   ███████║██║   ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
   ██║   ██╔══██║██║   ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
   ██║   ██║  ██║╚██████╔╝██║ ╚████║██████╔╝███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                            


██╗   ██╗███████╗███████╗██████╗ ██████╗  ██████╗ ████████╗
██║   ██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝
██║   ██║███████╗█████╗  ██████╔╝██████╔╝██║   ██║   ██║   
██║   ██║╚════██║██╔══╝  ██╔══██╗██╔══██╗██║   ██║   ██║   
╚██████╔╝███████║███████╗██║  ██║██████╔╝╚██████╔╝   ██║   
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝   
                                                           

"""

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


async def startup_log_all_done():
    try:
        await bot.tgbot.send_message(THUND, f"**ThunderUserbot has been started**")
    except BaseException:
        print("Either PRIVATE_GROUP_ID is wrong or bot isn't a admin in the group")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=APP_ID,
            api_hash=API_HASH
        ).start(bot_token=TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished, no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

path = 'thunderbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))


print("Setting up Assisting Bot")
path = "thunderbot/plugins/lightningbot/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_mybot(shortname.replace(".py", ""))

if LOAD_MYBOT == "True":
    path = "thunderbot/plugins/lightningbot/pmsparkbot/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_pmbot(shortname.replace(".py", ""))
    print("Assisting Bot set up completely!")

print(logo)
print("Thunderuserbot has been started without any issue! Please visit @thunderuserbot on telegram for more")
bot.loop.run_until_complete(startup_log_all_done())

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
