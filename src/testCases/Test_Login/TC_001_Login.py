import time
from selenium import webdriver
from src.Configure import config
from src.Configure.baseSetup import setup
from src.Configure.readPropertices import conf
from src.Page.Login_Page import LoginInPage


class Test_login_page:
    username = config.UserName
    password = config.Password

    def test_login(self, setup):
        self.driver = setup
        self.lp = LoginInPage(self.driver)
        self.lp.select_username(self.username)
        self.lp.select_password(self.password)
        self.lp.click_login()
        self.driver.quit()
        return setup
