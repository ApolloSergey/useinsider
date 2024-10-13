from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.helpers.ui_helper import UiHelper
from utils.tools.logs import log


class HomePage(BasePage):

    LOGIN_LINK = (By.LINK_TEXT, "Login")
    GET_A_DEMO_LINK = (By.LINK_TEXT, "Get a Demo")
    ACTION_BUTTON_XPATH = ".//a[contains(text(),'{}')]"
    ALLOW_COOKIES = (By.XPATH, "//a[@id='wt-cli-accept-all-btn']")

    def is_homepage_displayed(self):
        log.info("Verify Home page is displayed")
        allow_cookies_element = self.driver.find_element(*self.ALLOW_COOKIES)
        if UiHelper.wait_till_element_clickable(self.driver, self.ALLOW_COOKIES):
            allow_cookies_element.click()
        return UiHelper.wait_till_element_is_displayed(self.driver, self.GET_A_DEMO_LINK)

    def navigate_on_sub_menu(self, dropdown_menu, sub_menu):
        log.info("Navigate to page with navigation menu")
        self.click_on_action_button(dropdown_menu)
        self.click_on_action_button(sub_menu)

    def click_on_action_button(self, action_button_name):
        action_xpath = self.ACTION_BUTTON_XPATH.format(action_button_name)
        action_element = self.driver.find_element(By.XPATH, action_xpath)
        if UiHelper.wait_till_element_clickable(self.driver, (By.XPATH, action_xpath)):
            action_element.click()

