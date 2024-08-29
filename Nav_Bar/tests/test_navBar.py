import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Nav_Bar.dataAndFunctions.Data import Data
from Nav_Bar.dataAndFunctions.functions import *
from Nav_Bar.dataAndFunctions.links import links

set = Setup(driver=Setup.driver)

def test_check_phone_name(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    text = set.get_phone_name()
    assert text == Data.Phone_name

def test_check_price(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    text = set.get_price()
    assert text == Data.Price

def test_click_learn_more(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_learn_more()
    curr_url = set.driver.current_url
    assert curr_url == links.Learn_more_link

def test_click_specs(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_specs()
    curr_url = set.driver.current_url
    assert curr_url == links.Specs_link

def test_click_where_to_buy(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_clicked_where_to_buy() == False
    set.click_where_to_buy()
    time.sleep(1)
    assert set.check_clicked_where_to_buy() == True

def test_close():
    set.driver.quit()