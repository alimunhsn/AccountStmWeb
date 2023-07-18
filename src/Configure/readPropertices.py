from src.Configure import config


class conf:
    @staticmethod
    def getApplicationURl():
        Url = config.BaseUrl  # cfg.get('common', 'BaseUrl')
        return Url

    @staticmethod
    def getUsername():
        username = config.UserName  # cfg.get("common", "UserName")
        return username

    @staticmethod
    def getPassword():
        passwd = config.Password  # cfg.get("common", "Password")
        return passwd
