import pytest
from utilities import keys
from tests.conftest import load_data
from pages.ArticleWiki import ArticleWiki
from pages.WikiHomePage import WikiHomePage
from selenium.webdriver.chrome.webdriver import WebDriver


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

        article_wiki = ArticleWiki(init_driver)

        if "Selenium" in article_wiki.get_text(article_wiki.selenium_wiki_title):
            assert article_wiki.get_text(article_wiki.selenium_wiki_title) == keys.selenium_wiki_tit
        elif "Appium" in article_wiki.get_text(article_wiki.selenium_wiki_title):
            assert article_wiki.get_text(article_wiki.selenium_wiki_title) == keys.appium_wiki_tit
        elif "Jenkins" in article_wiki.get_text(article_wiki.selenium_wiki_title):
            assert article_wiki.get_text(article_wiki.selenium_wiki_title) == keys.jenkins_wiki_tit

        article_wiki.go_back()
        assert wiki_home.get_attr(wiki_home.wiki_title) == keys.wiki_title_atr
