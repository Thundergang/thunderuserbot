#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

import asyncio
from telethon.errors.rpcerrorlist import YouBlockedUserError
from thunderbot import CMD_HELP
bot = "@Indianofficial_Robot"


@thunderbot.on(admin_cmd(pattern="lyrics ?(.*)"))
@thunderbot.on(sudo_cmd(pattern="lyrics ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit("`Searching Your Lyrics...`")
    queryinput = event.pattern_match.group(1)
    if queryinput == "":
        await ok.edit(
            "It Should Be In This Format`.lyrics`songname"
        )
        return
    async with borg.conversation(bot) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("/lyrics " + queryinput)
            thunderlyricdata = await conv.get_response()
            await ok.edit(thunderlyricdata.text + "\n\nLyrics Generated By Your @thunderuserbot")
        except YouBlockedUserError:
            await ok.edit("**Error**\n `Unblock` @Indianofficial_Robot `and try again`!")

CMD_HELP.update(
    {
        "lyrics": "➟ `.lyrics` songname\nUse - Get Lyrics Of Any Song"
    }
)
