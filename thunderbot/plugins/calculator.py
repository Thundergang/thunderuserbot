#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

import io
import sys
import traceback

from thunderbot import CMD_HELP
from thunderbot.utils import admin_cmd


@thunderbot.on(admin_cmd(pattern="calc"))
@thunderbot.on(sudo_cmd(pattern="calc", allow_sudo=True))
async def _(event):
    if event.fwd_from or event.via_bot_id:
        return
    x = await eor(event, "Processing ...")
    cmd = event.text.split(" ", maxsplit=1)[1]
    event.message.id
    if event.reply_to_msg_id:
        event.reply_to_msg_id

    san = f"print({cmd})"
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(san, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Something went wrong"

    final_output = "**EQUATION**: `{}` \n\n **SOLUTION**: \n`{}` \n".format(
        cmd, evaluation
    )
    await x.edit(final_output)


async def aexec(code, event):
    exec(f"async def __aexec(event): " + "".join(f"\n {l}" for l in code.split("\n")))
    return await locals()["__aexec"](event)


CMD_HELP.update(
    {
        "calculator": ".calc <equation>\
      \nUse - Just a simple calculator. "
    }
)
