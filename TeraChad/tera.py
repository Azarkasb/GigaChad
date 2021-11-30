from pyrogram import Client


# Define TeraChad api bot
teraChad = Client(
    session_name='TeraChad',
    config_file='TeraChad.ini'
)


teraChad.run()
