import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Footer.dataAndFunctions.Data import Data
from Footer.dataAndFunctions.links import links
from Footer.dataAndFunctions.functions import *

set = Setup(driver=Setup.driver)

def test_shop_links_list(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    shop_links = set.find(set.locators['Shop']).text
    assert shop_links == Data.SHOP_TEXTS

def test_about_links_list(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    about_links = set.find(set.locators['ABOUT']).text
    assert about_links == Data.ABOUT_TEXTS

def test_the_planet_and_us_links_list(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    the_planet_and_us_links = set.find(set.locators['The_planet_and_us']).text
    assert the_planet_and_us_links == Data.THE_PLANET_AND_US_TEXTS

def test_support_links_list(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    support_links = set.find(set.locators['Support']).text
    assert support_links == Data.SUPPORT_TEXTS

def test_smartphones_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["Smartphones"]).click()
    assert set.driver.current_url == global_links.Smartphones_link

def test_feature_phones_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["Feature_phones"]).click()
    assert set.driver.current_url == global_links.Feature_phones_link

def test_tablets_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["Tablets"]).click()
    assert set.driver.current_url == global_links.Tablets_link

def test_accessories_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["Accessories"]).click()
    assert set.driver.current_url == global_links.Accessories_link

def test_offers_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["Offers"]).click()
    assert set.driver.current_url == global_links.Offers_link

def test_for_business_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["For_business"]).click()
    assert set.driver.current_url == global_links.For_business_link

def test_our_story_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["Our_story"]).click()
    assert set.driver.current_url == links.Our_story_link

def test_newsroom_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["Newsroom"]).click()
    assert set.driver.current_url == links.Newsroom_link

def test_brand_collaborations_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["Brand_collaborations"]).click()
    assert set.driver.current_url == links.Brand_collaborations_link

def test_blog_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["Blog"]).click()
    assert set.driver.current_url == links.Blog_link

def test_enterprise_solutions_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["Enterprise_solutions"]).click()
    assert set.driver.current_url == links.Enterprise_solutions_link

def test_sustainability_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["Sustainability"]).click()
    assert set.driver.current_url == links.Sustainability_link

def test_self_repair_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["Self_repair"]).click()
    assert set.driver.current_url == links.Self_repair_link

def test_device_recycling_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["Device_recycling"]).click()
    assert set.driver.current_url == links.Device_recycling_link

def test_support_center_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["Support_center"]).click()
    assert set.driver.current_url == links.Support_center_link

def test_FAQ_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["FAQ"]).click()
    assert set.driver.current_url == links.FAQ_link

def test_user_guides_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["User_guides"]).click()
    assert set.driver.current_url == links.User_guides_link

def test_software_updates_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["Software_updates"]).click()
    assert set.driver.current_url == links.Software_updates_link

def test_service_and_repairs_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["Service_and_repairs"]).click()
    assert set.driver.current_url == links.Service_and_repair_link

def test_shopping_online_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["Shopping_online"]).click()
    assert set.driver.current_url == links.Shopping_online_link

def test_track_order_link(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators["Track_order"]).click()
    assert set.driver.current_url == links.Track_order_link

def test_close():
    set.driver.quit()