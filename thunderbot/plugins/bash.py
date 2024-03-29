#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

import asyncio
import io
import time

from thunderbot import CMD_HELP
from thunderbot.utils import admin_cmd


@thunderbot.on(admin_cmd(pattern="bash ?(.*)"))
@thunderbot.on(sudo_cmd(pattern="bash ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    PROCESS_RUN_TIME = 100
    cmd = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    e = stderr.decode()
    if not e:
        e = "No Error"
    o = stdout.decode()
    if not o:
        o = "**Tip**: \n`If you want to see the results of your code, I suggest printing them to stdout.`"
    else:
        _o = o.split("\n")
        o = "`\n".join(_o)
    OUTPUT = f"**QUERY**\n\n__►__ **Command**\n`{cmd}`\n\n__►__ **PID**\n`{process.pid}`\n\n**__►__ **stderr** \n`{e}`\n\n**__►__** Output:**\n`{o}`"
    if len(OUTPUT) > 4095:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "exec.txt"
            await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id,
            )
            await event.delete()
    await eor(event, OUTPUT)


CMD_HELP.update({"bash": ".bash <code>\nUse - Run any code."})
