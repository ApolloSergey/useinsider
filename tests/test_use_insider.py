import pytest
from pages.careers_page import CareersPage
from pages.home_page import HomePage
from pages.quality_assurance_page import QualityAssurancePage
from utils.tools.verify import Verify


class TestUseInsider:
    """
    Perform test for UseInsider
    """

    @pytest.mark.usefixtures("base_driver_setup")
    def test_use_insider(self):
        home_page = HomePage(self.driver)
        careers_page = CareersPage(self.driver)
        qa_page = QualityAssurancePage(self.driver)
        Verify.true(home_page.is_homepage_displayed(), "Home Page is missing")
        careers_page.navigate_on_sub_menu("Company", "Careers")
        Verify.true(careers_page.is_careers_page_displayed(), "Careers Page is missing")

        Verify.true(careers_page.is_careers_page_section_displayed("Find your calling"),
                    "Find your calling section is missing")
        Verify.true(careers_page.is_careers_page_section_displayed("Our Locations"),
                    "Our Locations section is missing")
        Verify.true(careers_page.is_careers_page_section_displayed("Life at Insider"),
                    "Life at Insider section is missing")
        self.driver.get("https://useinsider.com/careers/quality-assurance/")
        Verify.true(qa_page.is_quality_assurance_page_displayed(), "Careers Page is missing")
        qa_page.find_jobs("Istanbul, Turkey", "Quality Assurance")
        Verify.true(qa_page.are_job_positions_displayed(), "List of positions is empty")
        Verify.true(qa_page.are_location_and_department_displayed("Istanbul, Turkey",
                                                                  "Quality Assurance"),
                    "Job positions are missing")

        qa_page.click_view_role_option()

        Verify.true(qa_page.is_lever_co_page_displayed(), "Lever co page is missing")






