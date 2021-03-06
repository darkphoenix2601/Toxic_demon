import random

from Toxic_demon import dispatcher
from Toxic_demon.modules.disable import DisableAbleCommandHandler
from telegram import Update
from telegram.ext import CallbackContext, run_async

reactions = [
        "๐คค",
        "๐",
        "๐",
        "โ",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐ฏ",
        "๐ถ",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐ฅ",
        "๐ด",
        "๐ฆ",
        "๐ฆ",
        "๐",
        "๐",
        "๐ฉ",
        "๐",
        "๐",
        "๐",
        "๐",
        "๐ฉ",
        "๐ฅต",
        "๐",
        "๐ฃ",
        "๐ฅด",
        "๐ฟ",
        "๐ฅฐ",
        "๐ฅถ",
        "๐คก",
        "๐ป",
        "โจ",
        "๐ฅ",
        "๐ก",
        "๐ฑ",
        "๐คญ",
        "๐ฟ",
        "๐คฌ",
        "๐",
        "๐ค",
        "๐ญ",
        "โค๏ธ",
        "๐ฏ",
        "๐ฅบ",
        "๐งผ",
]


@run_async
def react(update: Update, context: CallbackContext):
    message = update.effective_message
    react = random.choice(reactions)
    if message.reply_to_message:
        message.reply_to_message.reply_text(react)
    else:
        message.reply_text(react)


REACT_HANDLER = DisableAbleCommandHandler("react", react)

dispatcher.add_handler(REACT_HANDLER)

__command_list__ = ["react"]
__handlers__ = [REACT_HANDLER]
