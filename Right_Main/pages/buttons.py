from selenium.webdriver.common.by import By
from .common import Common

class buttons(Common):

    buttons_locators = {
        'Unlocked_button': (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > section > fieldset > label:nth-child(2)'),
        'Consumer_Cellular': (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > section > fieldset > label:nth-child(3)'),
        'Simple_Mobile': (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > section > fieldset > label:nth-child(4)'),
        'Straight_Talk': (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > section > fieldset > label:nth-child(5)'),
        'Total_by_verizon': (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > section > fieldset > label:nth-child(6)'),
        'Tracfone' : (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > section > fieldset > label:nth-child(7)'),
        'Walmart_family_mobile' : (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > section > fieldset > label:nth-child(8)'),
        'Unlocked_button_text_dev' : (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > section > div'),
        'Available_at_text_dev' : (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > h4'),
        'Unlocked_button_Buy_from_best_buy' : (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > a:nth-child(7) > span'),
        'Unlocked_button_Buy_from_Target' : (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > a:nth-child(8) > svg'),
        'PRICING_NOTE_TEXT' : (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > p'),
        'Consumer_Cellular_buy_from_Walmart' : (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > a > span'),
        'Simple_Mobile_buy_from_Walmart' : (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > a'),
        'Straight_Talk_buy_from_Walmart' : (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > a:nth-child(6) > span'),
        'Buy_from_Straight_Talk' : (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > a:nth-child(7) > svg'),
        'Total_by_verizon_buy_from_Walmart' : (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > a:nth-child(6)'),
        'buy_from_Total_by_verizon' : (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > a:nth-child(7) > span'),
        'Tracfone_buy_from_Walmart' : (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > a > span'),
        'Walmart_family_mobile_buy_from_Walmart' : (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > a > span'),
        'unlocked_button_learn_more' : (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > section > div > a'),
    }

    def click_Unlocked_button_learn_more(self):
        self.find(self.buttons_locators['unlocked_button_learn_more']).click()
    def click_Unlocked_button_Buy_from_best_buy(self):
        self.find(self.buttons_locators['Unlocked_button_Buy_from_best_buy']).click()

    def click_Unlocked_button_buy_from_target(self):
        self.find(self.buttons_locators['Unlocked_button_Buy_from_Target']).click()

    def click_Consumer_Cellular_buy_from_Walmart(self):
        self.find(self.buttons_locators['Consumer_Cellular_buy_from_Walmart']).click()

    def click_Simple_Mobile_buy_from_Walmart(self):
        self.find(self.buttons_locators['Simple_Mobile_buy_from_Walmart']).click()

    def click_Straight_Talk_buy_from_Walmart(self):
        self.find(self.buttons_locators['Straight_Talk_buy_from_Walmart']).click()

    def click_buy_from_Straight_Talk(self):
        self.find(self.buttons_locators['Buy_from_Straight_Talk']).click()

    def click_Total_by_verizon_buy_from_Walmart(self):
        self.find(self.buttons_locators['Total_by_verizon_buy_from_Walmart']).click()

    def click_buy_from_Total_by_verizon(self):
        self.find(self.buttons_locators['buy_from_Total_by_verizon']).click()

    def click_Tracfone_buy_from_Walmart(self):
        self.find(self.buttons_locators['Tracfone_buy_from_Walmart']).click()

    def click_Walmart_family_mobile_buy_from_Walmart(self):
        self.find(self.buttons_locators['Walmart_family_mobile_buy_from_Walmart']).click()

    def check_new_tab(self, link):
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            curr_link = self.driver.current_url
            if curr_link == link:
                return True
            else:
                return False
        except:
            return False



