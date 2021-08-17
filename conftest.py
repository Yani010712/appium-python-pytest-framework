import pytest 
from os import path
from appium import webdriver

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'app-release.apk')
APPIUM = 'http://localhost:4723/wd/hub'

@pytest.fixture
def driver():
    CAPS = {
    'platformName': 'Android',
    'platformVersion': '10.0',
    'deviceName': 'Pixel 3',
    'automationName': 'UIAutomator2',
    'app': APP,
    }

   
    driver = webdriver.Remote(APPIUM, CAPS)
    yield driver
    driver.quit()

