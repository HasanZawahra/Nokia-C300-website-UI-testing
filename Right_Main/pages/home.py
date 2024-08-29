from selenium.webdriver.common.by import By
from .common import Common
from Right_Main.dataAndFunctions.Data import Data

class home(Common):

    locators = {
        'SHOP_NOW_BUTTON': (By.LINK_TEXT, 'Shop now'),
        'PHONE_IMAGE': (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > fieldset:nth-child(2) > div > label > span.css-qz5npc.e92si8b1 > picture > img'),
        'CHECK_SIGNS_LIST': (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > header > ul'),
        'PHONE_NAME': (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > header > div:nth-child(1) > h2'),
        'SENTENCE': (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > header > div.lg.css-1cz7nou.e1oo4q1a3 > p'),
        'FEATURE_1': (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > header > ul > li:nth-child(1)'),
        'FEATURE_2': (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > header > ul > li:nth-child(2)'),
        'FEATURE_3': (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > header > ul > li:nth-child(3)'),
        'PRICE': (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > header > div.css-q750hw.e1oo4q1a7 > div > div > div'),
        'CHOOSE_COLOR': (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > fieldset:nth-child(2) > h2'),
        'BLUE' : (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > fieldset:nth-child(2) > div > label > span.xs.css-jjbr30.e92si8b2 > span'),
        'CHOOSE_CAPACITY': (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > fieldset:nth-child(3) > h2'),
        'STORAGE': (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > fieldset:nth-child(3) > div > div > label'),
        'CHOOSE_CARRIER': (By.CSS_SELECTOR, '#choose-carrier'),
        'AVAILABLE_AT' : (By.CSS_SELECTOR, '#app > main > div > div.col.css-hbdthm.e1j3itnl1.col-md-6.col-xxs-12 > section > fieldset > legend'),
        'BOTTOM_TEXT_1': (By.CSS_SELECTOR, '#app > section > div > div > small > p:nth-child(1)'),
        'BOTTOM_TEXT_2': (By.CSS_SELECTOR, '#app > section > div > div > small > p:nth-child(2)'),
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
    }

    def click_shop_now(self):
        self.find(self.locators['SHOP_NOW_BUTTON']).click()

    def get_phone_name(self):
        return self.find(self.locators['PHONE_NAME']).text

    def get_sentence(self):
        return self.find(self.locators['SENTENCE']).text

    def get_feature_1(self):
        return self.find(self.locators['FEATURE_1']).text

    def get_feature_2(self):
        return self.find(self.locators['FEATURE_2']).text

    def get_feature_3(self):
        return self.find(self.locators['FEATURE_3']).text

    def get_price(self):
        return self.find(self.locators['PRICE']).text

    def get_choose_color_text(self):
        return self.find(self.locators['CHOOSE_COLOR']).text

    def get_blue(self):
        return self.find(self.locators['BLUE']).text

    def get_storage(self):
        return self.find(self.locators['STORAGE']).text

    def get_choose_capacity_text(self):
        return self.find(self.locators['CHOOSE_CAPACITY']).text

    def get_choose_carrier_text(self):
        return self.find(self.locators['CHOOSE_CARRIER']).text

    def get_available_at_text(self):
        return self.find(self.locators['AVAILABLE_AT']).text

    def get_bottom_text_1(self):
        return self.find(self.locators['BOTTOM_TEXT_1']).text

    def get_bottom_text_2(self):
        return self.find(self.locators['BOTTOM_TEXT_2']).text

    def get_phone_image(self):
        return self.find(self.locators['PHONE_IMAGE']).get_attribute('src')

    def get_check_signs_list(self):
        try:
            list = self.find(self.locators['CHECK_SIGNS_LIST'])
            checks = list.find_elements(By.XPATH, "./*")
            if len(checks) == 3:
                return True
            else:
                return False
        except:
            return False

    def check_unlocked_button(self):
        try:
            self.find(self.locators['Unlocked_button'])
            return True
        except:
            return False

    def check_consumer_cellular(self):
        try:
            self.find(self.locators['Consumer_Cellular'])
            return True
        except:
            return False

    def check_simple_mobile(self):
        try:
            self.find(self.locators['Simple_Mobile'])
            return True
        except:
            return False

    def check_straight_talk(self):
        try:
            self.find(self.locators['Straight_Talk'])
            return True
        except:
            return False

    def check_total_by_verizon(self):
        try:
            self.find(self.locators['Total_by_verizon'])
            return True
        except:
            return False

    def check_tracfone(self):
        try:
            self.find(self.locators['Tracfone'])
            return True
        except:
            return False

    def check_walmart_family_mobile(self):
        try:
            self.find(self.locators['Walmart_family_mobile'])
            return True
        except:
            return False


    def click_Unlocked_button(self):
        self.find(self.locators['Unlocked_button']).click()

    def check_clicked_Unlocked_button(self):
        try:
            par = self.find(self.locators['Unlocked_button_text_dev']).text
            available = self.find(self.locators['Available_at_text_dev']).text
            pricing = self.find(self.locators['PRICING_NOTE_TEXT']).text
            self.find(self.locators['Unlocked_button_Buy_from_best_buy'])
            self.find(self.locators['Unlocked_button_Buy_from_Target'])
            if par == Data.UNLOCKED_BUTTON_PARAGRAPH and available == Data.AVAILABLE_AT2 and pricing == Data.PRICING_NOTE:
                return True
            return False
        except:
            return False

    def click_consumer_cellular(self):
        self.find(self.locators['Consumer_Cellular']).click()

    def check_clicked_consumer_cellular(self):
        try:
            available = self.find(self.locators['Available_at_text_dev'])
            pricing = self.find(self.locators['PRICING_NOTE_TEXT'])
            self.find(self.locators['Consumer_Cellular_buy_from_Walmart'])
            if available.text == Data.AVAILABLE_AT2 and pricing.text == Data.PRICING_NOTE:
                return True
            return False
        except:
            return False

    def click_simple_mobile(self):
        self.find(self.locators['Simple_Mobile']).click()

    def check_clicked_simple_mobile(self):
        try:
            available = self.find(self.locators['Available_at_text_dev'])
            pricing = self.find(self.locators['PRICING_NOTE_TEXT'])
            self.find(self.locators['Simple_Mobile_buy_from_Walmart'])
            if available.text == Data.AVAILABLE_AT2 and pricing.text == Data.PRICING_NOTE:
                return True
            return False
        except:
            return False

    def click_straight_talk(self):
        self.find(self.locators['Straight_Talk']).click()

    def check_clicked_straight_talk(self):
        try:
            available = self.find(self.locators['Available_at_text_dev'])
            pricing = self.find(self.locators['PRICING_NOTE_TEXT'])
            self.find(self.locators['Straight_Talk_buy_from_Walmart'])
            self.find(self.locators['Buy_from_Straight_Talk'])
            if available.text == Data.AVAILABLE_AT2 and pricing.text == Data.PRICING_NOTE:
                return True
            return False
        except:
            return False

    def click_total_by_verizon(self):
        self.find(self.locators['Total_by_verizon']).click()

    def check_clicked_total_by_verizon(self):
        try:
            available = self.find(self.locators['Available_at_text_dev'])
            pricing = self.find(self.locators['PRICING_NOTE_TEXT'])
            self.find(self.locators['Total_by_verizon_buy_from_Walmart'])
            self.find(self.locators['buy_from_Total_by_verizon'])
            if available.text == Data.AVAILABLE_AT2 and pricing.text == Data.PRICING_NOTE:
                return True
            return False
        except:
            return False

    def click_tracfone(self):
        self.find(self.locators['Tracfone']).click()

    def check_clicked_tracfone(self):
        try:
            available = self.find(self.locators['Available_at_text_dev'])
            pricing = self.find(self.locators['PRICING_NOTE_TEXT'])
            self.find(self.locators['Tracfone_buy_from_Walmart'])
            if available.text == Data.AVAILABLE_AT2 and pricing.text == Data.PRICING_NOTE:
                return True
            return False
        except:
            return False

    def click_walmart_family_mobile(self):
        self.find(self.locators['Walmart_family_mobile']).click()

    def check_clicked_walmart_family_mobile(self):
        try:
            available = self.find(self.locators['Available_at_text_dev'])
            pricing = self.find(self.locators['PRICING_NOTE_TEXT'])
            self.find(self.locators['Walmart_family_mobile_buy_from_Walmart'])
            if available.text == Data.AVAILABLE_AT2 and pricing.text == Data.PRICING_NOTE:
                return True
            return False
        except:
            return False