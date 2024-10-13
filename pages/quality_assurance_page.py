import time
from utils.tools.logs import log
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from utils.helpers.ui_helper import UiHelper
from selenium.webdriver.common.action_chains import ActionChains


class QualityAssurancePage(HomePage):

    SEE_ALL_JOBS_BUTTON = (By.LINK_TEXT, "See all QA jobs")
    APPLY_FOR_JOB_BUTTON = (By.XPATH, "//a[contains(text(),'Apply for this job')]")
    VIEW_ROLE_BUTTON = (By.XPATH, "//a[contains(text(),'View Role')]")
    JOB_LIST = (By.CSS_SELECTOR, ".position-list-item-wrapper")
    VIEW_BUTTON = (By.CSS_SELECTOR, ".btn-navy")
    LOCATION_FILTER = (By.XPATH, "//span[contains(@aria-labelledby, 'location') and @role='combobox']")
    DEPARTMENT_FILTER = (By.XPATH, "//span[contains(@aria-labelledby, 'department') and @role='combobox']")
    JOB_COUNT_DISPLAY = (By.XPATH, "//p[@id='resultCounter' and contains(text(),'Showing')]")
    OPTION_XPATH = "//li[text()='{}']"

    def is_quality_assurance_page_displayed(self):
        log.info("Verify Quality Assurance page is displayed")
        return UiHelper.wait_till_element_is_displayed(self.driver, self.SEE_ALL_JOBS_BUTTON)

    def find_jobs(self, location, department):
        log.info("Find job with Location and Department on Quality Assurance page")
        self.driver.find_element(*self.SEE_ALL_JOBS_BUTTON).click()
        self.wait_for_job_position_table_load()
        UiHelper.wait_till_element_clickable(self.driver, self.LOCATION_FILTER)
        location_filter = self.driver.find_element(*self.LOCATION_FILTER)
        location_filter.click()
        self.wait_for_job_position_table_load()
        location_filter.find_element(By.XPATH, self.OPTION_XPATH.format(location)).click()
        department_filter = self.driver.find_element(*self.DEPARTMENT_FILTER)
        department_filter.click()
        department_filter.find_element(By.XPATH, self.OPTION_XPATH.format(department)).click()
        self.wait_for_job_position_table_load()

    def wait_for_job_position_table_load(self):
        UiHelper.wait_till_element_appears(self.driver, self.JOB_LIST, timeout=10)
        UiHelper.wait_till_element_appears(self.driver, self.JOB_COUNT_DISPLAY, timeout=10)
        time.sleep(5)  # Unstable working of job result list

    def are_job_positions_displayed(self):
        log.info("Verify that the job position is displayed on Quality Assurance page")
        job_position_list_items = UiHelper.wait_till_all_elements_located(self.driver, self.JOB_LIST)
        return len(job_position_list_items) > 0

    def are_location_and_department_displayed(self, location, department):
        log.info("Verify that Location and Departament are displayed with correct values")
        self.wait_for_job_position_table_load()
        job_position_list_items = UiHelper.wait_till_all_elements_located(self.driver, self.JOB_LIST, timeout=10)
        status = []
        for i in job_position_list_items:
            position_location = i.find_element(By.CLASS_NAME, "position-location").text
            position_department = i.find_element(By.CLASS_NAME, "position-department").text
            if position_location == location and position_department == department:
                status.append(True)
            else:
                status.append(False)
        return all(status)

    def click_view_role_option(self):
        log.info("Open job description")
        UiHelper.wait_till_element_appears(self.driver, self.JOB_LIST, timeout=10)
        job_position_list_items = UiHelper.wait_till_all_elements_located(self.driver, self.JOB_LIST)
        first_job_position = job_position_list_items[0]
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", first_job_position)
        actions = ActionChains(self.driver)
        actions.pause(2).move_to_element(first_job_position).pause(2).perform()
        UiHelper.wait_till_element_clickable(self.driver, self.VIEW_ROLE_BUTTON)
        first_job_position.find_element(*self.VIEW_ROLE_BUTTON).click()

    def is_lever_co_page_displayed(self):
        log.info("Verify that job description opened in new window")
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])
        return UiHelper.wait_till_element_is_displayed(self.driver, self.APPLY_FOR_JOB_BUTTON, timeout=10)



