import os
import json
import pytest
from selenium import webdriver
from utilities import utilities as ut
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


# gives a json file path as a parameter and load in a python data object
def load_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
    return data


# open the configuration json file and verify that the browser corresponds to a valid value
@pytest.fixture()
def config():
    ruta_datos = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', r'..\Browsers\config.json'))

    with open(ruta_datos) as config_file:
        config = json.load(config_file)
    assert config["browser"] in [ut.FFX,
                                 ut.CHR,
                                 ut.EDG,
                                 ut.HCHR], f"Invalid browser value in configuration: {config['browser']}"
    return config


# Its depends on the configuration in json file I get one or other browser
@pytest.fixture()
def init_driver(config):
    if config["browser"] == ut.CHR:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif config["browser"] == ut.FFX:
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif config["browser"] == ut.EDG:
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif config["browser"] == ut.HCHR:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    else:
        raise Exception("Browser " + config["browser"] + " is not supported")

    driver.maximize_window()
    yield driver
    driver.quit()
