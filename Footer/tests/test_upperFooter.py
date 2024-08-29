import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Footer.dataAndFunctions.Data import Data
from Footer.dataAndFunctions.links import links
from Footer.dataAndFunctions.functions import *

set = Setup(driver=Setup.driver)

def test_shop_links_list(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    shop_links = set.get_shop_text()
    assert shop_links == Data.SHOP_TEXTS

def test_about_links_list(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    about_links = set.get_about_text()
    assert about_links == Data.ABOUT_TEXTS

def test_the_planet_and_us_links_list(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    the_planet_and_us_links = set.get_the_planet_and_us_text()
    assert the_planet_and_us_links == Data.THE_PLANET_AND_US_TEXTS

def test_support_links_list(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    support_links = set.get_support_text()
    assert support_links == Data.SUPPORT_TEXTS

def test_smartphones_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_smartphones()
    assert set.driver.current_url == global_links.Smartphones_link

def test_feature_phones_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_feature_phones()
    assert set.driver.current_url == global_links.Feature_phones_link

def test_tablets_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_tablets()
    assert set.driver.current_url == global_links.Tablets_link

def test_accessories_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_accessories()
    assert set.driver.current_url == global_links.Accessories_link

def test_offers_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_Offers()
    assert set.driver.current_url == global_links.Offers_link

def test_for_business_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_For_business()
    assert set.driver.current_url == global_links.For_business_link

def test_our_story_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_Our_story()
    assert set.driver.current_url == links.Our_story_link

def test_newsroom_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_Newsroom()
    assert set.driver.current_url == links.Newsroom_link

def test_brand_collaborations_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_Brand_collaborations()
    assert set.driver.current_url == links.Brand_collaborations_link

def test_blog_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_Blog()
    assert set.driver.current_url == links.Blog_link

def test_enterprise_solutions_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_Enterprise_solutions()
    assert set.driver.current_url == links.Enterprise_solutions_link

def test_sustainability_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_Sustainability()
    assert set.driver.current_url == links.Sustainability_link

def test_self_repair_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_Self_repair()
    assert set.driver.current_url == links.Self_repair_link

def test_device_recycling_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_Device_recycling()
    assert set.driver.current_url == links.Device_recycling_link

def test_support_center_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_support_center()
    assert set.driver.current_url == links.Support_center_link

def test_FAQ_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_FAQ()
    assert set.driver.current_url == links.FAQ_link

def test_user_guides_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_User_guides()
    assert set.driver.current_url == links.User_guides_link

def test_software_updates_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_Software_updates()
    assert set.driver.current_url == links.Software_updates_link

def test_service_and_repairs_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_Service_and_repairs()
    assert set.driver.current_url == links.Service_and_repair_link

def test_shopping_online_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_Shopping_online()
    assert set.driver.current_url == links.Shopping_online_link

def test_track_order_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_Track_order()
    assert set.driver.current_url == links.Track_order_link

def test_close():
    set.driver.quit()