from pyrogram import Client, filters
from plugins import gigaChad, admins, myConnector, myCommands


# Say Hi and report important data from the DB
@Client.on_message(filters.user(admins) & filters.command('hi'))
def echo_hi(client, message):
    client.send_message(message.chat.id, 'Hello')
    sql = 'SELECT COUNT(*) FROM chats WHERE State = TRUE'
    myCommands.execute(sql)
    myResults = myCommands.fetchone()
    msg = f'I am active on {myResults[0]} chat(s)!'
    client.send_message(message.chat.id, msg)
