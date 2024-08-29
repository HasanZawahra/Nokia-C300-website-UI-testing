import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Footer.dataAndFunctions.Data import Data
from Footer.dataAndFunctions.functions import *
from Footer.dataAndFunctions.links import links

set = Setup(driver=Setup.driver)

def test_click_facebook_logo(set_other_tab_opener):
    assert set.driver.current_url == global_links.buying_link
    set.click_facebook_logo()
    assert set.check_new_tab(links.FACEBOOK_link) == True

def test_click_instagram_logo(set_other_tab_opener):
    assert set.driver.current_url == global_links.buying_link
    set.click_instagram_logo()
    assert set.check_new_tab(links.INSTAGRAM_link) == True

def test_click_tiktok_logo(set_other_tab_opener):
    assert set.driver.current_url == global_links.buying_link
    set.click_tiktok_logo()
    assert set.check_new_tab(links.TIKTOK_link) == True

def test_click_youtube_logo(set_other_tab_opener):
    assert set.driver.current_url == global_links.buying_link
    set.click_youtube_logo()
    time.sleep(5)
    assert set.check_new_tab(links.YOUTUBE_link) == True

def test_click_linked_in_logo(set_other_tab_opener):
    assert set.driver.current_url == global_links.buying_link
    set.click_linked_in_logo()
    assert set.check_new_tab(links.LINKED_IN_link) == True

def test_click_discord_logo(set_other_tab_opener):
    assert set.driver.current_url == global_links.buying_link
    set.click_discord_logo()
    assert set.check_new_tab(links.DISCORD_link) == True

def test_check_visa(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_visa(Data.VISA) == True

def test_check_mastercard(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_mastercard(Data.MASTERCARD) == True

def test_check_discover(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_discover(Data.DISCOVER) == True

def test_check_american_express(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_american_express(Data.AMERICAN_EXPRESS) == True

def test_check_klarna(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_klarna(Data.KLARNA) == True

def test_check_paypal(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_paypal(Data.PAYPAL) == True

def test_check_google_pay(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_google_pay(Data.GOOGLE_PAY) == True

def test_click_united_states(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_united_states()
    assert set.driver.current_url == links.UNITED_STATES_link

def test_click_Espanol(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_Espanol()
    assert set.driver.current_url == links.Espanol_link

def test_check_paragraph(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    par = set.get_paragraph()
    assert par == Data.PARAGRAPH

def test_click_Terms(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_terms()
    assert set.driver.current_url == links.Terms_link

def test_click_Seller_terms(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_seller_terms()
    assert set.driver.current_url == links.Seller_terms_link

def test_click_Privacy(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_privacy()
    assert set.driver.current_url == links.Privacy_link

def test_click_Ethics(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_ethics()
    assert set.driver.current_url == links.Ethics_link

def test_click_speak_up_channel(set_other_tab_opener):
    assert set.driver.current_url == global_links.buying_link
    set.click_speak_up_channel()
    assert set.check_new_tab(links.Speak_up_channel_link) == True

def test_click_HMD_LOGO(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_HMD_logo()
    assert set.driver.current_url == global_links.HMD_logo_link

# def test_close():
#     set.driver.quit()