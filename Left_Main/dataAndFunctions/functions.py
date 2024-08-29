import pytest
from Left_Main.dataAndFunctions.home_setup import Setup
from Globals.links import links as global_links

@pytest.fixture
def set_ShopNow_page():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    yield set
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_first_big_image_test():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    set.click_left_slide()
    yield set
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_second_big_image_test():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    set.click_middle_slide()
    yield set
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_third_big_image_test():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    set.click_right_slide()
    yield set
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_left_arrows_test():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    set.click_right_slide()
    yield set
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_right_arrows_test():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    set.click_left_slide()
    yield set
    set.driver.get(global_links.base_link)