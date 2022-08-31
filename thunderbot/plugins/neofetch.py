#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from thunderbot import CMD_HELP
import os
import asyncio


@thunderbot.on(admin_cmd(outgoing=True, pattern="neofetch"))
@thunderbot.on(sudo_cmd(outgoing=True, pattern="neofetch", allow_sudo=True))
async def neofetchdetails(neofetch):
    """Neofetch For ThunderUserbot"""
    if not neofetch.text[0].isalpha() and neofetch.text[0] not in ("/", "#", "@", "!"):
        try:
            fetch = await asyncrunapp(
                "neofetch", "--stdout", stdout=asyncPIPE, stderr=asyncPIPE
            )

            stdout, stderr = await fetch.communicate()
            result = str(stdout.decode().strip()) + str(stderr.decode().strip())

            await neofetch.edit("`" + result + "`")
        except FileNotFoundError:
            await neofetch.edit("`Neofetch Not Found.. Please Install The Latest Version Of ThunderUserbot Or Get Help From Support Group` @thunderuserbot")


CMD_HELP.update(
    {
        "neofetch": "➟ `.neofetch`\nUse - Neofetch"
    }
)
