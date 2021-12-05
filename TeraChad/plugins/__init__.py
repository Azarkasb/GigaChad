from configparser import ConfigParser
import mysql.connector


# Parse Terachad.ini Config_file to DBdata and AdminID's list
config = ConfigParser()
config.read('TeraChad.ini')
DBdata = {
    'hostname': config['mysql']['hostname'],
    'username': config['mysql']['username'],
    'password': config['mysql']['password'],
    'database': config['mysql']['database']
}
admins = []
for admin in config['admins']:
    admins.append(int(config['admins'][admin]))

# Recognizing our gigaChad cli account
gigaChad = int(config['gigachad']['ID'])

# Connecting to DB
myConnector = mysql.connector.connect(
    host=DBdata['hostname'],
    user=DBdata['username'],
    password=DBdata['password'],
    database=DBdata['database']
)
myCommands = myConnector.cursor()

# GigaChad response to TeraChad Handler
response = {'currentAdmin': 'noBody', 'join': 0, 'leave': 0}
