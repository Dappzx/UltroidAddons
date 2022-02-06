from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd as dappzx

@bot.on(dappzx(pattern="bin ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    danish = event.pattern_match.group(1)
    chat = "@rkhackingbot"
    await event.edit("Searching Bin...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/bin {}".format(dappzx))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @rkhackingbot ")
              return
          if response.text.startswith(" "):
             await event.edit("That bot is dead.??")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)


@bot.on(dappzx(pattern="vbv ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    danish = event.pattern_match.group(1)
    chat = "@rkhackingbot"
    await event.edit("Checking Card...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/vbv {}".format(dappzx))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @rkhackingbot ")
              return
          if response.text.startswith(" "):
             await event.edit("That bot is dead.??")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)

@bot.on(dappzx(pattern="sk ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    danish = event.pattern_match.group(1)
    chat = "@rkhackingbot"
    await event.edit("Checking Card...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/sk {}".format(dappzx))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @rkhackingbot ")
              return
          if response.text.startswith(" "):
             await event.edit("That bot is dead.??")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)

  
@bot.on(dappzx(pattern="chk ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    danish = event.pattern_match.group(1)
    chat = "@rkhackingbot"
    await event.edit("Checking Card...")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1247032902))
              await event.client.send_message(chat, "/chk {}".format(dappzx))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @rkhackingbot ")
              return
          if response.text.startswith(" "):
             await event.edit("That bot is dead.??")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)