import random
import string
import time

from src.Configure.readPropertices import conf
from src.Page.UserManagePage import UserManagementPage
from src.Page.Login_Page import LoginInPage
from src.testCases.Test_Login.TC_001_Login import Test_login_page
from src.Configure.baseSetup import setup


class Test_User_Manage:
    user_name = conf.getUsername()
    passwd = conf.getPassword()
    fullname = "MD Alimun Hasan"
    # usrName = "alimun1193"
    # usrname = random.randint(alimun , 10001)
    role = "ROLE_SUPER_ADMIN"
    usrStatus = "0"
    usrType = "0"
    userPass = "Brac@1234."
    num = random.randint(1001, 10010)
    userPin = "11234"
    department = "BBLSQA"

    letters = string.ascii_lowercase
    usrName = ''.join((random.choice('alimun2234t') for i in range(3)))

    def test_user_page_reset(self, setup):
        self.driver = setup
        time.sleep(1)
        login = LoginInPage(self.driver)
        login.login_in_page()

