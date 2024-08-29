from selenium.webdriver.common.by import By
from .common import Common

class lower_footer(Common):

    lf_locators = {
        'FACEBOOK_LOGO': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > div > ul > li:nth-child(1) > a > span > svg'),
        'INSTAGRAM_LOGO': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > div > ul > li:nth-child(2) > a > span > svg'),
        'TIKTOK_LOGO': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > div > ul > li:nth-child(3) > a > span > svg'),
        'YOUTUBE_LOGO': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > div > ul > li:nth-child(4) > a > span > svg'),
        'LINKED_IN_LOGO': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > div > ul > li:nth-child(5) > a > span > svg'),
        'DISCORD_LOGO': (By.CSS_SELECTOR, '#app > footer > div.css-667gwk.em903fo0 > div > div > ul > li:nth-child(6) > a > span > svg'),
        'visa': (By.CSS_SELECTOR, '#app > footer > div.ey131wu4.css-phvju4.em903fo0 > div > div:nth-child(1) > ul > li:nth-child(1) > svg > use'),
        'mastercard': (By.CSS_SELECTOR, '#app > footer > div.ey131wu4.css-phvju4.em903fo0 > div > div:nth-child(1) > ul > li:nth-child(2) > svg > use'),
        'discover': (By.CSS_SELECTOR, '#app > footer > div.ey131wu4.css-phvju4.em903fo0 > div > div:nth-child(1) > ul > li:nth-child(3) > svg > use'),
        'american_express': (By.CSS_SELECTOR, '#app > footer > div.ey131wu4.css-phvju4.em903fo0 > div > div:nth-child(1) > ul > li:nth-child(4) > svg > use'),
        'klarna': (By.CSS_SELECTOR, '#app > footer > div.ey131wu4.css-phvju4.em903fo0 > div > div:nth-child(1) > ul > li:nth-child(5) > svg > use'),
        'paypal': (By.CSS_SELECTOR, '#app > footer > div.ey131wu4.css-phvju4.em903fo0 > div > div:nth-child(1) > ul > li:nth-child(6) > svg > use'),
        'google-pay': (By.CSS_SELECTOR, '#app > footer > div.ey131wu4.css-phvju4.em903fo0 > div > div:nth-child(1) > ul > li:nth-child(7) > svg > use'),
        'United_States': (By.CSS_SELECTOR, '#app > footer > div.ey131wu4.css-phvju4.em903fo0 > div > div:nth-child(2) > div.css-1y8b1k0.ey131wu6 > div > a > span'),
        'Espanol': (By.CSS_SELECTOR, '#app > footer > div.ey131wu4.css-phvju4.em903fo0 > div > div:nth-child(2) > div.css-1y8b1k0.ey131wu6 > div > div > a > span'),
        'PARAGRAPH': (By.CSS_SELECTOR, '#app > footer > div.ey131wu4.css-phvju4.em903fo0 > div > div:nth-child(2) > div.css-rhsu7u.ey131wu5 > div:nth-child(1) > p'),
        'Terms': (By.CSS_SELECTOR, '#app > footer > div.ey131wu4.css-phvju4.em903fo0 > div > div:nth-child(2) > ul > li:nth-child(1) > a'),
        'Seller_terms' : (By.CSS_SELECTOR, '#app > footer > div.ey131wu4.css-phvju4.em903fo0 > div > div:nth-child(2) > ul > li:nth-child(2) > a'),
        'Privacy': (By.CSS_SELECTOR, '#app > footer > div.ey131wu4.css-phvju4.em903fo0 > div > div:nth-child(2) > ul > li:nth-child(3) > a'),
        'Ethics': (By.CSS_SELECTOR, '#app > footer > div.ey131wu4.css-phvju4.em903fo0 > div > div:nth-child(2) > ul > li:nth-child(5) > a'),
        'Speak_up_channel': (By.CSS_SELECTOR, '#app > footer > div.ey131wu4.css-phvju4.em903fo0 > div > div:nth-child(2) > ul > li:nth-child(6) > a'),
        'HMD_LOGO': (By.CSS_SELECTOR, '#app > footer > a > svg > use')
    }

    def click_facebook_logo(self):
        self.find(self.lf_locators['FACEBOOK_LOGO']).click()

    def click_instagram_logo(self):
        self.find(self.lf_locators['INSTAGRAM_LOGO']).click()

    def click_tiktok_logo(self):
        self.find(self.lf_locators['TIKTOK_LOGO']).click()

    def click_youtube_logo(self):
        self.find(self.lf_locators['YOUTUBE_LOGO']).click()

    def click_linked_in_logo(self):
        self.find(self.lf_locators['LINKED_IN_LOGO']).click()

    def click_discord_logo(self):
        self.find(self.lf_locators['DISCORD_LOGO']).click()

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

    def check_visa(self, ref):
        try:
            href = self.find(self.lf_locators['visa']).get_attribute("href")
            if href == ref:
                return True
            return False
        except:
            return False

    def check_mastercard(self, ref):
        try:
            href = self.find(self.lf_locators['mastercard']).get_attribute('href')
            if href == ref:
                return True
            return False
        except:
            return False

    def check_discover(self, ref):
        try:
            href = self.find(self.lf_locators['discover']).get_attribute("href")
            if href == ref:
                return True
            return False
        except:
            return False

    def check_american_express(self, ref):
        try:
            href = self.find(self.lf_locators['american_express']).get_attribute("href")
            if href == ref:
                return True
            return False
        except:
            return False

    def check_klarna(self, ref):
        try:
            href = self.find(self.lf_locators['klarna']).get_attribute("href")
            if href == ref:
                return True
            return False
        except:
            return False

    def check_paypal(self, ref):
        try:
            href = self.find(self.lf_locators['paypal']).get_attribute("href")
            if href == ref:
                return True
            return False
        except:
            return False

    def check_google_pay(self, ref):
        try:
            href = self.find(self.lf_locators['google-pay']).get_attribute("href")
            if href == ref:
                return True
            return False
        except:
            return False

    def click_united_states(self):
        self.find(self.lf_locators['United_States']).click()

    def click_Espanol(self):
        self.find(self.lf_locators['Espanol']).click()

    def get_paragraph(self):
        return self.find(self.lf_locators['PARAGRAPH']).text

    def click_terms(self):
        self.find(self.lf_locators['Terms']).click()

    def click_seller_terms(self):
        self.find(self.lf_locators['Seller_terms']).click()

    def click_privacy(self):
        self.find(self.lf_locators['Privacy']).click()

    def click_ethics(self):
        self.find(self.lf_locators['Ethics']).click()

    def click_speak_up_channel(self):
        self.find(self.lf_locators['Speak_up_channel']).click()

    def click_HMD_logo(self):
        self.find(self.lf_locators['HMD_LOGO']).click()


