from pages.BasePage import BasePage
from utilities import utilities as ut
from selenium.webdriver.common.by import By

class WikiHomePage(BasePage):

    search_bar: tuple = (By.ID, ut.SEARCH_BAR)
    lupe_button: tuple = (By.XPATH, ut.SUBMIT_BTN)
    wiki_title: tuple = (By.TAG_NAME, ut.WIKIPEDIA)

    def __init__(self, driver):
        super(WikiHomePage, self).__init__(driver)
