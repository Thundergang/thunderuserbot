#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

from thunderbot import CMD_HELP, TG_BOT_TOKEN_BF_HER


@thunderbot.on(admin_cmd(pattern=r"echo (.*)"))
@thunderbot.on(sudo_cmd(pattern=r"echo ( .*)", allow_sudo=True))
async def _(event):
    bxt = TG_BOT_USER_NAME_BF_HER
    try:
        tex = str(event.text[6:])
        await tgbot.send_message(event.chat_id, tex)
        await event.delete()
    except BaseException:
        await event.client.send_message(event.chat_id, f"Please add @{bxt} here first!")
        await event.delete()


CMD_HELP.update(
    {
        "echo": ".echo <mssg>\nUse - Echoes the message you send via your bot. You must add it to this chat first."
    }
)
