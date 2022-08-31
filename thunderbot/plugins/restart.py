#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

import os
import sys
from thunderbot import CMD_HELP, CMD_HNDLR
from thunderbot.utils import admin_cmd


@thunderbot.on(admin_cmd(pattern="restart"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(
        f"**Restarting Your Thunderuserbot**.. Please Wait Until It Starts Again "
    )
    await thunderbot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()

CMD_HELP.update(
    {
        "restart": ".restart\nUse - Restarts the bot."
    }
)
