#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from thunderbot.utils import admin_cmd

T = ("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
"█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n"
"█░░║║║╠─║─║─║║║║║╠─░░█\n"
"█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
"█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")
Y = ("──────▄▀─\n"
"─█▀▀▀█▀█─\n"
"──▀▄░▄▀──\n"
"────█────\n"
"──▄▄█▄▄──\n")
U = ("─▄▀▀███═◯\n"
"▐▌▄▀▀█▀▀▄\n"
"█▐▌─────▐▌\n"
"█▐█▄───▄█▌\n"
"▀─▀██▄██▀\n")
I = ("───────────▀▄\n"
"──█▄▄▄▄▄███▀▄─▄▄\n"
"▄▀──▀▄─▀▀█▀▀▄▀──▀▄\n"
"▀▄▀▀█▀▀████─▀▄──▄▀\n"
"──▀▀──────────▀▀\n")
O = ("O────────────────O\n"
"█▓██▄────────────█\n"
"█▓▓░▀▄▀░░░░░░░░░░█\n"
"█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
"█────────────────█\n")

@thunderbot.on(admin_cmd(pattern=r"welcome"))
async def nandywelcome(welcome):
    await welcome.edit(T)
@thunderbot.on(admin_cmd(pattern=r"drink"))
async def nandydrink(drink):
    await drink.edit(Y)
@thunderbot.on(admin_cmd(pattern=r"bomb"))
async def nandybomb(bomb):
    await bomb.edit(U)
@thunderbot.on(admin_cmd(pattern=r"bike"))
async def nandybike(bike):
    await bike.edit(I)
@thunderbot.on(admin_cmd(pattern=r"goodnight"))
async def nandygoodnight(goodnight):
    await goodnight.edit(O)