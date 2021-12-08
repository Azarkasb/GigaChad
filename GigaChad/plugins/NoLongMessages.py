from pyrogram import Client, filters
from pyrogram.types import Message
from plugins import gigaWords, longTextLength, myCommands, myConnector
import random


# Creating respond function
@Client.on_message(filters.text & filters.group & ~ filters.bot)
def respond_to_long_messages(client: Client, message: Message):
    sql = 'SELECT state FROM chats WHERE ChatID=%s'
    val = (message.chat.id, )
    myCommands.execute(sql, val)
    myResult = myCommands.fetchone()
    if int(myResult[0]) and len(message.text) >= longTextLength:
        respond = random.choice(gigaWords['message'])
        message.reply(respond)
