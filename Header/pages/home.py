from selenium.webdriver.common.by import By
from .common import Common

class home(Common):

    locators = {
        'SHOP_NOW_BUTTON': (By.LINK_TEXT, 'Shop now'),
        'Smartphones': (By.CSS_SELECTOR, '#navigation-bar > div.css-3hh206.e7yl3vc0 > div.css-cv0vg5.e7yl3vc7 > ul > li:nth-child(1) > a'),
        'Feature_phones': (By.CSS_SELECTOR, '#navigation-bar > div.css-3hh206.e7yl3vc0 > div.css-cv0vg5.e7yl3vc7 > ul > li:nth-child(2) > a'),
        'Tablets': (By.CSS_SELECTOR, '#navigation-bar > div.css-3hh206.e7yl3vc0 > div.css-cv0vg5.e7yl3vc7 > ul > li:nth-child(3) > a'),
        'Accessories': (By.CSS_SELECTOR, '#navigation-bar > div.css-3hh206.e7yl3vc0 > div.css-cv0vg5.e7yl3vc7 > ul > li:nth-child(4) > a'),
        'HMD_Skyline': (By.CSS_SELECTOR, '#navigation-bar > div.css-3hh206.e7yl3vc0 > div.css-cv0vg5.e7yl3vc7 > ul > li:nth-child(5) > a'),
        'Offers': (By.CSS_SELECTOR, '#navigation-bar > div.css-3hh206.e7yl3vc0 > div.css-cv0vg5.e7yl3vc7 > ul > li:nth-child(6) > a'),
        'For_business': (By.CSS_SELECTOR, '#navigation-bar > div.css-3hh206.e7yl3vc0 > div.css-cv0vg5.e7yl3vc7 > ul > li:nth-child(7) > a'),
        'HMD_logo': (By.CSS_SELECTOR, '#navigation-bar > div.css-3hh206.e7yl3vc0 > div.css-cm8qpz.e7yl3vc9 > a > svg'),
        'MENU_ICON': (By.CSS_SELECTOR, '#navigation-bar > div.css-1s6mtog.e7yl3vc4 > button.action.e7yl3vc2.css-2n2z2m.e1af6ugw0 > span > svg'),
        'CART_ICON': (By.CSS_SELECTOR, '#navigation-bar > div.css-1s6mtog.e7yl3vc4 > a > span > svg'),
        'ACCOUNT_ICON': (By.CSS_SELECTOR,'#navigation-bar > div.css-1s6mtog.e7yl3vc4 > button.e7yl3vc3.css-2n2z2m.e1af6ugw0 > span > svg'),
        'My_account_BUTTON': (By.CSS_SELECTOR, '#header > dialog > div > div > div.col.css-1r0x3gs.eo76sqx1.col-xxs-12.col-lg-5 > div > button > span'),
        'COVERED_BODY': (By.CSS_SELECTOR, '#header > dialog'),
        'Account_tab_HMD_LOGO': (By.CSS_SELECTOR, '#header > dialog > div.css-1xsf3cw.e1l465e24 > div > div.col.css-1sn8j64.e1l465e29.col-xxs-12.col-lg-5 > a > svg > use')

    }

    menu_locators = {
        'Smartphones': (By.CSS_SELECTOR,'#navigation-main-menu-drawer > ul > li:nth-child(1) > a'),
        'Feature_phones': (By.CSS_SELECTOR,'#navigation-main-menu-drawer > ul > li:nth-child(2) > a'),
        'Tablets': (By.CSS_SELECTOR,'#navigation-main-menu-drawer > ul > li:nth-child(3) > a'),
        'Accessories': (By.CSS_SELECTOR,'#navigation-main-menu-drawer > ul > li:nth-child(4) > a'),
        'HMD_Skyline': (By.CSS_SELECTOR,'#navigation-main-menu-drawer > ul > li:nth-child(5) > a'),
        'Offers': (By.CSS_SELECTOR,'#navigation-main-menu-drawer > ul > li:nth-child(6) > a'),
        'For_business': (By.CSS_SELECTOR,'#navigation-main-menu-drawer > ul > li:nth-child(7) > a'),
        'HMD_logo': (By.CSS_SELECTOR, '#header > dialog > div > div > div.col.css-h7n3fv.eo76sqx2.col-xxs-12.col-lg-7 > a > svg > use'),
    }

    def check_menu_tab_cover(self):
        dialog_element = self.find(self.locators["COVERED_BODY"])
        is_open = dialog_element.get_attribute("open") is not None
        return is_open

    def click_smartphones(self):
        if self.check_menu_tab_cover():
            self.find(self.menu_locators["Smartphones"]).click()
        else:
            self.find(self.locators["Smartphones"]).click()

    def click_feature_phones(self):
        if self.check_menu_tab_cover():
            self.find(self.menu_locators["Feature_phones"]).click()
        else:
            self.find(self.locators["Feature_phones"]).click()

    def click_tablets(self):
        if self.check_menu_tab_cover():
            self.find(self.menu_locators["Tablets"]).click()
        else:
            self.find(self.locators["Tablets"]).click()

    def click_accessories(self):
        if self.check_menu_tab_cover():
            self.find(self.menu_locators["Accessories"]).click()
        else:
            self.find(self.locators["Accessories"]).click()

    def click_HMD_Skyline(self):
        if self.check_menu_tab_cover():
            self.find(self.menu_locators["HMD_Skyline"]).click()
        else:
            self.find(self.locators["HMD_Skyline"]).click()

    def click_Offers(self):
        if self.check_menu_tab_cover():
            self.find(self.menu_locators["Offers"]).click()
        else:
            self.find(self.locators["Offers"]).click()

    def click_For_business(self):
        if self.check_menu_tab_cover():
            self.find(self.menu_locators["For_business"]).click()
        else:
            self.find(self.locators["For_business"]).click()

    def click_HMD_logo(self):
        if self.check_menu_tab_cover():
            self.find(self.menu_locators["HMD_logo"]).click()
        else:
            self.find(self.locators["HMD_logo"]).click()