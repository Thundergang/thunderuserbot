#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

from telethon import events
from thunderbot import CMD_HELP
import asyncio


@thunderbot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 9)

    input_str = event.pattern_match.group(1)

    if input_str == "thunder":

        await event.edit(input_str)

        animation_chars = [
        
            "You Triggered Me Up",
            "I Am ThunderUserbot",
            "Thunder",
            "Feel",
            "Feel The",    
            "Feel The Thunder",
            "⛈",
            "⚡️",
            "⚡️"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 100])
CMD_HELP.update(
    {
        "thunder": "➟ `.thunder`\nUse - Feel The Thunder"
    }
)
