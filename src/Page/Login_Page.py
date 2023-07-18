from seleniumpagefactory import PageFactory


class LoginInPage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'user_name': ('CSS', "input[placeholder='Enter User ID']"),
        'password': ('CSS', "#password"),
        'login_btn': ('CSS', "button[type='submit']")
    }

    def select_username(self, user):
        self.user_name.set_text(user)

    def select_password(self, password):
        self.password.set_text(password)

    def click_login(self):
        self.login_btn.click()
