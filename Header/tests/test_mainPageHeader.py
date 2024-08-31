import sys
import os

from Header.dataAndFunctions.functions import *
from Header.dataAndFunctions.links import links
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


set = Setup(driver=Setup.driver)

def test_click_Smartphones_link(set_ShopNow_page):
    curr_url = set.driver.current_url
    assert curr_url == global_links.buying_link
    set.click_smartphones()
    curr_url = set.driver.current_url
    assert curr_url == global_links.Smartphones_link

def test_click_Feature_phones(set_ShopNow_page):
    curr_url = set.driver.current_url
    assert curr_url == global_links.buying_link
    set.click_feature_phones()
    curr_url = set.driver.current_url
    assert curr_url == global_links.Feature_phones_link

def test_click_tablets(set_ShopNow_page):
    curr_url = set.driver.current_url
    assert curr_url == global_links.buying_link
    set.click_tablets()
    curr_url = set.driver.current_url
    assert curr_url == global_links.Tablets_link

def test_click_Accessories(set_ShopNow_page):
    curr_url = set.driver.current_url
    assert curr_url == global_links.buying_link
    set.click_accessories()
    curr_url = set.driver.current_url
    assert curr_url == global_links.Accessories_link

def test_click_HMD_Skyline(set_ShopNow_page):
    curr_url = set.driver.current_url
    assert curr_url == global_links.buying_link
    set.click_HMD_Skyline()
    curr_url = set.driver.current_url
    assert curr_url == global_links.HMD_Skyline_link

def test_click_Offers(set_ShopNow_page):
    curr_url = set.driver.current_url
    assert curr_url == global_links.buying_link
    set.click_Offers()
    curr_url = set.driver.current_url
    assert curr_url == global_links.Offers_link

def test_click_For_business(set_ShopNow_page):
    curr_url = set.driver.current_url
    assert curr_url == global_links.buying_link
    set.click_For_business()
    curr_url = set.driver.current_url
    assert curr_url == global_links.For_business_link

def test_click_HMD_logo(set_ShopNow_page):
    curr_url = set.driver.current_url
    assert curr_url == global_links.buying_link
    set.click_HMD_logo()
    curr_url = set.driver.current_url
    assert curr_url == global_links.HMD_logo_link

def test_click_menu_icon(set_ShopNow_page):
    curr_url = set.driver.current_url
    assert curr_url == global_links.buying_link
    assert set.check_menu_tab_cover() == False
    set.find(set.locators["MENU_ICON"]).click()
    curr_url = set.driver.current_url
    assert curr_url == global_links.buying_link
    assert set.check_menu_tab_cover() == True

def test_click_cart_icon(set_ShopNow_page):
    curr_url = set.driver.current_url
    assert curr_url == global_links.buying_link
    set.find(set.locators["CART_ICON"]).click()
    curr_url = set.driver.current_url
    assert curr_url == links.cart_link

def test_click_account_icon(set_ShopNow_page):
    curr_url = set.driver.current_url
    assert curr_url == global_links.buying_link
    assert set.check_account_tab_cover() == False
    set.find(set.locators["ACCOUNT_ICON"]).click()
    assert curr_url == global_links.buying_link
    assert set.check_account_tab_cover() == True

def test_close():
    set.driver.quit()