#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

from telethon import events
import os
import requests
import json
from thunderbot.utils import admin_cmd
from thunderbot import CMD_HELP

@thunderbot.on(admin_cmd("duckduckgo (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://duckduckgo.com/?q={}".format(input_str.replace(" ","+"))
    if sample_url:
        link = sample_url.rstrip()
        await event.edit("Let Me 🦆 DuckDuckGo That For From My Thunderuserbot⚡️:\n🔎 [{}]({})".format(input_str, link))
    else:
        await event.edit("something is wrong. please try again later.")


CMD_HELP.update(
    {
        "duckduckgo": ".duckduckgo\nUse - To Get Direct Search Link To Duckduckgo."
    }
)
