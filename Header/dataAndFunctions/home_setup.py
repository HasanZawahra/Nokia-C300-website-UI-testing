from selenium import webdriver
from Globals.links import links
from Header.pages.home import home as home
from Header.pages.menu import menu
from Header.pages.account import account

class Setup(home, menu, account):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True
    chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})
    # # Options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(2)
    driver.maximize_window()
    driver.get(links.base_link)

