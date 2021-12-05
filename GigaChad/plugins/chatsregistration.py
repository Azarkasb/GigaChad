from pyrogram import Client, filters
from plugins import apiAdmin, myConnector, myCommands


# joining a chat
@Client.on_message(filters.user(apiAdmin) & filters.command('join', '+'))
async def join(client, message):
    try:
        invite_link = message.command[1]
        joined_chat = await client.join_chat(invite_link)
        sql = 'INSERT INTO chats(ChatID, Title) VALUE(%s, %s)'
        val = (joined_chat.id, joined_chat.title)
        myCommands.execute(sql, val)
        myConnector.commit()
        await client.send_message(apiAdmin, f'{joined_chat.title} has been registered!')
    except Exception as e:
        await client.send_message(apiAdmin, e)
