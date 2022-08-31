#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

import requests
import bs4
import re
from telethon import *
from thunderbot.utils import admin_cmd
from thunderbot import CMD_HELP




@thunderbot.on(admin_cmd(pattern="app (.*)"))

async def apk(e):

    try:

        app_name = e.pattern_match.group(1)

        remove_space = app_name.split(' ')

        final_name = '+'.join(remove_space)

        page = requests.get("https://play.google.com/store/search?q="+final_name+"&c=apps")

        lnk = str(page.status_code)

        soup = bs4.BeautifulSoup(page.content,'lxml', from_encoding='utf-8')

        results = soup.findAll("div","ZmHEEd")

        app_name = results[0].findNext('div', 'Vpfmgd').findNext('div', 'WsMG1c nnK0zc').text

        app_dev = results[0].findNext('div', 'Vpfmgd').findNext('div', 'KoLSrc').text

        app_dev_link = "https://play.google.com"+results[0].findNext('div', 'Vpfmgd').findNext('a', 'mnKHRc')['href']

        app_rating = results[0].findNext('div', 'Vpfmgd').findNext('div', 'pf5lIe').find('div')['aria-label']

        app_link = "https://play.google.com"+results[0].findNext('div', 'Vpfmgd').findNext('div', 'vU6FJ p63iDd').a['href']

        app_icon = results[0].findNext('div', 'Vpfmgd').findNext('div', 'uzcko').img['data-src']

        app_details = "<a href='"+app_icon+"'>ð²&#8203;</a>"

        app_details += " <b>"+app_name+"</b>"

        app_details += "\n\n<code>Developer :</code> <a href='"+app_dev_link+"'>"+app_dev+"</a>"

        app_details += "\n<code>Rating :</code> "+app_rating.replace("Rated ", "â­ ").replace(" out of ", "/").replace(" stars", "", 1).replace(" stars", "â­ ").replace("five", "5")

        app_details += "\n<code>Features :</code> <a href='"+app_link+"'>View in Play Store</a>"

        app_details += "\n\n===> @thunderuserbot <==="

        await e.edit(app_details, link_preview = True, parse_mode = 'HTML')

    except IndexError:

        await e.edit("No result found in search. Please enter **Valid app name**")

    except Exception as err:

        await e.edit("Exception Occured:- "+str(err))



@thunderbot.on(admin_cmd(pattern="appr (.*)"))

async def apkr(e):

    try:

        app_name = e.pattern_match.group(1)

        remove_space = app_name.split(' ')

        final_name = '+'.join(remove_space)

        page = requests.get("https://play.google.com/store/search?q="+final_name+"&c=apps")

        lnk = str(page.status_code)

        soup = bs4.BeautifulSoup(page.content,'lxml', from_encoding='utf-8')

        results = soup.findAll("div","ZmHEEd")

        app_name = results[0].findNext('div', 'Vpfmgd').findNext('div', 'WsMG1c nnK0zc').text

        app_dev = results[0].findNext('div', 'Vpfmgd').findNext('div', 'KoLSrc').text

        app_dev_link = "https://play.google.com"+results[0].findNext('div', 'Vpfmgd').findNext('a', 'mnKHRc')['href']

        app_rating = results[0].findNext('div', 'Vpfmgd').findNext('div', 'pf5lIe').find('div')['aria-label']

        app_link = "https://play.google.com"+results[0].findNext('div', 'Vpfmgd').findNext('div', 'vU6FJ p63iDd').a['href']

        app_icon = results[0].findNext('div', 'Vpfmgd').findNext('div', 'uzcko').img['data-src']

        app_details = "<a href='"+app_icon+"'>ð²&#8203;</a>"

        app_details += " <b>"+app_name+"</b>"

        app_details += "\n\n<code>Developer :</code> <a href='"+app_dev_link+"'>"+app_dev+"</a>"

        app_details += "\n<code>Rating :</code> "+app_rating.replace("Rated ", "â­ ").replace(" out of ", "/").replace(" stars", "", 1).replace(" stars", "â­ ").replace("five", "5")

        app_details += "\n<code>Features :</code> <a href='"+app_link+"'>View in Play Store</a>"

        app_details += "\n\n<b>Download : </b> <a href='https://t.me/thunderuserbot'>Request_Here by typing #request</a>"

        app_details += "\n\n===> @thunderuserbot <==="

        await e.edit(app_details, link_preview = True, parse_mode = 'HTML')

    except IndexError:

        await e.edit("No result found in search. Please enter **Valid app name**")

    except Exception as err:

        await e.edit("Exception Occured:- "+str(err))


CMD_HELP.update(
    {
        "app": "➟ `.app <app_name> or .appr <appname> \nUse - To fetch app details"
    }
)
