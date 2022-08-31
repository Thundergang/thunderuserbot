#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.


from telethon.tl.types import Channel

from thunderbot import *
from thunderbot import ALIVE_NAME, bot, thunderversion

if PRIVATE_GROUP_ID:
    log = "Enabled"
else:
    log = "Disabled"

if TG_BOT_USER_NAME_BF_HER:
    bots = "Enabled"
else:
    bots = "Disabled"
if SUDO_USERS:
    sudo = "Disabled"
else:
    sudo = "Enabled"

if PMSECURITY.lower() == "off":
    pm = "Disabled"
else:
    pm = "Enabled"

THETHUNDERUSER = str(ALIVE_NAME) if ALIVE_NAME else "@thunderuserbot"

thundrgang = f"ThunderUserbot Version: {thunderversion}\n"
thundrgang += f"Log Group: {log}\n"
thundrgang += f"Support Bot: {bots}\n"
thundrgang += f"Sudo Status: {sudo}\n"
thundrgang += f"PMSecurity: {pm}\n"
thundrgang += f"\nVisit @thunderuserbot for any help.\n"
thundrstats = f"{thundrgang}"

THEFIRST_NAME = bot.me.first_name
OWNER_ID = bot.me.id

# Counting number of groups


async def thethundr_grps(event):
    a = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):
            if entity.megagroup:
                if entity.creator or entity.admin_rights:
                    a.append(entity.id)
    return len(a), a
