import os
import pytest
from tests.conftest import load_data
from utilities import utilities as ut
from pages.ArticleWiki import ArticleWiki
from pages.WikiHomePage import WikiHomePage
from selenium.webdriver.chrome.webdriver import WebDriver


class TestWiki:

    ruta_datos = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', r'..\data\search_data.json'))
    data = load_data(ruta_datos)

    @pytest.mark.search
    @pytest.mark.parametrize("element", data["input_search"])
    def test_search_for_element(self, init_driver: WebDriver, element: str) -> None:
        wiki_home = WikiHomePage(init_driver)
        wiki_home.go_to_page(ut.WIKI_LINK)
        assert wiki_home.get_attr(wiki_home.wiki_title) == ut.WIKI_ARTICLE
        wiki_home.clear_textbox(wiki_home.search_bar)
        wiki_home.do_send_key(wiki_home.search_bar, element)
        wiki_home.do_click(wiki_home.lupe_button)

        article_wiki = ArticleWiki(init_driver)

        if ut.SELENIUM_KEY in article_wiki.get_text(article_wiki.selenium_wiki_title):
            assert article_wiki.get_text(article_wiki.selenium_wiki_title) == ut.SELENIUM_KEY
        elif ut.APPIUM_KEY in article_wiki.get_text(article_wiki.selenium_wiki_title):
            assert article_wiki.get_text(article_wiki.selenium_wiki_title) == ut.APPIUM_KEY
        elif ut.JENKINS_KEY in article_wiki.get_text(article_wiki.selenium_wiki_title):
            assert article_wiki.get_text(article_wiki.selenium_wiki_title) == ut.JENKINS_KEY

        article_wiki.go_back()
        assert wiki_home.get_attr(wiki_home.wiki_title) == ut.WIKI_ARTICLE
