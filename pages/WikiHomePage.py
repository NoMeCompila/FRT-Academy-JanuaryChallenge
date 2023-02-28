from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class WikiHomePage(BasePage):

    search_bar: tuple = (By.ID, "searchInput")
    lupe_button: tuple = (By.XPATH, "//button[@type='submit']")
    wiki_title: tuple = (By.TAG_NAME, "h1")

    def __init__(self, driver):
        super(WikiHomePage, self).__init__(driver)
