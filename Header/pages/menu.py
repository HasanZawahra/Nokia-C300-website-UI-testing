from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

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

    def click_My_account_button(self):
        self.find(self.menuLocators["My_account_button"]).click()

    def check_account_tab_cover(self, timeout=2):
        try:
            account_tab_cover = WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located(self.menuLocators["ACCOUNT_TAB_COVER"])
            )
            return account_tab_cover.is_displayed()
        except:
            return False

    def click_About(self):
        self.find(self.menuLocators["About"]).click()

    def check_about_clicked(self):
        details_element = self.find(self.menuLocators["About_details"])
        is_open = details_element.get_attribute("open") is not None
        return is_open

    def click_who_we_are(self):
        self.find(self.menuLocators["who_we_are"]).click()

    def click_Newsroom(self):
        self.find(self.menuLocators["Newsroom"]).click()

    def click_Blog(self):
        self.find(self.menuLocators["Blog"]).click()

    def click_self_repair(self):
        self.find(self.menuLocators["Self-repair"]).click()

    def click_repair_reuse_recycle(self):
        self.find(self.menuLocators["Repair, reuse, recycle"]).click()

    def check_repair_reuse_recycle_clicked(self):
        details_element = self.find(self.menuLocators["RRR_details"])
        is_open = details_element.get_attribute("open") is not None
        return is_open

    def click_repair_reuse_recycle_self_repair(self):
        self.find(self.menuLocators["RRR_self_repair"]).click()

    def click_Device_recycling(self):
        self.find(self.menuLocators["Device_recycling"]).click()

    def click_Sustainability(self):
        self.find(self.menuLocators["Sustainability"]).click()

    def click_Support(self):
        self.find(self.menuLocators["Support"]).click()

    def click_United_States(self):
        self.find(self.menuLocators["United_States"]).click()

    def click_Español(self):
        self.find(self.menuLocators["Español"]).click()

    def click_Menu_x(self):
        self.find(self.menuLocators["MENU_X"]).click()