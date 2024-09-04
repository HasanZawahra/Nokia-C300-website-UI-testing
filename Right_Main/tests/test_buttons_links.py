import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Right_Main.dataAndFunctions.functions import *
from Right_Main.dataAndFunctions.links import links

set = Setup(driver=Setup.driver)

def test_click_unlocked_button_learn_more(set_ShopNow_page):
    set.find(set.locators['Unlocked_button']).click()
    assert set.check_clicked_Unlocked_button() == True
    set.find(set.buttons_locators['unlocked_button_learn_more']).click()
    current_url = set.driver.current_url
    assert current_url == links.unlocked_button_learn_more

def test_click_Unlocked_button_Buy_from_best_buy(set_click_unlocked):
    assert set.check_clicked_Unlocked_button() == True
    assert set.check_new_tab(links.unlocked_button_buy_from_best_buy) != True
    set.find(set.buttons_locators['Unlocked_button_Buy_from_best_buy']).click()
    assert set.check_new_tab(links.unlocked_button_buy_from_best_buy) == True

def test_click_Unlocked_button_buy_from_target(set_click_unlocked):
    assert set.check_clicked_Unlocked_button() == True
    assert set.check_new_tab(links.unlocked_button_buy_from_target) != True
    set.find(set.buttons_locators['Unlocked_button_Buy_from_Target']).click()
    assert set.check_new_tab(links.unlocked_button_buy_from_target) == True

def test_click_Consumer_Cellular_buy_from_Walmart(set_click_consumer_cellular):
    assert set.check_clicked_seller('Consumer_Cellular_buy_from_Walmart') == True
    assert set.check_new_tab(links.consumer_cellular_buy_from_walmart) != True
    set.find(set.buttons_locators['Consumer_Cellular_buy_from_Walmart']).click()
    assert set.check_new_tab(links.consumer_cellular_buy_from_walmart) == True

def test_click_Simple_Mobile_buy_from_Walmart(set_click_simple_mobile):
    assert set.check_clicked_seller('Simple_Mobile_buy_from_Walmart') == True
    assert set.check_new_tab(links.simple_mobile_buy_from_walmart) != True
    set.find(set.buttons_locators['Simple_Mobile_buy_from_Walmart']).click()
    assert set.check_new_tab(links.simple_mobile_buy_from_walmart) == True

def test_click_Straight_Talk_buy_from_Walmart(set_click_straight_talk):
    assert set.check_clicked_seller2('Straight_Talk_buy_from_Walmart', 'Buy_from_Straight_Talk') == True
    assert set.check_new_tab(links.straight_talk_buy_from_walmart) != True
    set.find(set.buttons_locators['Straight_Talk_buy_from_Walmart']).click()
    assert set.check_new_tab(links.straight_talk_buy_from_walmart) == True

def test_click_buy_from_Straight_Talk(set_click_straight_talk):
    assert set.check_clicked_seller2('Straight_Talk_buy_from_Walmart', 'Buy_from_Straight_Talk') == True
    assert set.check_new_tab(links.buy_from_straight_talk) != True
    set.find(set.buttons_locators['Buy_from_Straight_Talk']).click()
    assert set.check_new_tab(links.buy_from_straight_talk) == True

def test_click_Total_by_verizon_buy_from_Walmart(set_click_total_by_verizon):
    assert set.check_clicked_seller2('Total_by_verizon_buy_from_Walmart', 'buy_from_Total_by_verizon') == True
    assert set.check_new_tab(links.total_by_verizon_buy_from_walmart) != True
    set.find(set.buttons_locators['Total_by_verizon_buy_from_Walmart']).click()
    assert set.check_new_tab(links.total_by_verizon_buy_from_walmart) == True

def test_click_buy_from_Total_by_verizon(set_click_total_by_verizon):
    assert set.check_clicked_seller2('Total_by_verizon_buy_from_Walmart', 'buy_from_Total_by_verizon') == True
    assert set.check_new_tab(links.buy_from_total_by_verizon) != True
    set.find(set.buttons_locators['buy_from_Total_by_verizon']).click()
    assert set.check_new_tab(links.buy_from_total_by_verizon) == True

def test_click_Tracfone_buy_from_Walmart(set_click_tracfone):
    assert set.check_clicked_seller('Tracfone_buy_from_Walmart') == True
    assert set.check_new_tab(links.tracfone_buy_from_walmart) != True
    set.find(set.buttons_locators['Tracfone_buy_from_Walmart']).click()
    time.sleep(5)
    assert set.check_new_tab(links.tracfone_buy_from_walmart) == True

def test_click_Walmart_family_mobile_buy_from_Walmart(set_click_walmart_family_mobile):
    assert set.check_clicked_seller('Walmart_family_mobile_buy_from_Walmart') == True
    assert set.check_new_tab(links.walmart_family_mobile_buy_from_walmart) != True
    set.find(set.buttons_locators['Walmart_family_mobile_buy_from_Walmart']).click()
    time.sleep(5)
    assert set.check_new_tab(links.walmart_family_mobile_buy_from_walmart) == True

# def test_close():
#     set.driver.quit()