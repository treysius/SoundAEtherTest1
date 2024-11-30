import configparser
import os


def load_config(filename: "") -> configparser.ConfigParser:
    c = configparser.ConfigParser()
    # if config does not exist, create default config
    if not os.path.isfile(filename):
        portNum = 7894

        c['Connections'] = {'server_port': portNum}
        c['Database'] = {'db_filename': 'database.db', 'audio_dirname': 'audio'}

        # save config file
        with(open(filename, 'w')) as configFile:
            c.write(configFile)

    # if config does exist, load it
    else:
        c.read(filename)
    return c