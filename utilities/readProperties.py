import configparser

config = configparser.RawConfigParser()
config.read("D:/Selenium/Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('common_info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common_info', 'username')
        return username

    @staticmethod
    def getPassword():
        pwd = config.get('common_info', 'password')
        return pwd
