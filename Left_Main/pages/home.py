from selenium.webdriver.common.by import By
from .common import Common
class home(Common):

    locators = {
        'SHOP_NOW_BUTTON': (By.LINK_TEXT, 'Shop now'),
        'FIRST_IMAGE': (By.CSS_SELECTOR, '#app > main > div > div.col.css-16cxww.e1j3itnl2.col-md-6.col-xxs-12 > div > div > ul > li.active.css-1ylw0h1.e3k2d6h0 > button > picture > img'),
        'SECOND_IMAGE': (By.CSS_SELECTOR, '#app > main > div > div.col.css-16cxww.e1j3itnl2.col-md-6.col-xxs-12 > div > div > ul > li:nth-child(2) > button > picture > img'),
        'THIRD_IMAGE': (By.CSS_SELECTOR, '#app > main > div > div.col.css-16cxww.e1j3itnl2.col-md-6.col-xxs-12 > div > div > ul > li:nth-child(3) > button > picture > img'),
        'BIG_IMAGE': (By.CSS_SELECTOR, '#app > main > div > div.col.css-16cxww.e1j3itnl2.col-md-6.col-xxs-12 > div > div > div > ul > li:nth-child(1) > button > picture > img'),
        'LEFT_SLIDE': (By.CSS_SELECTOR, '#app > main > div > div.col.css-16cxww.e1j3itnl2.col-md-6.col-xxs-12 > div > div > div > div > div > div > ul > li:nth-child(1) > button'),
        'MIDDLE_SLIDE': (By.CSS_SELECTOR, '#app > main > div > div.col.css-16cxww.e1j3itnl2.col-md-6.col-xxs-12 > div > div > div > div > div > div > ul > li:nth-child(2) > button'),
        'RIGHT_SLIDE': (By.CSS_SELECTOR, '#app > main > div > div.col.css-16cxww.e1j3itnl2.col-md-6.col-xxs-12 > div > div > div > div > div > div > ul > li:nth-child(3) > button'),
        'SLIDING_BAR': (By.CSS_SELECTOR, '#app > main > div > div.col.css-16cxww.e1j3itnl2.col-md-6.col-xxs-12 > div > div > div > div > div > div > ul'),
        '1st_IMAGE': (By.CSS_SELECTOR, '#app > main > div > div.col.css-16cxww.e1j3itnl2.col-md-6.col-xxs-12 > div > div > ul > li:nth-child(1)'),
        '2nd_IMAGE': (By.CSS_SELECTOR, '#app > main > div > div.col.css-16cxww.e1j3itnl2.col-md-6.col-xxs-12 > div > div > ul > li:nth-child(2)'),
        '3rd_IMAGE': (By.CSS_SELECTOR, '#app > main > div > div.col.css-16cxww.e1j3itnl2.col-md-6.col-xxs-12 > div > div > ul > li:nth-child(3)'),
        'ARROWS': (By.CSS_SELECTOR, '#app > main > div > div.col.css-16cxww.e1j3itnl2.col-md-6.col-xxs-12 > div > div > div > div > div > div > ul > li.css-1ec9tq.eah9xwi0'),
        'LEFT_ARROW': (By.CSS_SELECTOR, '#app > main > div > div.col.css-16cxww.e1j3itnl2.col-md-6.col-xxs-12 > div > div > div > div > div > div > ul > li.css-1ec9tq.eah9xwi0 > button:nth-child(1)'),
        'RIGHT_ARROW': (By.CSS_SELECTOR, '#app > main > div > div.col.css-16cxww.e1j3itnl2.col-md-6.col-xxs-12 > div > div > div > div > div > div > ul > li.css-1ec9tq.eah9xwi0 > button:nth-child(2)'),
        'FIRST_BIG_IMAGE': (By.CSS_SELECTOR, '#app > main > div > div.col.css-16cxww.e1j3itnl2.col-md-6.col-xxs-12 > div > div > div > ul > li:nth-child(1) > button > picture > img'),
        'SECOND_BIG_IMAGE': (By.CSS_SELECTOR, '#app > main > div > div.col.css-16cxww.e1j3itnl2.col-md-6.col-xxs-12 > div > div > div > ul > li:nth-child(2) > button > picture > img'),
        'THIRD_BIG_IMAGE': (By.CSS_SELECTOR, '#app > main > div > div.col.css-16cxww.e1j3itnl2.col-md-6.col-xxs-12 > div > div > div > ul > li:nth-child(3) > button > picture > img')
    }

    def get_image(self, image):
        return self.find(self.locators[image]).get_attribute('src')
    def get_big_image_location(self, image):
        return self.find(self.locators[image]).location

    def check_sliding_bar(self):
        bar = self.find(self.locators['SLIDING_BAR'])
        child_elements = bar.find_elements(By.XPATH, "./*")
        count = 0
        for child in child_elements:
            if 'css-ehzz0m eah9xwi1' == child.get_attribute('class'):
                count += 1
        if count == 3:
            return True
        else:
            return False

    def check_image(self, classes, clicked, other1, other2):
        classes = self.find(self.locators[classes]).get_attribute('class')
        slide_classes = self.find(self.locators[clicked]).get_attribute('class')
        other_slide_classes = self.find(self.locators[other1]).get_attribute('class')+self.find(self.locators[other2]).get_attribute('class')
        active_slide = 'e1arj6xw0 css-bxj52c e1af6ugw0'
        other_slide = 'e1arj6xw0 css-1xmudvv e1af6ugw0'
        return 'active' in classes and active_slide == slide_classes and other_slide in other_slide_classes

    def check_arrows(self):
        arrows = self.find(self.locators['ARROWS'])
        child_elements = arrows.find_elements(By.XPATH, "./*")
        if len(child_elements) == 2:
            return True
        else:
            return False

    def check_disabled_arrow(self, arrow):
        dialog_element = self.find(self.locators[arrow])
        is_disabled = dialog_element.get_attribute("disabled") is not None
        return is_disabled