#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from thunderbot.utils import admin_cmd

G = ("▄█▀─▄▄▄▄▄▄▄─▀█▄\n"
"▀█████████████▀\n"
"────█▄███▄█\n"
"─────█████\n"
"─────█▀█▀█\n")
H = ("───▄▄─▄████▄▐▄▄▄▌\n"
"──▐──████▀███▄█▄▌\n"
"▐─▌──█▀▌──▐▀▌▀█▀\n"
"─▀───▌─▌──▐─▌\n"
"─────█─█──▐▌█\n")
J = ("──▄──▄────▄▀\n"
"───▀▄─█─▄▀▄▄▄\n"
"▄██▄████▄██▄▀█▄\n"
"─▀▀─█▀█▀▄▀███▀\n"
"──▄▄▀─█──▀▄▄\n")
K = ("░╔╔╩╩╝\n"
"▄██▄\n"
"░░██████▄░░░░░░▄▄▄▄▄▄█\n"
"░░█▀█▀█▀█░░▄░▄████████\n"
"░▄▌▄▌▄▌▄▌░▀▄▄▄▄█▄▄▄▄█▄\n")
L = ("█───▄▀▀▀▀▄─▐█▌▐█▌▐██\n"
"█──▐▄▄────▌─█▌▐█─▐▌─\n"
"█──▐█▀█─▀─▌─█▌▐█─▐██\n"
"█──▐████▄▄▌─▐▌▐▌─▐▌─\n"
"███─▀████▀───██──▐██\n")

@thunderbot.on(admin_cmd(pattern=r"bull"))
async def nandybull(bull):
    await bull.edit(G)
@thunderbot.on(admin_cmd(pattern=r"fox"))
async def nandyfox(fox):
    await fox.edit(H)
@thunderbot.on(admin_cmd(pattern=r"spider"))
async def nandyspider(spider):
    await spider.edit(J)
@thunderbot.on(admin_cmd(pattern=r"winter"))
async def nandywinter(winter):
    await winter.edit(K)
@thunderbot.on(admin_cmd(pattern=r"love"))
async def nandylove(love):
    await love.edit(L)
