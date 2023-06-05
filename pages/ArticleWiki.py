from pages.BasePage import BasePage
from utilities import utilities as ut
from selenium.webdriver.common.by import By

class ArticleWiki(BasePage):

    selenium_wiki_title: tuple = (By.XPATH, ut.WIKI_TITLE)

    def __init__(self, driver):
        super(ArticleWiki, self).__init__(driver)
