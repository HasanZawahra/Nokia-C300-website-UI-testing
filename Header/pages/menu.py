from selenium.webdriver.common.by import By

from Header.pages.common import Common

class menu(Common):

    menuLocators = {
        'MENU_X': (By.CSS_SELECTOR, '#header > dialog > div > button > span > svg > use'),
        'My_account_button': (By.XPATH, '//*[@id="header"]/dialog/div/div/div[2]/div/button/span'),
        'ACCOUNT_TAB_COVER': (By.CSS_SELECTOR, '#header > dialog > div.css-1xsf3cw.e1l465e24'),
        'About': (By.CSS_SELECTOR, '#navigation-secondary-menu-drawer > details:nth-child(1) > summary > div'),
        'About_details': (By.CSS_SELECTOR, '#navigation-secondary-menu-drawer > details:nth-child(1)'),
        'RRR_details': (By.CSS_SELECTOR, '#navigation-secondary-menu-drawer > details:nth-child(4)'),
        'who_we_are': (By.CSS_SELECTOR, '#navigation-secondary-menu-drawer > details:nth-child(1) > div > ul > li:nth-child(1) > a'),
        'Newsroom': (By.CSS_SELECTOR, '#navigation-secondary-menu-drawer > details:nth-child(1) > div > ul > li:nth-child(2) > a'),
        'Blog': (By.CSS_SELECTOR, '#navigation-secondary-menu-drawer > a:nth-child(2)'),
        'Self-repair': (By.CSS_SELECTOR, '#navigation-secondary-menu-drawer > a:nth-child(3)'),
        'Repair, reuse, recycle': (By.CSS_SELECTOR, '#navigation-secondary-menu-drawer > details:nth-child(4) > summary > div'),
        'RRR_self_repair': (By.CSS_SELECTOR, '#navigation-secondary-menu-drawer > details:nth-child(4) > div > ul > li:nth-child(1) > a'),
        'Device_recycling': (By.CSS_SELECTOR, '#navigation-secondary-menu-drawer > details:nth-child(4) > div > ul > li:nth-child(2) > a'),
        'Sustainability': (By.CSS_SELECTOR, '#navigation-secondary-menu-drawer > a:nth-child(5)'),
        'Support': (By.CSS_SELECTOR, '#navigation-secondary-menu-drawer > a:nth-child(6)'),
        'United_States': (By.CSS_SELECTOR, '#navigation-secondary-menu-drawer > div > a > span'),
        'Español': (By.CSS_SELECTOR, '#navigation-secondary-menu-drawer > div > div > a > span')
    }

    def check_account_tab_cover(self):
        try:
            self.find(self.menuLocators["ACCOUNT_TAB_COVER"])
            return True
        except:
            return False


    def check_dropdwon_list(self, locator):
        details_element = self.find(self.menuLocators[locator])
        is_open = details_element.get_attribute("open") is not None
        return is_open