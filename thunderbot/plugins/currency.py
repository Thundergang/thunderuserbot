#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

from datetime import datetime

import requests
from uniborg.util import admin_cmd

from thunderbot import CMD_HELP


@thunderbot.on(admin_cmd(pattern="currency (.*)"))
@thunderbot.on(sudo_cmd(pattern="currency (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    input_sgra = input_str.split(" ")
    if len(input_sgra) == 3:
        try:
            number = float(input_sgra[0])
            currency_from = input_sgra[1].upper()
            currency_to = input_sgra[2].upper()
            request_url = "https://api.exchangeratesapi.io/latest?base={}".format(
                currency_from
            )
            current_response = requests.get(request_url).json()
            if currency_to in current_response["rates"]:
                current_rate = float(current_response["rates"][currency_to])
                rebmun = round(number * current_rate, 2)
                await eor(
                    event,
                    "**According to current rates,**\n {} **{}** = {} **{}**\n \n▬⚡️▬⚡️▬⚡️▬⚡️▬\n\n**Current Conversion Rates:**\n 1 **{}** = {} **{}**".format(
                        number,
                        currency_from,
                        rebmun,
                        currency_to,
                        currency_from,
                        current_rate,
                        currency_to,
                    ),
                )
            else:
                await eor(
                    event,
                    "Well, This Currency isn't supported **yet**.\n__Try__ `.currencies` __for a list of supported currencies.__",
                )
        except e:
            await eor(event, str(e))
    else:
        await eor(
            event,
            "**Syntax:**\n.currency amount from to\n**Example:**\n`.currency 10 usd inr`",
        )
    end = datetime.now()
    (end - start).seconds


@thunderbot.on(admin_cmd(pattern="currencies (.*)"))
async def list(ups):
    if ups.fwd_from:
        return
    request_url = "https://api.exchangeratesapi.io/latest?base=USD"
    current_response = requests.get(request_url).json()
    tell_me_the_rate_baby = current_response["rates"]
    for key, value in tell_me_the_rate_baby.items():
        await borg.send_message(
            ups.chat_id,
            "**List of currencies:**\n {}\n*Tip:** Use `.gs` currency_code for more details on the currency.".format(
                key
            ),
        )


CMD_HELP.update(
    {
        "currency": ".currency <value> <from> <to>\nUse - To convert currency."
    }
)
