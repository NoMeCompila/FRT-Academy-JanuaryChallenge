import time

from selenium.webdriver.chrome.webdriver import WebDriver
import pytest

from pages.SeleniumWiki import SeleniumWiki
from pages.WikiHomePage import WikiHomePage
from utilities import keys
from tests.conftest import load_data


class TestWiki:

    data = load_data(r"C:\Users\fernando.caballero\Desktop\FreeRangeTestersAcademy\January Challenge\data\search_data.json")

    @pytest.mark.search
    @pytest.mark.parametrize("element", data["input_search"])
    def test_search_for_element(self, init_driver: WebDriver, element: str) -> None:
        wiki_home = WikiHomePage(init_driver)
        wiki_home.go_to_page(keys.wiki_url)
        assert wiki_home.get_attr(wiki_home.wiki_title) == keys.wiki_title_atr
        wiki_home.clear_textbox(wiki_home.search_bar)
        wiki_home.do_send_key(wiki_home.search_bar, element)
        wiki_home.do_click(wiki_home.lupe_button)

        selenium_wiki = SeleniumWiki(init_driver)
        assert selenium_wiki.get_text(selenium_wiki.selenium_wiki_title) == keys.selenium_wiki_tit

        selenium_wiki.go_back()
        assert wiki_home.get_attr(wiki_home.wiki_title) == keys.wiki_title_atr

