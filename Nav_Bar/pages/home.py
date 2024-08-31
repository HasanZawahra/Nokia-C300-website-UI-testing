from selenium.webdriver.common.by import By
from .common import Common

class home(Common):

    locators = {
        'SHOP_NOW_BUTTON': (By.LINK_TEXT, 'Shop now'),
        'PHONE_NAME': (By.CSS_SELECTOR, '#sticky-bar-header > div.css-1fiiow1.ebj1o0l2 > h5'),
        'PRICE': (By.CSS_SELECTOR, '#sticky-bar-header > div.css-k8k3wj.ez0fsog4 > div.css-v2wgeq.ez0fsog2 > div > div'),
        'Learn_more': (By.LINK_TEXT, 'Learn more'),
        'Specs': (By.LINK_TEXT, 'Specs'),
        'Where_to_buy_button': (By.CSS_SELECTOR, '#sticky-bar-header > div.css-k8k3wj.ez0fsog4 > div.css-vk66me.ez0fsog3 > a'),
        'NAV': (By.ID, "sticky-bar-header")
    }

    def check_clicked_where_to_buy(self):
        nav_element = self.find(self.locators['NAV'])
        classes = nav_element.get_attribute("class")
        return "on-top" in classes

