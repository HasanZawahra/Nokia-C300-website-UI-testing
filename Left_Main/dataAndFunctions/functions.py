import pytest
from Left_Main.dataAndFunctions.home_setup import Setup
from Globals.links import links as global_links

@pytest.fixture
def set_ShopNow_page():
    set = Setup(driver=Setup.driver)
    set.find(set.locators['SHOP_NOW_BUTTON']).click()
    yield set
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_first_big_image_test():
    set = Setup(driver=Setup.driver)
    set.find(set.locators['SHOP_NOW_BUTTON']).click()
    set.find(set.locators['LEFT_SLIDE']).click()
    yield set
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_second_big_image_test():
    set = Setup(driver=Setup.driver)
    set.find(set.locators['SHOP_NOW_BUTTON']).click()
    set.find(set.locators['MIDDLE_SLIDE']).click()
    yield set
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_third_big_image_test():
    set = Setup(driver=Setup.driver)
    set.find(set.locators['SHOP_NOW_BUTTON']).click()
    set.find(set.locators['RIGHT_SLIDE']).click()
    yield set
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_left_arrows_test():
    set = Setup(driver=Setup.driver)
    set.find(set.locators['SHOP_NOW_BUTTON']).click()
    set.find(set.locators['RIGHT_SLIDE']).click()
    yield set
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_right_arrows_test():
    set = Setup(driver=Setup.driver)
    set.find(set.locators['SHOP_NOW_BUTTON']).click()
    set.find(set.locators['LEFT_SLIDE']).click()
    yield set
    set.driver.get(global_links.base_link)