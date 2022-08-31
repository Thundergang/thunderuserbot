#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from thunderbot.utils import admin_cmd

Z = ("░▄░█░░░▄▀▀▀▀▀▄░░░█░▄░\n"
"▄▄▀▄░░░█─▀─▀─█░░░▄▀▄▄\n"
"░░░░▀▄▒▒▒▒▒▒▒▒▒▄▀░░░░\n"
"░░░░░█────▀────█░░░░░\n"
"░░░░░█────▀────█░░░░░\n")
X = ("░░░░░░░░░░░░░░░░▄▓▄\n"
"░░░░▄█▄░░░░░░░░▄▓▓▓▄\n"
"░░▄█████▄░░░░░▄▓▓▓▓▓▄\n"
"░▀██┼█┼██▀░░░▄▓▓▓▓▓▓▓▄\n"
"▄▄███████▄▄▄▄▄▄▄▄█▄▄▄▄\n")
C = ("░▄▀▀▀▀▄░░▄▄\n"
"█░░░░░░▀▀░░█░░░░░░▄░▄\n"
"█░║░░░░██░████████████ \n"
"█░░░░░░▄▄░░█░░░░░░▀░▀\n"
"░▀▄▄▄▄▀░░▀▀\n")
V = ("░▄▌░░░░░░░░░▄\n"
"████████████▄\n"
"░░░░░░░░▀▐████\n"
"░░░░░░░░░░░▐██▌\n")
B = ("─────▀▄▀─────▄─────▄\n"
"──▄███████▄──▀██▄██▀\n"
"▄█████▀█████▄──▄█\n"
"███████▀████████▀\n"
"─▄▄▄▄▄▄███████▀\n")

@thunderbot.on(admin_cmd(pattern=r"snowman"))
async def nandysnowman(snowman):
    await snowman.edit(Z)
@thunderbot.on(admin_cmd(pattern=r"home"))
async def nandyhome(home):
    await home.edit(X)
@thunderbot.on(admin_cmd(pattern=r"guitar"))
async def nandyguitar(guitar):
    await guitar.edit(C)
@thunderbot.on(admin_cmd(pattern=r"pistol"))
async def nandypistol(pistol):
    await pistol.edit(V)
@thunderbot.on(admin_cmd(pattern=r"whale"))
async def nandywhale(whale):
    await whale.edit(B)
