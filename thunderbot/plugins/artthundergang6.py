#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from thunderbot.utils import admin_cmd

N = ("▄▀─────────────▀▄\n"
"█▄█──█▀█─█▀█─▄█▄█\n"
"─▀██▄▀▄▀─▀▄▀▄██▀\n"
"░░░▄██▀███▀███▄\n"
"░▐▀█▀██▄▄▄██▀█▀▌\n")
M = ("║░█░█░║░█░█░█░║░█░█░║\n"
"║░█░█░║░█░█░█░║░█░█░║\n"
"║░║░║░║░║░║░║░║░║░║░║\n"
"╚═╩═╩═╩═╩═╩═╩═╩═╩═╩═╝\n")
QQ = ("───────▄██████▄───────\n"
"──────▐▀▀▀▀▀▀▀▀▌──────\n"
"──────▌▌▀▀▌▐▀▀▐▐──────\n"
"──────▐──▄▄▄▄──▌──────\n"
"───────▌▐▌──▐▌▐───────\n")
WW = ("───▄▀▀▀▀▀───▄█▀▀▀█▄\n"
"──▐▄▄▄▄▄▄▄▄██▌▀▄▀▐██\n"
"──▐▒▒▒▒▒▒▒▒███▌▀▐███\n"
"───▌▒▓▒▒▒▒▓▒██▌▀▐██\n"
"───▌▓▐▀▀▀▀▌▓─▀▀▀▀▀\n")
EE = ("──███▅▄▄▄▄▄▄▄▄▄\n"
"─██▐████████████\n"
"▐█▀████████████▌▌\n"
"▐─▀▀▀▐█▌▀▀███▀█─▌\n"
"▐▄───▄█───▄█▌▄█\n")

@thunderbot.on(admin_cmd(pattern=r"crab"))
async def nandycrab(crab):
    await crab.edit(N)
@thunderbot.on(admin_cmd(pattern=r"piano"))
async def nandypiano(piano):
    await piano.edit(M)
@thunderbot.on(admin_cmd(pattern=r"man"))
async def nandyman(man):
    await man.edit(QQ)
@thunderbot.on(admin_cmd(pattern=r"lion"))
async def nandylion(lion):
    await lion.edit(WW)
@thunderbot.on(admin_cmd(pattern=r"elephant"))
async def nandyelephant(elephant):
    await elephant.edit(EE)
