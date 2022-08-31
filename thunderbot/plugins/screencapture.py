#    ThunderUserbot
#    This program is licensed under GNU Affero General Public License.(https://github.com/Thundergang/thunderuserbot/blob/master/LICENSE)
#    You cannot edit and publish it before asking owner or support team(@thunderuserbotchat on telegram), otherwise we can take any actions against you.

import io
import requests
from thunderbot import CMD_HELP, SCREEN_SHOT_LAYER_ACCESS_KEY
from thunderbot.utils import admin_cmd


@thunderbot.on(admin_cmd(pattern="screencapture (.*)"))
@thunderbot.on(sudo_cmd(pattern="screencapture (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if SCREEN_SHOT_LAYER_ACCESS_KEY is None:
        await eor(
            event,
            "Need to get an API key from https://screenshotlayer.com/product \nModule stopping!",
        )
        return
    await eor(event, "Processing ...")
    sample_url = "https://api.screenshotlayer.com/api/capture?access_key={}&url={}&fullpage={}&viewport={}&format={}&force={}"
    input_str = event.pattern_match.group(1)
    response_api = requests.get(
        sample_url.format(
            SCREEN_SHOT_LAYER_ACCESS_KEY, input_str, "1", "2560x1440", "PNG", "1"
        )
    )
    # https://stackoverflow.com/a/23718458/4723940
    contentType = response_api.headers["content-type"]
    if "image" in contentType:
        with io.BytesIO(response_api.content) as screenshot_image:
            screenshot_image.name = "screencapture.png"
            try:
                await borg.send_file(
                    event.chat_id,
                    screenshot_image,
                    caption=input_str,
                    force_document=True,
                    reply_to=event.message.reply_to_msg_id,
                )
                await event.delete()
            except Exception as e:
                await eor(event, str(e))
    else:
        await eor(event, response_api.text)


CMD_HELP.update(
    {
        "screencapture": ".screencapture <link>\nUse - Capture a screenshot of the site and send as a telegram media."
    }
)
