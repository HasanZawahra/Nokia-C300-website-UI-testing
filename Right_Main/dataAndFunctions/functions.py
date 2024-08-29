import pytest
from Right_Main.dataAndFunctions.home_setup import Setup
from Globals.links import links as global_links

@pytest.fixture
def set_ShopNow_page():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    yield set
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_click_unlocked():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    assert set.driver.current_url == global_links.buying_link
    set.click_Unlocked_button()
    yield set
    set.driver.switch_to.window(set.driver.window_handles[1])
    set.driver.close()
    set.driver.switch_to.window(set.driver.window_handles[0])
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_click_consumer_cellular():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    assert set.driver.current_url == global_links.buying_link
    set.click_consumer_cellular()
    yield set
    set.driver.switch_to.window(set.driver.window_handles[1])
    set.driver.close()
    set.driver.switch_to.window(set.driver.window_handles[0])
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_click_simple_mobile():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    assert set.driver.current_url == global_links.buying_link
    set.click_simple_mobile()
    yield set
    set.driver.switch_to.window(set.driver.window_handles[1])
    set.driver.close()
    set.driver.switch_to.window(set.driver.window_handles[0])
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_click_straight_talk():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    assert set.driver.current_url == global_links.buying_link
    set.click_straight_talk()
    yield set
    set.driver.switch_to.window(set.driver.window_handles[1])
    set.driver.close()
    set.driver.switch_to.window(set.driver.window_handles[0])
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_click_total_by_verizon():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    assert set.driver.current_url == global_links.buying_link
    set.click_total_by_verizon()
    yield set
    set.driver.switch_to.window(set.driver.window_handles[1])
    set.driver.close()
    set.driver.switch_to.window(set.driver.window_handles[0])
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_click_tracfone():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    assert set.driver.current_url == global_links.buying_link
    set.click_tracfone()
    yield set
    set.driver.switch_to.window(set.driver.window_handles[1])
    set.driver.close()
    set.driver.switch_to.window(set.driver.window_handles[0])
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_click_walmart_family_mobile():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    assert set.driver.current_url == global_links.buying_link
    set.click_walmart_family_mobile()
    yield set
    set.driver.switch_to.window(set.driver.window_handles[1])
    set.driver.close()
    set.driver.switch_to.window(set.driver.window_handles[0])
    set.driver.get(global_links.base_link)