from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # get an URL in string format and goes there
    def go_to_page(self, url: str) -> None:
        self.driver.get(url)

    # waits for an element then clicks it
    def do_click(self, by_locator: tuple) -> None:
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    # writes some text given as a parameter in a textbox
    def do_send_key(self, by_locator: tuple, txt: str) -> None:
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(txt)

    # clear the text from a textbox
    def clear_textbox(self, by_locator: tuple) -> None:
        self.wait.until(EC.visibility_of_element_located(by_locator)).clear()

    # waits for an element and returns its text
    def get_text(self, by_locator: tuple) -> str:
        return self.wait.until(EC.visibility_of_element_located(by_locator)).text

    # returns the attribute of the element in by_locator
    def get_attr(self, by_locator: tuple) -> str:
        return self.wait.until(EC.visibility_of_element_located(by_locator)).get_attribute("class")

    # go back to the previous page
    def go_back(self):
        self.driver.back()
