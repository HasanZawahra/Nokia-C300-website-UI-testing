import pytest
from Nav_Bar.dataAndFunctions.home_setup import Setup
from Globals.links import links as global_links

@pytest.fixture
def set_ShopNow_page():
    set = Setup(driver=Setup.driver)
    set.click_shop_now()
    yield set
    set.driver.get(global_links.base_link)