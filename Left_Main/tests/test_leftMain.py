import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Left_Main.dataAndFunctions.functions import *
from Left_Main.dataAndFunctions.links import links

set = Setup(driver=Setup.driver)

def test_first_image(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    image_src = set.get_image('FIRST_IMAGE')
    assert image_src == links.first_image_src

def test_second_image(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    image_src = set.get_image('SECOND_IMAGE')
    assert image_src == links.second_image_src

def test_third_image(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    image_src = set.get_image('THIRD_IMAGE')
    assert image_src == links.third_image_src

def test_first_big_image(set_first_big_image_test):
    assert set.driver.current_url == global_links.buying_link
    location = set.get_big_image_location('FIRST_BIG_IMAGE')
    set.find(set.locators['MIDDLE_SLIDE']).click()
    time.sleep(1)
    assert set.get_big_image_location('FIRST_BIG_IMAGE') != location
    set.find(set.locators['LEFT_SLIDE']).click()
    time.sleep(1)
    assert set.get_big_image_location('FIRST_BIG_IMAGE') == location

def test_second_big_image(set_second_big_image_test):
    assert set.driver.current_url == global_links.buying_link
    time.sleep(1)
    location = set.get_big_image_location('SECOND_BIG_IMAGE')
    set.find(set.locators['LEFT_SLIDE']).click()
    time.sleep(1)
    assert set.get_big_image_location('SECOND_BIG_IMAGE') != location
    set.find(set.locators['MIDDLE_SLIDE']).click()
    time.sleep(1)
    assert set.get_big_image_location('SECOND_BIG_IMAGE') == location

def test_third_big_image(set_third_big_image_test):
    assert set.driver.current_url == global_links.buying_link
    time.sleep(1)
    location = set.get_big_image_location('THIRD_BIG_IMAGE')
    set.find(set.locators['MIDDLE_SLIDE']).click()
    time.sleep(1)
    assert set.get_big_image_location('THIRD_BIG_IMAGE') != location
    set.find(set.locators['RIGHT_SLIDE']).click()
    time.sleep(1)
    assert set.get_big_image_location('THIRD_BIG_IMAGE') == location

def test_sliding_bar(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_sliding_bar() == True

def test_click_first_image(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators['FIRST_IMAGE']).click()
    assert set.check_image('1st_IMAGE', 'LEFT_SLIDE', 'MIDDLE_SLIDE', 'RIGHT_SLIDE') == True

def test_click_second_image(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators['SECOND_IMAGE']).click()
    assert set.check_image('2nd_IMAGE', 'MIDDLE_SLIDE', 'LEFT_SLIDE', 'RIGHT_SLIDE') == True

def test_click_third_image(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators['THIRD_IMAGE']).click()
    assert set.check_image('3rd_IMAGE', 'RIGHT_SLIDE', 'LEFT_SLIDE', 'MIDDLE_SLIDE') == True

def test_click_left_slide(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators['LEFT_SLIDE']).click()
    assert set.check_image('1st_IMAGE', 'LEFT_SLIDE', 'MIDDLE_SLIDE', 'RIGHT_SLIDE') == True
    set.find(set.locators['MIDDLE_SLIDE']).click()
    assert set.check_image('2nd_IMAGE', 'MIDDLE_SLIDE', 'LEFT_SLIDE', 'RIGHT_SLIDE') == True
    set.find(set.locators['LEFT_SLIDE']).click()
    assert set.check_image('1st_IMAGE', 'LEFT_SLIDE', 'MIDDLE_SLIDE', 'RIGHT_SLIDE') == True

def test_click_middle_slide(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators['MIDDLE_SLIDE']).click()
    assert set.check_image('2nd_IMAGE', 'MIDDLE_SLIDE', 'LEFT_SLIDE', 'RIGHT_SLIDE') == True
    set.find(set.locators['LEFT_SLIDE']).click()
    assert set.check_image('1st_IMAGE', 'LEFT_SLIDE', 'MIDDLE_SLIDE', 'RIGHT_SLIDE') == True
    set.find(set.locators['RIGHT_SLIDE']).click()
    assert set.check_image('3rd_IMAGE', 'RIGHT_SLIDE', 'LEFT_SLIDE', 'MIDDLE_SLIDE') == True

def test_click_right_slide(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    set.find(set.locators['RIGHT_SLIDE']).click()
    assert set.check_image('3rd_IMAGE', 'RIGHT_SLIDE', 'LEFT_SLIDE', 'MIDDLE_SLIDE') == True
    set.find(set.locators['MIDDLE_SLIDE']).click()
    assert set.check_image('2nd_IMAGE', 'MIDDLE_SLIDE', 'LEFT_SLIDE', 'RIGHT_SLIDE') == True
    set.find(set.locators['RIGHT_SLIDE']).click()
    assert set.check_image('3rd_IMAGE', 'RIGHT_SLIDE', 'LEFT_SLIDE', 'MIDDLE_SLIDE') == True

def test_check_arrows(set_ShopNow_page):
    assert set.driver.current_url == global_links.buying_link
    assert set.check_arrows() == True

def test_left_arrow(set_left_arrows_test):
    # in the setup function, I sat the active image to be the last one from the right
    assert set.driver.current_url == global_links.buying_link
    assert set.check_image('3rd_IMAGE', 'RIGHT_SLIDE', 'LEFT_SLIDE', 'MIDDLE_SLIDE') == True
    assert set.check_disabled_arrow("LEFT_ARROW") == False
    set.find(set.locators['LEFT_ARROW']).click()
    assert set.check_image('3rd_IMAGE', 'RIGHT_SLIDE', 'LEFT_SLIDE', 'MIDDLE_SLIDE') == False
    assert set.check_disabled_arrow("LEFT_ARROW") == False
    assert set.check_image('2nd_IMAGE', 'MIDDLE_SLIDE', 'LEFT_SLIDE', 'RIGHT_SLIDE') == True
    set.find(set.locators['LEFT_ARROW']).click()
    assert set.check_image('2nd_IMAGE', 'MIDDLE_SLIDE', 'LEFT_SLIDE', 'RIGHT_SLIDE') == False
    assert set.check_disabled_arrow("LEFT_ARROW") == True
    assert set.check_image('1st_IMAGE', 'LEFT_SLIDE', 'MIDDLE_SLIDE', 'RIGHT_SLIDE') == True

def test_right_arrow(set_right_arrows_test):
    # in the setup function, I sat the active image to be the first one from the left
    assert set.driver.current_url == global_links.buying_link
    assert set.check_image('1st_IMAGE', 'LEFT_SLIDE', 'MIDDLE_SLIDE', 'RIGHT_SLIDE') == True
    assert set.check_disabled_arrow("RIGHT_ARROW") == False
    set.find(set.locators['RIGHT_ARROW']).click()
    assert set.check_image('1st_IMAGE', 'LEFT_SLIDE', 'MIDDLE_SLIDE', 'RIGHT_SLIDE') == False
    assert set.check_disabled_arrow("RIGHT_ARROW") == False
    assert set.check_image('2nd_IMAGE', 'MIDDLE_SLIDE', 'LEFT_SLIDE', 'RIGHT_SLIDE') == True
    set.find(set.locators['RIGHT_ARROW']).click()
    assert set.check_image('2nd_IMAGE', 'MIDDLE_SLIDE', 'LEFT_SLIDE', 'RIGHT_SLIDE') == False
    assert set.check_disabled_arrow("RIGHT_ARROW") == True
    assert set.check_image('3rd_IMAGE', 'RIGHT_SLIDE', 'LEFT_SLIDE', 'MIDDLE_SLIDE') == True

def test_close():
    set.driver.quit()