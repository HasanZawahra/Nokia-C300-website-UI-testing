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