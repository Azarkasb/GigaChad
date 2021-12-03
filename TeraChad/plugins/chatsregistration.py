from pyrogram import Client, filters
from plugins import admins, myConnector, myCommands


# Converting a python list to a readable message
# rewriting in more customizable way! later
'''def listing_information_telegram_message(ls):
    message = ''
    for item in ls:
        message += f''
'''


# Command /chats for receiving chats list
@Client.on_message(filters.user(admins) & filters.command('chats'))
def show_chats(client: Client, message):
    sql = 'SELECT * FROM chats'
    myCommands.execute(sql)
    myResults = myCommands.fetchall()
    msg = ''
    for chat in myResults:
        msg += f'`{chat[0]:<7}` | `{chat[1]:^30}` | `{bool(int(chat[2]))}`'
    client.send_message(message.chat.id, msg)


# Command /power for changing a chat status
@Client.on_message(filters.user(admins) & filters.command('power'))
def power(client, message):
    try:
        ChatID = message.text.split()[1]
        sql = 'UPDATE chats SET State = State XOR 1 WHERE ChatID = %s'
        val = (ChatID, )
        myCommands.execute(sql, val)
        myConnector.commit()
        client.send_message(message.chat.id, 'Done!')
    except Exception as e:
        client.send_message(message.chat.id, f'**Something doesn\'t work well**\n`{e}`')
