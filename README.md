# GigaChad
Giga Chad Official Telegram Account!

> This repository blongs to a meme bot called giga chad

## Requirements 
- python
- A [Telegram API key](//docs.pyrogram.org/intro/setup#api-keys)
- A [Telegram bot token](//t.me/botfather)

## Config files
this bot uses config files to receive variables
> You need two config files in these formats
1. `giga.ini`
  ```ini
  [pyrogram]
  api_id = your_api_id
  api_hash = your_api_hash

  [plugins]
  root = plugins

  [mysql]
  hostname = your_hostname
  username = your_username
  password = your_password
  database = gigachad

  [apiadmin]
  ;TeraChad
  api_admin = your bot username

  [gigachad]
  longTextLength = 150
   ```
2. `tera.ini`
```ini
[pyrogram]
api_id = your_api_id
api_hash = your_api_hash
bot_token = your_bot_token

[plugins]
root = plugins

[mysql]
hostname = your_hostname
username = your_username
password = your_password
database = gigachad

[admins]
; admin1
admin = admin1_ID
; admin2
admin1 = admin2_ID
; admin3
admin3 = admin3_ID

[gigachad]
ID = your_client_id
```

## Run

1. `git clone https://github.com/Azarkasb/GigaChad.git` to download the source code.
2. `cd GigaChad`, to enter the directory.
3. `python -m venv venv && . venv/bin/activate` to create and activate a virtual environment.
4. `pip install -U -r requirements.txt`, to install the requirements.
5. create `giga.ini`,`tera.ini` in GigaChad and TeraChad directory
6. Run `giga.py` and `tera.py` in two different cmd
7. enjoy

## License

MIT © 2021-present [Azarkasb](//github.com/Azarkasb)
