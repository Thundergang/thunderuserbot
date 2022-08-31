#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

import asyncio
import requests
import urllib
import json
import os
from telethon import events
from thunderbot.utils import admin_cmd
from thunderbot import CMD_HELP

@thunderbot.on(admin_cmd(pattern="animepic"))
async def _(event):
    if event.fwd_from:
        return
    with urllib.request.urlopen(
            "https://api.waifu.pics/sfw/waifu"
    ) as url:
        data = json.loads(url.read().decode())
    finalcat = (data['url'])
    r = requests.get(finalcat, allow_redirects=True)
    open('animepicthunder.jpg', 'wb').write(r.content)
    await thunderbot.send_file(
                        event.chat_id,
                        'animepicthunder.jpg',
                        caption=f"Here's Your Waifu..\nGathered By Your @thunderuserbot",
                    )
    os.system("rm animepicthunder.jpg")

CMD_HELP.update(
    {
        "animepics": "➟ `.animepic \nUse - Get Random Waifu Images"
    }
)
