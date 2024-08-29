import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Right_Main.dataAndFunctions.Data import Data
from Right_Main.dataAndFunctions.functions import *
from Right_Main.dataAndFunctions.links import links

set = Setup(driver=Setup.driver)

def test_check_phone_name_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.get_phone_name() == Data.PHONE_NAME

def test_check_sentence_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.get_sentence() == Data.SENTENCE

def test_check_feature_1_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.get_feature_1() == Data.FEATURE_1

def test_check_feature_2_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.get_feature_2() == Data.FEATURE_2

def test_check_feature_3_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.get_feature_3() == Data.FEATURE_3

def test_check_price_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.get_price() == Data.PRICE

def test_check_choose_color_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.get_choose_color_text() == Data.CHOOSE_COLOR

def test_check_blue_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.get_blue() == Data.BLUE

def test_check_choose_capacity_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.get_choose_capacity_text() == Data.CHOOSE_CAPACITY

def test_check_storage_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.get_storage() == Data.STORAGE

def test_check_choose_carrier_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.get_choose_carrier_text() == Data.CHOOSE_CARRIER

def test_check_available_at_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.get_available_at_text() == Data.AVAILABLE_AT

def test_check_bottom_text(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.get_bottom_text_1() == Data.BOTTOM_TEXT_1

def test_check_bottom_text_2(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.get_bottom_text_2() == Data.BOTTOM_TEXT_2

def test_check_signs(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.get_check_signs_list() == True

def test_check_image(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    src = set.get_phone_image()
    assert src == links.phone_image_src

def test_check_unlocked_button(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_unlocked_button() == True

def test_check_consumer_cellular(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_consumer_cellular() == True

def test_check_simple_mobile(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_simple_mobile() == True

def test_check_straight_talk(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_straight_talk() == True

def test_check_total_by_verizon(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_total_by_verizon() == True

def test_check_tracfone(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_tracfone() == True

def test_check_walmart_family_mobile(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_walmart_family_mobile() == True

def test_click_unlocked_button(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_clicked_Unlocked_button() == False
    set.click_Unlocked_button()
    assert set.check_clicked_Unlocked_button() == True

def test_click_Consumer_Cellular(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_clicked_consumer_cellular() == False
    set.click_consumer_cellular()
    assert set.check_clicked_consumer_cellular() == True

def test_click_simple_mobile(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_clicked_simple_mobile() == False
    set.click_simple_mobile()
    assert set.check_clicked_simple_mobile() == True

def test_click_straight_talk(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_clicked_straight_talk() == False
    set.click_straight_talk()
    assert set.check_clicked_straight_talk() == True

def test_click_total_by_verizon(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_clicked_total_by_verizon() == False
    set.click_total_by_verizon()
    assert set.check_clicked_total_by_verizon() == True

def test_click_tracfone(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_clicked_tracfone() == False
    set.click_tracfone()
    assert set.check_clicked_tracfone() == True

def test_click_walmart_family_mobile(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_clicked_walmart_family_mobile() == False
    set.click_walmart_family_mobile()
    assert set.check_clicked_walmart_family_mobile() == True

def test_close():
    set.driver.quit()