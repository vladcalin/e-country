import configparser


class Config(object):
    def __init__(self, conf_file):
        self.conf_file = conf_file
        self.data = configparser.ConfigParser()
        with open(conf_file, 'r') as f:
            self.data.read_file(f)

    def get(self, section, name):
        return self.data.get(section, name)
