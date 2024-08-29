import pytest
from Footer.dataAndFunctions.home_setup import Setup
from Globals.links import links as global_links

@pytest.fixture
def set_ShopNow_page():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    yield set
    set.driver.get(global_links.base_link)
@pytest.fixture
def set_other_tab_opener():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    yield set
    set.driver.switch_to.window(set.driver.window_handles[1])
    set.driver.close()
    set.driver.switch_to.window(set.driver.window_handles[0])
    set.driver.get(global_links.base_link)