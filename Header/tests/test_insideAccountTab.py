import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Header.dataAndFunctions.Data import Data
from Header.dataAndFunctions.functions import *
from Header.dataAndFunctions.links import links

set = Setup(driver=Setup.driver)

def test_check_enter_email_text(set_account_tab):
    assert set.check_account_tab_cover() == True
    text = set.get_enter_email_text()
    assert text == Data.enter_email_text

def test_click_HMD_logo(set_account_tab):
    assert set.check_account_tab_cover() == True
    set.click_HMD_logo()
    curr_url = set.driver.current_url
    assert curr_url == global_links.HMD_logo_link

def test_check_privacy_policy_text(set_account_tab):
    assert set.check_account_tab_cover() == True
    text = set.get_privacy_policy_text()
    assert Data.privacy_policy_text in text

def test_click_privacy_policy(set_account_tab):
    assert set.check_account_tab_cover() == True
    set.click_privacy_policy()
    curr_url = set.driver.current_url
    assert curr_url == links.Privacy_Policy_link

def test_click_continue_with_google(set_account_tab):
    assert set.check_account_tab_cover() == True
    set.click_continue_with_google()
    curr_url = set.driver.current_url
    assert links.Continue_with_Google_link in curr_url

def test_click_my_account_x(set_account_tab):
    assert set.check_account_tab_cover() == True
    set.click_my_account_x()
    assert set.check_account_tab_cover() == False

# def test_close():
#     set.driver.quit()