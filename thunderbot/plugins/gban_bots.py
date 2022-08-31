#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

"""Globally Ban users from all the
Group Administrations bots where you are SUDO
Available Commands:
.gban REASON
.ungban"""

from thunderbot import CMD_HELP, G_BAN_LOGGER_GROUP
from thunderbot.utils import admin_cmd


@thunderbot.on(admin_cmd(pattern="botgban ?(.*)"))
@thunderbot.on(sudo_cmd(pattern="botgban ?(.*)", allow_sudo=True))
async def _(event):
    if G_BAN_LOGGER_GROUP is None:
        await eor(
            event,
            "Make a group, add all your sudo bots and paste it's id in ENV VAR (G_BAN_LOGGER_GROUP) for this module to work.",
        )
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        if r.forward:
            r_from_id = r.forward.from_id or r.from_id
        else:
            r_from_id = r.from_id
        await borg.send_message(
            G_BAN_LOGGER_GROUP,
            "/gban [user](tg://user?id={}) {}".format(r_from_id, reason),
        )
    await event.delete()


@thunderbot.on(admin_cmd(pattern="botungban ?(.*)"))
@thunderbot.on(sudo_cmd(pattern="botungban ?(.*)", allow_sudo=True))
async def _(event):
    if G_BAN_LOGGER_GROUP is None:
        await eor(
            event,
            "Make a group, add all your sudo bots and paste it's id in ENV VAR (G_BAN_LOGGER_GROUP) for this module to work.",
        )
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        r_from_id = r.from_id
        await borg.send_message(
            G_BAN_LOGGER_GROUP,
            "/ungban [user](tg://user?id={}) {}".format(r_from_id, reason),
        )
    await event.delete()


CMD_HELP.update(
    {
        "gban_bots": ".botgban <reply to user/userid/username> <reason>\nUse - Gban in all bots you are sudo.\
        \n\n.botungban <reply to user/userid/username>\nUse - Ungban from all bots."
    }
)
