import pytest
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class SeleniumWiki(BasePage):

    selenium_wiki_title: tuple = (By.XPATH, "//h1/span")

    def __init__(self, driver):
        super(SeleniumWiki, self).__init__(driver)

