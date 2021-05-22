"""
✘ Commands Available

• `{i}joke`
    To get joke.

• `{i}insult`
    Insult someone..

• `{i}url <long url>`
    To get a shorten link of long link.

• `{i}decide`
    Decide something.

• `{i}gif <your query>`
    Sends the desired gif related to your query.

• `{i}xo`
    Opens tic tac game only where using inline mode is allowed.

• `{i}wordi`
    Opens word game only where using inline mode is allowed.

• `{i}gps <name of place>`
    Shows the desired place in the map.

"""

import random

import requests
from bs4 import BeautifulSoup as bs
from pyjokes import get_joke
from telethon.errors import ChatSendMediaForbiddenError

from . import *


@ultroid_cmd(pattern="joke$")
async def _(ult):
    await eor(ult, get_joke())


@ultroid_cmd(pattern="insult$")
async def gtruth(ult):
    m = await eor(ult, "Generating...")
    nl = "https://fungenerators.com/random/insult/new-age-insult/"
    ct = requests.get(nl).content
    bsc = bs(ct, "html.parser", from_encoding="utf-8")
    cm = bsc.find_all("h2")[0].text
    await m.edit(f"{cm}")


@ultroid_cmd(pattern="url ?(.*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    if not input_str:
        await eor(event, "Give some url")
        return
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await eor(
            event,
            "Shortened url==> {} for the given url==> {}.".format(
                response_api, input_str
            ),
        )
    else:
        await eor(event, "`Something went wrong. Please try again Later.`")


@ultroid_cmd(pattern="decide$")
async def _(event):
    hm = await eor(event, "`Deciding`")
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
    r = requests.get("https://yesno.wtf/api").json()
    try:
        await ultroid_bot.send_message(
            event.chat_id, r["answer"], reply_to=message_id, file=r["image"]
        )
        await hm.delete()
    except ChatSendMediaForbiddenError:
        await eor(event, r["answer"])


@ultroid_cmd(pattern="xo$")
async def xo(ult):
    if BOT_MODE:
        return await eor(ult, "You cant use this command in BOT MODE.")
    xox = await ultroid_bot.inline_query("xobot", "play")
    await xox[random.randrange(0, len(xox) - 1)].click(
        ult.chat.id, reply_to=ult.reply_to_msg_id, silent=True, hide_via=True
    )
    await ult.delete()


@ultroid_cmd(pattern="wordi$")
async def word(ult):
    if BOT_MODE:
        return await eor(ult, "You cant use this Command in BOT MODE.")
    game = await ultroid_bot.inline_query("wordibot", "play")
    await game[0].click(
        ult.chat.id, reply_to=ult.reply_to_msg_id, silent=True, hide_via=True
    )
    await ult.delete()


@ultroid_cmd(pattern="gps (.*)")
async def map(ult):
    if BOT_MODE:
        return await eor(ult, "You cant use this Command in BOT MODE.")
    get = ult.pattern_match.group(1)
    if not get:
        return await eor(ult, "Use this command as `.gps <query>`")
    gps = await ultroid_bot.inline_query("openmap_bot", f"{get}")
    await gps[0].click(
        ult.chat.id, reply_to=ult.reply_to_msg_id, silent=True, hide_via=True
    )
    await ult.delete()


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
