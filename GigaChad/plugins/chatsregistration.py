from pyrogram import Client, filters
from plugins import apiAdmin, myConnector, myCommands


# joining a chat +join
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
        await client.send_message(apiAdmin, f'Error: {e}')


# leaving a chat +leave
@Client.on_message(filters.user(apiAdmin) & filters.command('leave', '+'))
async def leave(client: Client, message):
    try:
        target_chat_id = message.command[-1]
        await client.leave_chat(target_chat_id, delete=True)
        sql = 'DELETE FROM chats WHERE ChatID=%s'
        val = (target_chat_id, )
        myCommands.execute(sql, val)
        myConnector.commit()
        await client.send_message(apiAdmin, f'{target_chat_id} has been deleted')
    except Exception as e:
        await client.send_message(apiAdmin, f'Error: {e}')
