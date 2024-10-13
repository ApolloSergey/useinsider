import pytest


@pytest.mark.usefixtures("base_use_insider_setup")
class BaseTest:
    def __init__(self, driver):
        self.driver = driver
