#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

import asyncio
import os
from datetime import datetime
from pathlib import Path

from telethon.tl.types import InputMessagesFilterDocument

from thunderbot import CMD_HELP
from thunderbot.utils import admin_cmd, load_module, remove_plugin

from .. import ALIVE_NAME

DELETE_TIMEOUT = 5
thumb_image_path = "./Extras/logo.jpg"
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ThunderUserbot User"


@thunderbot.on(admin_cmd(pattern=r"send (?P<shortname>\w+)", outgoing=True))
@thunderbot.on(sudo_cmd(pattern=r"send (?P<shortname>\w+)", allow_sudo=True))
async def send(event):
    ok = await eor(event, "Sending...")
    if event.fwd_from:
        return
    hmm = bot.uid
    message_id = event.message.id
    thumb = thumb_image_path
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./thunderbot/plugins/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        await ok.delete()
        start = datetime.now()
        pro = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            allow_cache=False,
            thumb=thumb,
            reply_to=message_id,
        )
        end = datetime.now()
        time_taken_in_ms = (end - start).seconds
        await pro.edit(
            f"**⚡️ Plugin Name:** `{input_str}`\n**⚡️ Uploaded in {time_taken_in_ms} seconds.**\n**⚡️ Uploaded by:** [{DEFAULTUSER}](tg://user?id={hmm})\n\nThanks to @thunderuserbot"
        )
        await asyncio.sleep(DELETE_TIMEOUT)
    else:
        await ok.edit("**404**: `No Such Plugin Found!`")


@thunderbot.on(admin_cmd(pattern="install"))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "thunderbot/plugins/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.edit(
                    "ThunderUserbot Succesfully Installed The Plugin `{}`".format(
                        os.path.basename(downloaded_file_name)
                    )
                )
            else:
                os.remove(downloaded_file_name)
                await event.edit(
                    "**Error!**\nPlugin cannot be installed!\nMight have been pre-installed."
                )
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


@thunderbot.on(admin_cmd(pattern=r"unload (?P<shortname>\w+)$"))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await event.edit(f"Thunderuserbot has successfully unloaded {shortname}")
    except Exception as e:
        await event.edit(
            "ThunderUserbot has successfully unloaded {shortname}\n{}".format(
                shortname, str(e)
            )
        )


@thunderbot.on(admin_cmd(pattern=r"load (?P<shortname>\w+)$"))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await event.edit(f"ThunderUserbot has successfully loaded {shortname}")
    except Exception as e:
        await event.edit(
            f"ThunderUserbot could not load {shortname} because of the following error.\n{str(e)}"
        )


@thunderbot.on(admin_cmd(pattern=r"installall$"))
async def install(event):
    if event.fwd_from:
        return
    documentss = await event.client.get_messages(
        event.chat_id, None, search=".py", filter=InputMessagesFilterDocument
    )
    total = int(documentss.total)
    total_doxx = range(0, total)
    b = await event.client.send_message(
        event.chat_id,
        f"**Installing {total} plugins...**\n`This msg will be deleted after the installation gets completed`",
    )
    text = "**Installing Plugins...**\n\n"
    a = await event.client.send_message(event.chat_id, text)
    if total == 0:
        await a.edit("**No plugins to install.**")
        await event.delete()
        return
    for ixo in total_doxx:
        mxo = documentss[ixo].id
        downloaded_file_name = await event.client.download_media(
            await event.client.get_messages(event.chat_id, ids=mxo), "thunderbot/plugins/"
        )
        if "(" not in downloaded_file_name:
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            try:
                load_module(shortname.replace(".py", ""))
                text += f"**• Installed** `{(os.path.basename(downloaded_file_name))}` **successfully.**\n"
            except BaseException:
                text += f"**• Error installing** `{(os.path.basename(downloaded_file_name))}`\n"
        else:
            text += f"**• Plugin** `{(os.path.basename(downloaded_file_name))}` **already installed.**\n"
        await a.edit(f"{text}\n**Installed every plugin.**")
        await event.delete()
        await b.delete()


CMD_HELP.update(
    {
        "core": ".load <plugin name>\nUse - Load the plugin.\
        \n\n.unload <plugin name>\nUse - Unload the plugin.\
        \n\n.install <reply to plugin file (.py)>\nUse - Install the plugin.\
        \n\n.installall\nUse - Install all the plugins in the group/channel where it is used in.\
        \n\n.send <plugin name>\nUse - Send the plugin."
    }
)
