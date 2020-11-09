import unittest
from selenium import webdriver
import page
import os

class DroneFlightPlannerTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(os.path.dirname(os.path.abspath(__file__)) + '/dependencies/chromedriver.exe')
        self.driver.get("https://stupendous-birth.surge.sh/")

    def test_check_page_name(self):
        """
        Checks main page title
        """
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches()

    def test_click_create_new_plan(self):
        """
        Load the main page and check if clicking "create new plan button" enables clicking on the main map
        """
        try:
            main_page = page.MainPage(self.driver)
            main_page.click_create_new_plan()
            main_page.wait(1)
            main_page.click_main_map()
            assert True
        except:
            assert False

    def test_testcase_that_fails(self):
        assert False

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    input()
