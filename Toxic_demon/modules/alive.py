from telethon import events, Button, custom
import re, os
from Toxic_demon.events import register
from Toxic_demon import telethn as tbot
from Toxic_demon import telethn as tgbot
PHOTO = "https://telegra.ph/file/1ebb791d3370bea387a51.jpg"
@register(pattern=("/alive"))
async def awake(event):
 Toxic_demon = event.sender.first_name
 Toxic_demon = "**β‘ I,m Toxic_demonπ** \n\n"
 Toxic_demon += "**β‘ I'm Working with awesome speed**\n\n"
 Toxic_demon += "**β‘Toxic_demon : 1.0 LATEST**\n\n"
 Toxic_demon += "**β‘ ππΊ π°πΈπ―π¦π³ :** [ππ΄π©πΆπ](t.me/akshi_S_ashu)\n\n"
 Toxic_demon += "**β‘ Telethon Version : 1.23.0**\n\n"
 BUTTON = [[Button.url("ππΆπ±π±π°π³π΅π₯", "https://t.me/phoenix_music_suport"), Button.url("ππ±π₯π’π΅π¦π΄", "https://t.me/phoenix_music_new")]]
 await tbot.send_file(event.chat_id, PHOTO, caption=Toxic_demon,  buttons=BUTTON)
