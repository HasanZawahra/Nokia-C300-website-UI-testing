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

    def check_new_tab(self, link):
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            curr_link = self.driver.current_url
            if curr_link == link:
                return True
        except Exception as e:
            return e

    def check_payment(self,payment, ref):
        try:
            href = self.find(self.lf_locators[payment]).get_attribute("href")
            if href == ref:
                return True

        except Exception as e:
            return e