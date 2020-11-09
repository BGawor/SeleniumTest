from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    NEW_PLAN_BUTTON = (By.CLASS_NAME, 'md-raised.md-primary.md-button.md-ink-ripple')
    CURRENT_PLAN = (By.CLASS_NAME, 'dfp-item.zipper-animation.md-3-line.secondary-button-padding.ng-scope.md-clickable.dfp-item-selected.md-whiteframe-2dp')
    CURRENT_PLAN_BUTTON_NODE_COUNTER = (By.CLASS_NAME, 'dfp-item-takeoff.ng-binding.ng-scope') # Does not contain any text, ask dev for help
    MAIN_MAP = (By.CLASS_NAME, 'leaflet-zoom-animated')
    ROUTE = (By.CLASS_NAME, 'leaflet-clickable')