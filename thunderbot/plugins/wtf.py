#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

"""Emoji
Available Commands:
.wtf"""
import asyncio

from thunderbot.utils import admin_cmd


@thunderbot.on(admin_cmd("wtf"))
async def _(event):
    if event.fwd_from:
        return
    animation_ttl = range(0, 5)
    await event.edit("wtf")
    animation_chars = [
        "What",
        "What The",
        "What The F",
        "What The Fuc",
        "[What The Fuck](https://telegra.ph/file/3eb2619d669a1c0ff5af9.jpg)",
    ]
    for i in animation_ttl:
        await asyncio.sleep(0.3)
        await event.edit(animation_chars[i])
        i += 1
