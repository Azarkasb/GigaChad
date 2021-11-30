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

# Connecting to DB
myConnector = mysql.connector.connect(
    host=DBdata['hostname'],
    user=DBdata['username'],
    password=DBdata['password'],
    database=DBdata['database']
)
myCommands = myConnector.cursor()
