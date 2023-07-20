from seleniumpagefactory.Pagefactory import PageFactory


class DashboardPage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        'User_module': ('LINK_TEXT', "Users"),
        'Reconciliation_Queue_module': ('LINK_TEXT', "Reconciliation Queue"),
    }

    def click_report_module(self):
        self.User_module.click()

    def click_reconciliation_queue_module(self):
        self.Reconciliation_Queue_module.click()
