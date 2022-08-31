#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

"""Auto Profile Updation Commands
.autoname"""
import asyncio
import time

from telethon.errors import FloodWaitError
from telethon.tl import functions
from thunderbot.utils import admin_cmd
from thunderbot import ALIVE_NAME, CMD_HELP, PRIVATE_GROUP_ID

DEL_TIME_OUT = 60
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "thunderuserbot"


@thunderbot.on(admin_cmd(pattern="autoname"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    while True:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%H:%M")
        name = f"🕒{HM} ⚡{DEFAULTUSER}⚡ {DM} 🗓️"
        logger.info(name)
        try:
            await borg(
                functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                    first_name=name
                )
            )
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)

        # else:
        # logger.info(r.stringify())
        await borg.send_message(
            PRIVATE_GROUP_ID, "#Auto_Name\nSuccessfully started AutoName"
        )
        await asyncio.sleep(DEL_TIME_OUT)
    await event.edit(f"Auto Name has been started...")


CMD_HELP.update({"autoname": ".autoname\nUse - Automatic changing name with time."})
