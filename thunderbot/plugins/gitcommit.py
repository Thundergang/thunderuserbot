#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

"""
GITHUB File Uploader Plugin for userbot.
Instructions:- Set GITHUB_ACCESS_TOKEN and GIT_REPO_NAME Variables in vars First
usage:- .commit reply_to_any_plugin //can be any type of file too. but for plugin must be in .py
"""


import os
import time
from datetime import datetime

from github import Github

from thunderbot import CMD_HELP, GITHUB_ACCESS_TOKEN, GIT_REPO_NAME

GIT_TEMP_DIR = "./userbot/temp/"


@thunderbot.on(admin_cmd(pattern="commit", outgoing=True))
@thunderbot.on(sudo_cmd(pattern="commit", allow_sudo=True))
async def download(event):
    if event.fwd_from:
        return
    if GITHUB_ACCESS_TOKEN is None:
        await eor(event, "`Please ADD Proper Access Token from github.com`")
        return
    if GIT_REPO_NAME is None:
        await eor(event, "`Please ADD Proper Github Repo Name of your userbot`")
        return
    mone = await event.reply("Processing ...")
    if not os.path.isdir(GIT_TEMP_DIR):
        os.makedirs(GIT_TEMP_DIR)
    start = datetime.now()
    reply_message = await event.get_reply_message()
    try:
        time.time()
        print("Downloading to TEMP directory")
        downloaded_file_name = await bot.download_media(
            reply_message.media, GIT_TEMP_DIR
        )
    except Exception as e:
        await mone.edit(str(e))
    else:
        end = datetime.now()
        ms = (end - start).seconds
        await event.delete()
        await mone.edit(
            "Downloaded to `{}` in {} seconds.".format(downloaded_file_name, ms)
        )
        await mone.edit("Committing to Github....")
        await git_commit(downloaded_file_name, mone)


async def git_commit(file_name, mone):
    content_list = []
    access_token = GITHUB_ACCESS_TOKEN
    g = Github(access_token)
    file = open(file_name, "r", encoding="utf-8")
    commit_data = file.read()
    repo = g.get_repo(GIT_REPO_NAME)
    print(repo.name)
    create_file = True
    contents = repo.get_contents("")
    for content_file in contents:
        content_list.append(str(content_file))
        print(content_file)
    for i in content_list:
        create_file = True
        if i == 'ContentFile(path="' + file_name + '")':
            return await mone.edit("`File Already Exists`")
            create_file = False
    file_name = "userbot/plugins/" + file_name
    if create_file:
        file_name = file_name.replace("./userbot/temp/", "")
        print(file_name)
        try:
            repo.create_file(
                file_name, "Uploaded New Plugin", commit_data, branch="master"
            )
            print("Committed File")
            ccess = GIT_REPO_NAME
            ccess = ccess.strip()
            await mone.edit(
                f"`Commited On Your Github Repo`\n\n[Your Standard Plugins](https://github.com/{ccess}/tree/master/userbot/plugins/)"
            )
        except BaseException:
            print("Cannot Create Plugin")
            await mone.edit("Cannot Upload Plugin")
    else:
        return await mone.edit("`Committed Suicide`")


CMD_HELP.update(
    {
        "gitcommit": ".commit <reply to file>\nUse - Commit the file directly to your git repo/fork.\n"
    }
)
