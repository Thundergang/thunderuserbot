#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

import os
from thunderbot import *
from telethon.tl.functions.users import GetFullUserRequest

sudousers = os.environ.get("SUDO_USERS", None)


@thunderbot.on(admin_cmd(pattern="sudo"))
async def sudo(event):
    sudo = "True" if SUDO_USERS else "False"
    users = os.environ.get("SUDO_USERS", None)
    if sudo == "True":
        await eor(event, f"**ThunderUserbot**\nSudo - `Enabled`\nSudo user(s) - `{users}`")
    else:
        await eor(event, f"**ThunderUserbot**\nSudo - `Disabled`")


@thunderbot.on(admin_cmd(pattern="prefix"))
async def handler(event):
    hndlr = CMD_HNDLR
    if hndlr == r"\.":
        x = "."
    else:
        x = CMD_HNDLR

    sudohndlr = SUDO_HNDLR
    await eor(event, f"Command Handler - {x}\nSudo Handler - {sudohndlr}")



async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target
