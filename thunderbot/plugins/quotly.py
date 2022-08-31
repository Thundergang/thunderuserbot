#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from thunderbot.utils import admin_cmd
from thunderbot import CMD_HELP


@thunderbot.on(admin_cmd(pattern="qbot ?(.*)"))
@thunderbot.on(sudo_cmd(pattern="qbot ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await eor(event, "```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await eor(event, "```Reply to text message```")
        return
    chat = "@QuotLyBot"
    reply_message.sender
    if reply_message.sender.bot:
        await eor(event, "```Reply to actual users message.```")
        return
    await eor(event, "```Making a Quote```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1031952739)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please Unblock (@QuotLyBot) And Try Again```")
            return
        if response.text.startswith("Hi!"):
            await eor(
                event,
                "```Can you kindly disable your forward privacy settings for good?```",
            )
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update({"quotly": ".qbot <reply to message>\nUse - To make a quote."})
