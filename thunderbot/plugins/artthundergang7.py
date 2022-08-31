#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from thunderbot.utils import admin_cmd

RR = ("───▄▄▄\n"
"─▄▀░▄░▀▄\n"
"─█░█▄▀░█\n"
"─█░▀▄▄▀█▄█▄▀\n"
"▄▄█▄▄▄▄███▀\n")
TT = ("─────────█▄██▄█\n"
"█▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█\n"
"███┼█████▐████▌█████┼███\n"
"█████████▐████▌█████████\n")
YY = ("─▀▀▌───────▐▀▀\n"
"─▄▀░◌░░░░░░░▀▄\n"
"▐░░◌░▄▀██▄█░░░▌\n"
"▐░░░▀████▀▄░░░▌\n"
"═▀▄▄▄▄▄▄▄▄▄▄▄▀═\n")
UU = ("░░█▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
"██▀▀▀██▀▀▀▀▀▀██▀▀▀██\n"
"█▒▒▒▒▒█▒▀▀▀▀▒█▒▒▒▒▒█\n"
"█▒▒▒▒▒█▒████▒█▒▒▒▒▒█\n"
"██▄▄▄██▄▄▄▄▄▄██▄▄▄██\n")
II = ("▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░\n"
"▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░\n"
"▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░\n"
"▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░\n"
"░░░░▄▄███▄▄░░░░░█████░\n")

@thunderbot.on(admin_cmd(pattern=r"snail"))
async def nandysnail(snail):
    await snail.edit(RR)
@thunderbot.on(admin_cmd(pattern=r"fort"))
async def nandyfort(fort):
    await fort.edit(TT)
@thunderbot.on(admin_cmd(pattern=r"fish"))
async def nandyfish(fish):
    await fish.edit(YY)
@thunderbot.on(admin_cmd(pattern=r"radio"))
async def nandyradio(radio):
    await radio.edit(UU)
@thunderbot.on(admin_cmd(pattern=r"computer"))
async def nandycomputer(computer):
    await computer.edit(II)
