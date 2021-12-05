from pyrogram import Client


# Define GigaChad api bot
GigaChad = Client(
    session_name='GigaChad',
    config_file='GigaChad.ini'
)


GigaChad.run()
