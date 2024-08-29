from selenium.webdriver.common.by import By
from .common import Common

class home(Common):

    locators = {
        'SHOP_NOW_BUTTON': (By.LINK_TEXT, 'Shop now'),
        'Shop': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(1)'),
        'ABOUT': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(2)'),
        'The_planet_and_us': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(3)'),
        'Support': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(4)'),
        'Smartphones': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(1) > div > ul > li:nth-child(1) > a'),
        'Feature_phones': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(1) > div > ul > li:nth-child(2) > a'),
        'Tablets': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(1) > div > ul > li:nth-child(3) > a'),
        'Accessories': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(1) > div > ul > li:nth-child(4) > a'),
        'Offers': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(1) > div > ul > li:nth-child(5) > a'),
        'For_business': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(1) > div > ul > li:nth-child(6) > a'),
        'Our_story': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(2) > div > ul > li:nth-child(1) > a'),
        'Newsroom': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(2) > div > ul > li:nth-child(2) > a'),
        'Brand_collaborations': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(2) > div > ul > li:nth-child(3) > a'),
        'Blog': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(2) > div > ul > li:nth-child(4) > a'),
        'Enterprise_solutions': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(2) > div > ul > li:nth-child(5) > a'),
        'Sustainability': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(3) > div > ul > li:nth-child(1) > a'),
        'Self_repair': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(3) > div > ul > li:nth-child(2) > a'),
        'Device_recycling': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(3) > div > ul > li:nth-child(3) > a'),
        'Support_center': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(4) > div > ul > li:nth-child(1) > a'),
        'FAQ': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(4) > div > ul > li:nth-child(2) > a'),
        'User_guides': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(4) > div > ul > li:nth-child(3) > a'),
        'Software_updates': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(4) > div > ul > li:nth-child(4) > a'),
        'Service_and_repairs': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(4) > div > ul > li:nth-child(5) > a'),
        'Shopping_online': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(4) > div > ul > li:nth-child(6) > a'),
        'Track_order': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > nav > details:nth-child(4) > div > ul > li:nth-child(7) > a')
    }

    def click_shop_now(self):
        self.find(self.locators['SHOP_NOW_BUTTON']).click()

    def get_shop_text(self):
        return self.find(self.locators['Shop']).text

    def get_about_text(self):
        return self.find(self.locators['ABOUT']).text

    def get_the_planet_and_us_text(self):
        return self.find(self.locators['The_planet_and_us']).text

    def get_support_text(self):
        return self.find(self.locators['Support']).text

    def click_smartphones(self):
        self.find(self.locators["Smartphones"]).click()

    def click_feature_phones(self):
        self.find(self.locators["Feature_phones"]).click()

    def click_tablets(self):
        self.find(self.locators["Tablets"]).click()

    def click_accessories(self):
        self.find(self.locators["Accessories"]).click()

    def click_Offers(self):
        self.find(self.locators["Offers"]).click()

    def click_For_business(self):
        self.find(self.locators["For_business"]).click()

    def click_Our_story(self):
        self.find(self.locators["Our_story"]).click()

    def click_Newsroom(self):
        self.find(self.locators["Newsroom"]).click()

    def click_Brand_collaborations(self):
        self.find(self.locators["Brand_collaborations"]).click()

    def click_Blog(self):
        self.find(self.locators["Blog"]).click()

    def click_Enterprise_solutions(self):
        self.find(self.locators["Enterprise_solutions"]).click()

    def click_Sustainability(self):
        self.find(self.locators["Sustainability"]).click()

    def click_Self_repair(self):
        self.find(self.locators["Self_repair"]).click()

    def click_Device_recycling(self):
        self.find(self.locators["Device_recycling"]).click()

    def click_support_center(self):
        self.find(self.locators["Support_center"]).click()

    def click_FAQ(self):
        self.find(self.locators["FAQ"]).click()

    def click_User_guides(self):
        self.find(self.locators["User_guides"]).click()

    def click_Software_updates(self):
        self.find(self.locators["Software_updates"]).click()

    def click_Service_and_repairs(self):
        self.find(self.locators["Service_and_repairs"]).click()

    def click_Shopping_online(self):
        self.find(self.locators["Shopping_online"]).click()

    def click_Track_order(self):
        self.find(self.locators["Track_order"]).click()