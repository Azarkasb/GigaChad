from pyrogram import Client, filters
from pyrogram.types import Message
from plugins import gigaChad, admins, myConnector, myCommands, response


# Command /chats for receiving chats list
@Client.on_message(filters.user(admins) & filters.command('chats'))
def show(client: Client, message):
    myConnector.commit()
    sql = 'SELECT * FROM chats'
    myCommands.execute(sql)
    myResults = myCommands.fetchall()
    msg = ''
    for chat in myResults:
        msg += f'`{chat[0]:<20} | {chat[1]:^30} | {bool(int(chat[2]))}`\n'
    client.send_message(message.chat.id, msg)


# Command /power for changing a chat status
@Client.on_message(filters.user(admins) & filters.command('power'))
async def power(client, message):
    try:
        ChatID = message.text.split()[1]
        sql = 'UPDATE chats SET State = State XOR 1 WHERE ChatID = %s'
        val = (ChatID, )
        myCommands.execute(sql, val)
        myConnector.commit()
        await client.send_message(message.chat.id, 'Done!')
    except Exception as e:
        await client.send_message(message.chat.id, f'**Something doesn\'t work well**\n`{e}`')


# Command /join for joining a chat
@Client.on_message((filters.user(admins) & filters.command('join')))
async def join(client, message):
    invite_link = message.command[1]
    invite_link = invite_link.replace('+', 'joinchat/')
    if 'joinchat' not in invite_link:
        invite_link = invite_link.split('/')[-1]
    await client.send_message(gigaChad, f'+join {invite_link}', disable_web_page_preview=True)
    response['join'] = 1
    response['currentAdmin'] = message.chat.id


# Getting response of +join from gigachad
async def response_join(client: Client, message):
    await client.send_message(response['currentAdmin'], message.text)


# Command /leave for leaving a chat
@Client.on_message(filters.user(admins) & filters.command('leave'))
async def leave(client, message):
    target_chat_id = message.command[-1]
    await client.send_message(gigaChad, f'+leave {target_chat_id}')
    response['leave'] = 1
    response['currentAdmin'] = message.chat.id


# Getting response of +leave from gigachad
async def response_leave(client: Client, message: Message):
    await client.send_message(response['currentAdmin'], message.text)


# Handling gigaChad responses!
@Client.on_message(filters.user(gigaChad))
async def handling_gigachad_response(client, message):
    if response['join']:
        await response_join(client, message)
        response['join'] = 0
    elif response['leave']:
        await response_leave(client, message)
        response['leave'] = 0
