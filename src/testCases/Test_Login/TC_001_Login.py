import time

from src.Configure import config
from src.Page.Login_Page import LoginInPage
from src.Configure.baseSetup import setup


class Test_TC001_Login():
    username = config.UserName
    password = config.Password

    def test_login(self, psetup):
        self.driver = setup
