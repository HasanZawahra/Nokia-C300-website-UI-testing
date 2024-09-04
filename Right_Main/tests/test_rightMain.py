import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Right_Main.dataAndFunctions.Data import Data
from Right_Main.dataAndFunctions.functions import *
from Right_Main.dataAndFunctions.links import links

set = Setup(driver=Setup.driver)

def test_check_phone_name_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.find(set.locators['PHONE_NAME']).text == Data.PHONE_NAME

def test_check_sentence_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.find(set.locators['SENTENCE']).text == Data.SENTENCE

def test_check_feature_1_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.find(set.locators['FEATURE_1']).text == Data.FEATURE_1

def test_check_feature_2_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.find(set.locators['FEATURE_2']).text == Data.FEATURE_2

def test_check_feature_3_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.find(set.locators['FEATURE_3']).text == Data.FEATURE_3

def test_check_price_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.find(set.locators['PRICE']).text == Data.PRICE

def test_check_choose_color_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.find(set.locators['CHOOSE_COLOR']).text == Data.CHOOSE_COLOR

def test_check_blue_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.find(set.locators['BLUE']).text == Data.BLUE

def test_check_choose_capacity_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.find(set.locators['CHOOSE_CAPACITY']).text == Data.CHOOSE_CAPACITY

def test_check_storage_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.find(set.locators['STORAGE']).text == Data.STORAGE

def test_check_choose_carrier_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.find(set.locators['CHOOSE_CARRIER']).text == Data.CHOOSE_CARRIER

def test_check_available_at_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.find(set.locators['AVAILABLE_AT']).text == Data.AVAILABLE_AT

def test_check_bottom_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.find(set.locators['BOTTOM_TEXT_1']).text == Data.BOTTOM_TEXT_1

def test_check_bottom_text_2(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.find(set.locators['BOTTOM_TEXT_2']).text == Data.BOTTOM_TEXT_2

def test_check_signs(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.get_check_signs_list() == True

def test_check_image(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    src = set.get_phone_image()
    assert src == links.phone_image_src

def test_check_unlocked_button(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_button('Unlocked_button') == True

def test_check_consumer_cellular(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_button('Consumer_Cellular') == True

def test_check_simple_mobile(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_button('Simple_Mobile') == True

def test_check_straight_talk(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_button('Straight_Talk') == True

def test_check_total_by_verizon(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_button('Total_by_verizon') == True

def test_check_tracfone(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_button('Tracfone') == True

def test_check_walmart_family_mobile(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_button('Walmart_family_mobile') == True

def test_click_unlocked_button(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_clicked_Unlocked_button() != True
    set.find(set.locators['Unlocked_button']).click()
    assert set.check_clicked_Unlocked_button() == True

def test_click_Consumer_Cellular(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_clicked_seller('Consumer_Cellular_buy_from_Walmart') != True
    set.find(set.locators['Consumer_Cellular']).click()
    assert set.check_clicked_seller('Consumer_Cellular_buy_from_Walmart') == True

def test_click_simple_mobile(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_clicked_seller('Simple_Mobile_buy_from_Walmart') != True
    set.find(set.locators['Simple_Mobile']).click()
    assert set.check_clicked_seller('Simple_Mobile_buy_from_Walmart') == True

def test_click_straight_talk(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_clicked_seller2('Straight_Talk_buy_from_Walmart', 'Buy_from_Straight_Talk') != True
    set.find(set.locators['Straight_Talk']).click()
    assert set.check_clicked_seller2('Straight_Talk_buy_from_Walmart', 'Buy_from_Straight_Talk') == True

def test_click_total_by_verizon(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_clicked_seller2('Total_by_verizon_buy_from_Walmart', 'buy_from_Total_by_verizon') != True
    set.find(set.locators['Total_by_verizon']).click()
    assert set.check_clicked_seller2('Total_by_verizon_buy_from_Walmart', 'buy_from_Total_by_verizon') == True

def test_click_tracfone(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_clicked_seller('Tracfone_buy_from_Walmart') != True
    set.find(set.locators['Tracfone']).click()
    assert set.check_clicked_seller('Tracfone_buy_from_Walmart') == True

def test_click_walmart_family_mobile(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_clicked_seller('Walmart_family_mobile_buy_from_Walmart') != True
    set.find(set.locators['Walmart_family_mobile']).click()
    assert set.check_clicked_seller('Walmart_family_mobile_buy_from_Walmart') == True

def test_close():
    set.driver.quit()