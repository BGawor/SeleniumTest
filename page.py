from element import BasePageElement
from locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CurrentPlan(BasePageElement):
    # The locator for current plan element
    locator = MainPageLocators.CURRENT_PLAN

class CurrentPlanNodeCounter(BasePageElement):
    # The locator for current plan element
    locator = MainPageLocators.CURRENT_PLAN_BUTTON_NODE_COUNTER

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here."""

    # Define elements on the page
    current_plan = CurrentPlan()
    current_plan_node_counter = CurrentPlanNodeCounter()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Mission: Drone Flight Planner" in self.driver.title

    def click_create_new_plan(self):
        """Triggers the button"""
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.NEW_PLAN_BUTTON)
        )
        element.click()

    def click_main_map(self):
        """Triggers the button"""
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.MAIN_MAP)
        )
        element.click()

    def get_current_plan(self):
        """Returns currently active flight plan"""
        return self.current_plan

    def is_result_found(self, text):
        """Searches for text in current page source"""
        return str(text) in self.driver.page_source

    def wait(self, seconds):
        """Waits for {seconds} seconds"""
        self.driver.implicitly_wait(seconds)
