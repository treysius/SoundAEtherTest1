import configparser
import os


def load_config(filename: "") -> configparser.ConfigParser:
    c = configparser.ConfigParser()
    # if config does not exist, create default config
    if not os.path.isfile(filename):
        portNum = input("Enter the port number to listen on (this will be stored in the "+filename+" file) ")

        c['Connections'] = {'server_port': portNum}
        c['Database'] = {'db_filename': 'database.db'}

        # save config file
        with(open(filename, 'w')) as configFile:
            c.write(configFile)

    # if config does exist, load it
    else:
        c.read("config.ini")