import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Left_Main.dataAndFunctions.functions import *
from Left_Main.dataAndFunctions.links import links

set = Setup(driver=Setup.driver)

def test_first_image(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    image_src = set.get_first_image()
    assert image_src == links.first_image_src

def test_second_image(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    image_src = set.get_second_image()
    assert image_src == links.second_image_src

def test_third_image(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    image_src = set.get_third_image()
    assert image_src == links.third_image_src

def test_first_big_image(set_first_big_image_test):
    assert set.driver.current_url == global_links.buying_link
    location = set.get_first_big_image_location()
    set.click_middle_slide()
    time.sleep(1)
    assert set.get_first_big_image_location() != location
    set.click_left_slide()
    time.sleep(1)
    assert set.get_first_big_image_location() == location

def test_second_big_image(set_second_big_image_test):
    assert set.driver.current_url == global_links.buying_link
    time.sleep(1)
    location = set.get_second_big_image_location()
    set.click_left_slide()
    time.sleep(1)
    assert set.get_second_big_image_location() != location
    set.click_middle_slide()
    time.sleep(1)
    assert set.get_second_big_image_location() == location

def test_third_big_image(set_third_big_image_test):
    assert set.driver.current_url == global_links.buying_link
    time.sleep(1)
    location = set.get_third_big_image_location()
    set.click_middle_slide()
    time.sleep(1)
    assert set.get_third_big_image_location() != location
    set.click_right_slide()
    time.sleep(1)
    assert set.get_third_big_image_location() == location

def test_sliding_bar(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_sliding_bar() == True

def test_click_first_image(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_first_image()
    assert set.check_first_image() == True

def test_click_second_image(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_second_image()
    assert set.check_second_image() == True

def test_click_third_image(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_third_image()
    assert set.check_third_image() == True

def test_click_left_slide(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.click_left_slide()
    assert set.check_first_image() == True
    set.click_middle_slide()
    assert set.check_second_image() == True
    set.click_left_slide()
    assert set.check_first_image() == True

def test_check_arrows(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_arrows() == True

def test_left_arrow(set_left_arrows_test):
    # in the setup function, I sat the active image to be the last one from the right
    assert set.driver.current_url == global_links.buying_link
    assert set.check_third_image() == True
    assert set.check_disabled_left_arrow() == False
    set.click_left_arrow()
    assert set.check_third_image() == False
    assert set.check_disabled_left_arrow() == False
    assert set.check_second_image() == True
    set.click_left_arrow()
    assert set.check_second_image() == False
    assert set.check_disabled_left_arrow() == True
    assert set.check_first_image() == True

def test_right_arrow(set_right_arrows_test):
    # in the setup function, I sat the active image to be the first one from the left
    assert set.driver.current_url == global_links.buying_link
    assert set.check_first_image() == True
    assert set.check_disabled_right_arrow() == False
    set.click_right_arrow()
    assert set.check_first_image() == False
    assert set.check_disabled_right_arrow() == False
    assert set.check_second_image() == True
    set.click_right_arrow()
    assert set.check_second_image() == False
    assert set.check_disabled_right_arrow() == True
    assert set.check_third_image() == True

def test_close():
    set.driver.quit()