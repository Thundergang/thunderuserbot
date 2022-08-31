#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

import os
import pygments
from pygments.formatters import ImageFormatter
from pygments.lexers import Python3Lexer
from thunderbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from thunderbot.utils import admin_cmd, sudo_cmd


@thunderbot.on(admin_cmd(pattern=r"ncode"))
@thunderbot.on(sudo_cmd(pattern=r"ncode", allow_sudo=True))
async def coder_print(event):
    a = await event.client.download_media(
        await event.get_reply_message(), TEMP_DOWNLOAD_DIRECTORY
    )
    s = open(a, "r")
    c = s.read()
    s.close()
    pygments.highlight(
        f"{c}",
        Python3Lexer(),
        ImageFormatter(font_name="DejaVu Sans Mono", line_numbers=True),
        "result.png",
    )
    res = await event.client.send_message(
        event.chat_id,
        "**Pasting this code on my page...**",
        reply_to=event.reply_to_msg_id,
    )
    await event.client.send_file(
        event.chat_id, "result.png", force_document=True, reply_to=event.reply_to_msg_id
    )
    # await event.client.send_file(event.chat_id, "resuly.png",
    # force_document=False, reply_to=event.reply_to_msg_id)
    await res.delete()
    await event.delete()
    os.remove(a)
    os.remove("result.png")


CMD_HELP.update(
    {"ncode": ".ncode <file>\nUse - Paste the contents of file and send as pic."}
)
