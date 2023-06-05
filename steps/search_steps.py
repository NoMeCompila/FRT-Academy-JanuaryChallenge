from behave import given, when, then

from pages.ArticleWiki import ArticleWiki
from utilities import utilities as ut
from selenium.webdriver.common.by import By


@given('I am on the Wikipedia home page')
def step_given_i_am_on_the_wikipedia_home_page(context):
    context.wiki_home.go_to_page(ut.WIKI_LINK)
    assert context.wiki_home.get_attr(context.wiki_home.wiki_title) == ut.WIKI_ARTICLE


@when('I search for "{element}"')
def step_when_i_search_for_element(context, element):
    context.wiki_home.clear_textbox(context.wiki_home.search_bar)
    context.wiki_home.do_send_key(context.wiki_home.search_bar, element)
    context.wiki_home.do_click(context.wiki_home.lupe_button)


@then('I should see the search results for "{element}"')
def step_then_i_should_see_search_results(context, element):
    article_wiki = ArticleWiki(context.init_driver)
    assert element in article_wiki.get_text(article_wiki.selenium_wiki_title)
