from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

import os
from datetime import datetime

from selenium.common.exceptions import (NoSuchElementException,
                                        StaleElementReferenceException,
                                        TimeoutException)
from project_constants import project_path


class UiHelper(object):
    """
    All actions from selenium that are common.
    """

    @staticmethod
    def wait_till_element_clickable(driver, locator, timeout=5):
        wait = WebDriverWait(driver, timeout=int(timeout),
                             ignored_exceptions=(StaleElementReferenceException, TimeoutException))
        try:
            UiHelper.wait_till_element_is_displayed(driver, locator, timeout=int(timeout))
            wait.until(ec.element_to_be_clickable(locator))
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    @staticmethod
    def wait_till_element_is_displayed(driver, locator, timeout=5):
        """
        :return: True if element IS displayed
        """
        wait = WebDriverWait(driver, timeout=int(timeout),
                             ignored_exceptions=(StaleElementReferenceException, NoSuchElementException))
        try:
            wait.until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @staticmethod
    def scroll_to_element(driver, web_element):
        """
        Scroll to the exact element
        :param web_element: web element (e.g. driver.find_element_by_xpath("//div")
        :param driver: webdriver
        """
        driver.execute_script("return arguments[0].scrollIntoView(true);", web_element)

    @staticmethod
    def create_screen_shot(driver, test_name):
        current_date = "_" + (datetime.now().strftime("%Y_%m_%d_%H-%M"))
        save_path = os.path.join(project_path, "screenshots")

        # Create directory for storing screenshots if not exists
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        driver.save_screenshot(os.path.join(save_path, test_name + current_date + ".png"))

    @staticmethod
    def wait_till_element_text_is_displayed(driver, locator, text, timeout=5):
        """
        :return: True if element text IS displayed
        """
        wait = WebDriverWait(driver, timeout=int(timeout),
                             ignored_exceptions=(StaleElementReferenceException, NoSuchElementException))
        try:
            wait.until(ec.text_to_be_present_in_element(locator, text))
            return True
        except TimeoutException:
            return False

    @staticmethod
    def wait_till_all_elements_located(driver, locator, timeout=10):
        """
        :return: True if elements located
        """
        wait = WebDriverWait(driver, timeout=int(timeout),
                             ignored_exceptions=(StaleElementReferenceException, NoSuchElementException))
        try:
            return wait.until(ec.presence_of_all_elements_located(locator))
        except TimeoutException:
            return False

    @staticmethod
    def wait_till_element_disappear(driver, element, timeout=5):
        wait = WebDriverWait(driver, timeout=timeout,
                             ignored_exceptions=(StaleElementReferenceException,
                                                 NoSuchElementException,
                                                 TimeoutException))
        try:
            return wait.until_not(ec.presence_of_element_located(element))
        except (NoSuchElementException, TimeoutException):
            return False

    @staticmethod
    def wait_till_element_appears(driver, element, timeout=10):
        wait = WebDriverWait(driver, timeout=timeout,
                             ignored_exceptions=(StaleElementReferenceException,
                                                 NoSuchElementException,
                                                 TimeoutException))
        try:
            wait.until(ec.presence_of_element_located(element))
            return True
        except TimeoutException:
            return False
