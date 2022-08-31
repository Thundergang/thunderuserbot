#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

from thunderbot.utils import admin_cmd
from thunderbot import CHANNEL_ID

@thunderbot.on(admin_cmd(pattern="frwd"))
@thunderbot.on(sudo_cmd(pattern="frwd", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if CHANNEL_ID is None:
        await eor(
            event,
            "Please set the required environment variable `CHANNEL_ID` for this plugin to work",
        )
        return
    try:
        e = await borg.get_entity(CHANNEL_ID)
    except Exception as e:
        await eor(event, str(e))
    else:
        re_message = await event.get_reply_message()
        fwd_message = await borg.forward_messages(e, re_message, silent=True)
        await borg.forward_messages(event.chat_id, fwd_message)
        await fwd_message.delete()
        await event.delete()
