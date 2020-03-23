import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from common_util.logger_manager import LoggerManager
from config import config_manager


class Page(object):
    def __init__(self, driver):
        self.log = LoggerManager.get_instance()
        self.driver = driver if driver != '' else webdriver.Chrome(ChromeDriverManager().install())

        self.driver.implicitly_wait(config_manager.DEFAULT_TIMEOUT)

        if not os.path.exists(config_manager.SCREENSHOTS_DIR_PATH):
            os.makedirs(config_manager.SCREENSHOTS_DIR_PATH)

        if not os.path.exists(os.path.join(config_manager.SCREENSHOTS_DIR_PATH, time.strftime("%Y%m%d"))):
            os.makedirs(os.path.join(config_manager.SCREENSHOTS_DIR_PATH, time.strftime("%Y%m%d")))

    # ======================= single element ====================== #
    def find_element(self, locator):
        element = self.driver.find_element(locator[0], locator[1])
        return element

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def get_text_from_element(self, locator):
        element = self.find_element(locator)
        return element.text

    def send_text_to_element(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def wait_page(self):
        self.driver.implicitly_wait(config_manager.DEFAULT_TIMEOUT)

    # ======================= screenshots ====================== #
    def screenshot(self, method_name):
        try:
            screenshots_name = '{now}_{name}.png'.format(now=time.strftime("%Y%m%d%H%M%S"), name=method_name)
            screenshots_path = os.path.join(config_manager.SCREENSHOTS_DIR_PATH, time.strftime("%Y%m%d"),
                                            screenshots_name)

            self.log.info("Taking screenshots: {abs_path}".format(abs_path=screenshots_path))
            self.driver.get_screenshot_as_file(screenshots_path)

        except Exception as e:
            self.log.error(e)
