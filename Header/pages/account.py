from selenium.webdriver.common.by import By
from Header.pages.common import Common

class account(Common):

    account_locators = {
        'ENTER_EMAIL_TEXT': (By.CSS_SELECTOR, '#header > dialog > div.css-1xsf3cw.e1l465e24 > div > div.col.css-d0t1lw.e1l465e28.col-xxs-12.col-lg-6 > h2'),
        'PRIVACY_POLICY_TEXT': (By.CSS_SELECTOR, '#header > dialog > div.css-1xsf3cw.e1l465e24 > div > div.col.css-d0t1lw.e1l465e28.col-xxs-12.col-lg-6 > form > div.css-1fxbeoc.e1l465e20 > span'),
        'Privacy_Policy': (By.CSS_SELECTOR, '#header > dialog > div.css-1xsf3cw.e1l465e24 > div > div.col.css-d0t1lw.e1l465e28.col-xxs-12.col-lg-6 > form > div.css-1fxbeoc.e1l465e20 > span > a'),
        'Continue_with_Google_button': (By.CSS_SELECTOR, '#header > dialog > div.css-1xsf3cw.e1l465e24 > div > div.col.css-d0t1lw.e1l465e28.col-xxs-12.col-lg-6 > form > div.css-1owca9d.e1l465e23 > button.e1b0jdit3.css-13sigz4.e1af6ugw0'),
        'MY_ACCOUNT_X': (By.CSS_SELECTOR, '#header > dialog > div.css-1xsf3cw.e1l465e24 > div > div.col.css-1sn8j64.e1l465e29.col-xxs-12.col-lg-5 > button > span > svg'),
    }