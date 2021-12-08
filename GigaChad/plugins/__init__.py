from configparser import ConfigParser
import mysql.connector

# Parse GigaChad.ini Config_file to DBdata and api_admin
config = ConfigParser()
config.read('GigaChad.ini')
DBdata = {
    'hostname': config['mysql']['hostname'],
    'username': config['mysql']['username'],
    'password': config['mysql']['password'],
    'database': config['mysql']['database']
}
admins = []
apiAdmin = config['apiadmin']['api_admin']
longTextLength = int(config['gigachad']['longTextLength'])

# Connecting to DB
myConnector = mysql.connector.connect(
    host=DBdata['hostname'],
    user=DBdata['username'],
    password=DBdata['password'],
    database=DBdata['database']
)
myCommands = myConnector.cursor()

# Defining Giga Words
gigaWords = {'message': [
    'نخوندم',
    'نشنیدم',
    'ندیدم',
    'نفهمیدم',
    'نیستم',
    'نگرفتم',
]}
