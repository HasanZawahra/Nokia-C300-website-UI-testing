import pytest
from Right_Main.dataAndFunctions.home_setup import Setup
from Globals.links import links as global_links

@pytest.fixture
def set_ShopNow_page():
    set = Setup(driver=Setup.driver)
    set.find(set.locators['SHOP_NOW_BUTTON']).click()
    yield set
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_click_unlocked():
    set = Setup(driver=Setup.driver)
    set.find(set.locators['SHOP_NOW_BUTTON']).click()
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators['Unlocked_button']).click()
    yield set
    set.driver.switch_to.window(set.driver.window_handles[1])
    set.driver.close()
    set.driver.switch_to.window(set.driver.window_handles[0])
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_click_consumer_cellular():
    set = Setup(driver=Setup.driver)
    set.find(set.locators['SHOP_NOW_BUTTON']).click()
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators['Consumer_Cellular']).click()
    yield set
    set.driver.switch_to.window(set.driver.window_handles[1])
    set.driver.close()
    set.driver.switch_to.window(set.driver.window_handles[0])
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_click_simple_mobile():
    set = Setup(driver=Setup.driver)
    set.find(set.locators['SHOP_NOW_BUTTON']).click()
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators['Simple_Mobile']).click()
    yield set
    set.driver.switch_to.window(set.driver.window_handles[1])
    set.driver.close()
    set.driver.switch_to.window(set.driver.window_handles[0])
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_click_straight_talk():
    set = Setup(driver=Setup.driver)
    set.find(set.locators['SHOP_NOW_BUTTON']).click()
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators['Straight_Talk']).click()
    yield set
    set.driver.switch_to.window(set.driver.window_handles[1])
    set.driver.close()
    set.driver.switch_to.window(set.driver.window_handles[0])
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_click_total_by_verizon():
    set = Setup(driver=Setup.driver)
    set.find(set.locators['SHOP_NOW_BUTTON']).click()
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators['Total_by_verizon']).click()
    yield set
    set.driver.switch_to.window(set.driver.window_handles[1])
    set.driver.close()
    set.driver.switch_to.window(set.driver.window_handles[0])
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_click_tracfone():
    set = Setup(driver=Setup.driver)
    set.find(set.locators['SHOP_NOW_BUTTON']).click()
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators['Tracfone']).click()
    yield set
    set.driver.switch_to.window(set.driver.window_handles[1])
    set.driver.close()
    set.driver.switch_to.window(set.driver.window_handles[0])
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_click_walmart_family_mobile():
    set = Setup(driver=Setup.driver)
    set.find(set.locators['SHOP_NOW_BUTTON']).click()
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators['Walmart_family_mobile']).click()
    yield set
    set.driver.switch_to.window(set.driver.window_handles[1])
    set.driver.close()
    set.driver.switch_to.window(set.driver.window_handles[0])
    set.driver.get(global_links.base_link)