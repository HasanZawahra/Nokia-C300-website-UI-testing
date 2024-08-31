import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Header.dataAndFunctions.functions import *
from Header.dataAndFunctions.links import links

set = Setup(driver=Setup.driver)

def test_click_Smartphones_link(set_menu_tab):
    assert set.check_menu_tab_cover() == True
    set.click_smartphones()
    curr_url = set.driver.current_url
    assert curr_url == global_links.Smartphones_link

def test_click_Feature_phones(set_menu_tab):
    assert set.check_menu_tab_cover() == True
    set.click_feature_phones()
    curr_url = set.driver.current_url
    assert curr_url == global_links.Feature_phones_link

def test_click_Tablets(set_menu_tab):
    assert set.check_menu_tab_cover() == True
    set.click_tablets()
    curr_url = set.driver.current_url
    assert curr_url == global_links.Tablets_link

def test_click_Accessories(set_menu_tab):
    assert set.check_menu_tab_cover() == True
    set.click_accessories()
    curr_url = set.driver.current_url
    assert curr_url == global_links.Accessories_link

def test_click_HMD_Skyline(set_menu_tab):
    assert set.check_menu_tab_cover() == True
    set.click_HMD_Skyline()
    curr_url = set.driver.current_url
    assert curr_url == global_links.HMD_Skyline_link

def test_click_Offers(set_menu_tab):
    assert set.check_menu_tab_cover() == True
    set.click_Offers()
    curr_url = set.driver.current_url
    assert curr_url == global_links.Offers_link

def test_click_For_business(set_menu_tab):
    assert set.check_menu_tab_cover() == True
    set.click_For_business()
    curr_url = set.driver.current_url
    assert curr_url == global_links.For_business_link

def test_click_HMD_logo(set_menu_tab):
    assert set.check_menu_tab_cover() == True
    set.click_HMD_logo()
    curr_url = set.driver.current_url
    assert curr_url == global_links.HMD_logo_link

def test_click_My_account_button(set_menu_tab):
    assert set.check_menu_tab_cover() == True
    assert set.check_account_tab_cover() == False
    set.find(set.menuLocators["My_account_button"]).click()
    assert set.driver.current_url == global_links.buying_link
    assert set.check_account_tab_cover() == True

def test_click_About(set_menu_tab):
    assert set.check_menu_tab_cover() == True
    assert set.check_about_clicked() == False
    set.find(set.menuLocators["About"]).click()
    assert set.check_about_clicked() == True
    set.find(set.menuLocators["About"]).click()
    assert set.check_about_clicked() == False

def test_click_who_we_are(set_About_links):
    assert set.check_menu_tab_cover() == True
    assert set.check_about_clicked() == True
    set.find(set.menuLocators["who_we_are"]).click()
    curr_url = set.driver.current_url
    assert curr_url == links.who_we_are_link

def test_click_Newsroom(set_About_links):
    assert set.check_menu_tab_cover() == True
    assert set.check_about_clicked() == True
    set.find(set.menuLocators["Newsroom"]).click()
    curr_url = set.driver.current_url
    assert curr_url == links.Newsroom_link

def test_click_Blog(set_menu_tab):
    assert set.check_menu_tab_cover() == True
    set.find(set.menuLocators["Blog"]).click()
    curr_url = set.driver.current_url
    assert curr_url == links.Blog_link

def test_click_Self_repair(set_menu_tab):
    assert set.check_menu_tab_cover() == True
    set.find(set.menuLocators["Self-repair"]).click()
    curr_url = set.driver.current_url
    assert curr_url == links.Self_repair_link

def test_click_Repair_reuse_recycle(set_menu_tab):
    assert set.check_menu_tab_cover() == True
    assert set.check_repair_reuse_recycle_clicked() == False
    set.find(set.menuLocators["Repair, reuse, recycle"]).click()
    assert set.check_repair_reuse_recycle_clicked() == True
    set.find(set.menuLocators["Repair, reuse, recycle"]).click()
    assert set.check_repair_reuse_recycle_clicked() == False

def test_click_repair_reuse_recycle_self_repair(set_repair_reuse_recycle_links):
    assert set.check_menu_tab_cover() == True
    assert set.check_repair_reuse_recycle_clicked() == True
    set.find(set.menuLocators["RRR_self_repair"]).click()
    curr_url = set.driver.current_url
    assert curr_url == links.RRR_self_self_repair_link

def test_click_Device_recycling(set_repair_reuse_recycle_links):
    assert set.check_menu_tab_cover() == True
    assert set.check_repair_reuse_recycle_clicked() == True
    set.find(set.menuLocators["Device_recycling"]).click()
    curr_url = set.driver.current_url
    assert curr_url == links.Device_recycling_link

def test_click_Sustainability(set_menu_tab):
    assert set.check_menu_tab_cover() == True
    set.find(set.menuLocators["Sustainability"]).click()
    curr_url = set.driver.current_url
    assert curr_url == links.Sustainability_link

def test_click_Support(set_menu_tab):
    assert set.check_menu_tab_cover() == True
    set.find(set.menuLocators["Support"]).click()
    curr_url = set.driver.current_url
    assert curr_url == links.Support_link

def test_click_United_States(set_menu_tab):
    assert set.check_menu_tab_cover() == True
    set.find(set.menuLocators["United_States"]).click()
    curr_url = set.driver.current_url
    assert curr_url == links.United_States_link

def test_click_Español(set_menu_tab):
    assert set.check_menu_tab_cover() == True
    set.find(set.menuLocators["Español"]).click()
    curr_url = set.driver.current_url
    assert curr_url == links.Español_link

def test_click_Menu_X(set_menu_tab):
    assert set.check_menu_tab_cover() == True
    set.find(set.menuLocators["MENU_X"]).click()
    assert set.check_menu_tab_cover() == False

# def test_close():
#     set.driver.quit()