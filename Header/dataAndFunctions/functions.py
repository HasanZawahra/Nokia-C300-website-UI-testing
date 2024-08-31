import pytest
from Header.dataAndFunctions.home_setup import Setup
from Globals.links import links as global_links

@pytest.fixture
def set_ShopNow_page():
    set = Setup(driver=Setup.driver)
    set.find(set.locators["SHOP_NOW_BUTTON"]).click()
    yield set
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_menu_tab():
    set = Setup(driver=Setup.driver)
    set.find(set.locators["SHOP_NOW_BUTTON"]).click()
    curr_url = set.driver.current_url
    assert curr_url == global_links.buying_link
    set.find(set.locators["MENU_ICON"]).click()
    yield set
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_About_links():
    set = Setup(driver=Setup.driver)
    set.find(set.locators["SHOP_NOW_BUTTON"]).click()
    curr_url = set.driver.current_url
    assert curr_url == global_links.buying_link
    set.find(set.locators["MENU_ICON"]).click()
    set.find(set.menuLocators["About"]).click()
    yield set
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_repair_reuse_recycle_links():
    set = Setup(driver=Setup.driver)
    set.find(set.locators["SHOP_NOW_BUTTON"]).click()
    curr_url = set.driver.current_url
    assert curr_url == global_links.buying_link
    set.find(set.locators["MENU_ICON"]).click()
    set.find(set.menuLocators["Repair, reuse, recycle"]).click()
    yield set
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_account_tab():
    set = Setup(driver=Setup.driver)
    set.find(set.locators["SHOP_NOW_BUTTON"]).click()
    curr_url = set.driver.current_url
    assert curr_url == global_links.buying_link
    set.find(set.locators["ACCOUNT_ICON"]).click()
    yield set
    set.driver.get(global_links.base_link)