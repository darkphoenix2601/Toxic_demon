from telethon import events, Button, custom
import re, os
from Toxic_demon.events import register
from Toxic_demon import telethn as tbot
from Toxic_demon import telethn as tgbot
PHOTO = "https://telegra.ph/file/1ebb791d3370bea387a51.jpg"
@register(pattern=("/alive"))
async def awake(event):
 Toxic_demon = event.sender.first_name
 Toxic_demon = "**♡ I,m Toxic_demon💕** \n\n"
 Toxic_demon += "**♡ I'm Working with awesome speed**\n\n"
 Toxic_demon += "**♡Toxic_demon : 1.0 LATEST**\n\n"
 Toxic_demon += "**♡ 𝘔𝘺 𝘰𝘸𝘯𝘦𝘳 :** [𝘈𝘴𝘩𝘶👑](t.me/akshi_S_ashu)\n\n"
 Toxic_demon += "**♡ Telethon Version : 1.23.0**\n\n"
 BUTTON = [[Button.url("𝘚𝘶𝘱𝘱𝘰𝘳𝘵🔥", "https://t.me/phoenix_music_suport"), Button.url("𝘜𝘱𝘥𝘢𝘵𝘦𝘴", "https://t.me/phoenix_music_new")]]
 await tbot.send_file(event.chat_id, PHOTO, caption=Toxic_demon,  buttons=BUTTON)
