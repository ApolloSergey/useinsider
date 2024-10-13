from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from utils.helpers.ui_helper import UiHelper
from utils.tools.logs import log


class CareersPage(HomePage):
    CAREER_PAGE_TEXT = ".//*[contains(text(),'{}')]"
    CAREER_PAGE = (By.LINK_TEXT, "Find your dream job")
    SEE_ALL_TEAM = (By.LINK_TEXT, "See all teams")

    def is_careers_page_displayed(self):
        log.info("Verify Careers page is displayed")
        return UiHelper.wait_till_element_is_displayed(self.driver, self.CAREER_PAGE)

    def is_careers_page_section_displayed(self, section_name):
        log.info("Verify sections on Careers page")
        section_xpath = self.CAREER_PAGE_TEXT.format(section_name)
        return UiHelper.wait_till_element_is_displayed(self.driver, (By.XPATH, section_xpath))

    def select_team(self, team_name):
        see_all_teams_xpath = self.CAREER_PAGE_TEXT.format("See all teams")
        see_all_team_element = self.driver.find_element(By.XPATH, see_all_teams_xpath)
        if UiHelper.wait_till_element_clickable(self.driver, (By.XPATH, see_all_teams_xpath)):
            see_all_team_element.click()
        else:
            UiHelper.scroll_to_element(self.driver, see_all_team_element)
            see_all_team_element.click()
        team_xpath = self.CAREER_PAGE_TEXT.format(team_name)
        team_element = self.driver.find_element(By.XPATH, team_xpath)
        UiHelper.wait_till_element_is_displayed(self.driver, (By.XPATH, team_xpath))
        if UiHelper.wait_till_element_clickable(self.driver, (By.XPATH, team_xpath)):
            team_element.click()
        else:
            UiHelper.scroll_to_element(self.driver, team_element)
            team_element.click()

