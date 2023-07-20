import random

from seleniumpagefactory.Pagefactory import PageFactory

from seleniumpagefactory.Pagefactory import PageFactory


class UserManagementPage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'User_Mg_module': ('LINK_TEXT', "User Management"),
        'Add_user_btn': ('CSS', "a[color='info'] button[type='button']"),
        'Full_Name': ('Id', "name"),
        'add_Username': ('Id', "username"),
        'select_role': ('Id', "roleId"),
        'Ucheck_hasEmail': ('Id', "hasEmail"),
        ##'select_usrType': ('Id', "addUserType"),
        'entry_pass': ('Id', "addPassword"),
        'entry_pin': ('Id', "pin"),
        'entry_dept': ('Id', "department"),
        'click_user_list_btn': ('CSS', "a[color='success'] button[type='button']"),
        'click_adduser': ('CSS', "button[type='submit']")

    }

    def click_adduser_btn(self):
        self.Add_user_btn.click()

    def entry_fullname(self, fullname):
        self.Full_Name.set_text(fullname)

    def entry_user_pin(self, upin):
        self.add_Username.set_text(upin)

    def entry_department(self, depart):
        self.entry_dept.set_text(depart)

    def entry_username(self, uname):
        self.add_Username.set_text(uname)

    def select_role_name(self, role):
        self.select_role.select_element_by_value(role)

    def uncheck_email(self):
        self.Ucheck_hasEmail.click()

    def entry_user_password(self, userpass):
        self.entry_pass.set_text(userpass)

    def click_user_list_button(self):
        self.click_user_list_btn.click()

    def click_button_adduser(self):
        self.click_adduser.click()
