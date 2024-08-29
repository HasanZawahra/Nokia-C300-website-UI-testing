import pytest
from Header.dataAndFunctions.home_setup import Setup
from Globals.links import links as global_links

@pytest.fixture
def set_ShopNow_page():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    yield set
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_menu_tab():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    curr_url = set.driver.current_url
    assert curr_url == global_links.buying_link
    set.click_menu_icon()
    yield set
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_About_links():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    curr_url = set.driver.current_url
    assert curr_url == global_links.buying_link
    set.click_menu_icon()
    set.click_About()
    yield set
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_repair_reuse_recycle_links():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    curr_url = set.driver.current_url
    assert curr_url == global_links.buying_link
    set.click_menu_icon()
    set.click_repair_reuse_recycle()
    yield set
    set.driver.get(global_links.base_link)

@pytest.fixture
def set_account_tab():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    curr_url = set.driver.current_url
    assert curr_url == global_links.buying_link
    set.click_account_icon()
    yield set
    set.driver.get(global_links.base_link)