from playwright.sync_api import Page, expect
import pytest
import os
import sys

# Dynamic path resolution to find the project root
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

# Now you can import safely
from Util.funtions import generate_dummy_users, read_json_file


@pytest.mark.smoke
def test_get_started_link(page_instance):
    page_instance.goto("https://www.purolator.com/en")

    # read selectorrs from json
    dict = read_json_file("./locators/pageObjects.json")
    obj_register_link= dict["landing_page"]["obj_register_link"]
    obj_ship_online_link = dict["landing_page"]["obj_ship_online_link"]
    obj_open_puro_account = dict["landing_page"]["obj_open_puro_account"]

    # Click the get started link.
    register_link = page_instance.wait_for_selector(obj_register_link ,timeout=3000,state="visible")
    register_link.click()
    page_instance.wait_for_timeout(1000)

    # Expects page to have a heading with the name of Installation.
    shop_online_button = page_instance.wait_for_selector(obj_ship_online_link, timeout=3000,state="visible")
    shop_online_button.click()
    page_instance.wait_for_timeout(2000)
    open_puro_acc_radio_btn = page_instance.locator(obj_open_puro_account)
    open_puro_acc_radio_btn.click()
    page_instance.wait_for_timeout(2000)

@pytest.mark.smoke
def test_fill_user_details(page_instance):
    
    dict = read_json_file("./locators/pageObjects.json")
    obj_firstnameEdit = dict["register_users"]["obj_firstnameEdit"]
    obj_lastnameEdit = dict["register_users"]["obj_lastnameEdit"]
    obj_contactEmail = dict["register_users"]["obj_contactEmail"]
    obj_retypecontactEmail = dict["register_users"]["obj_retypecontactEmail"]
    obj_username = dict["register_users"]["obj_username"]
    obj_createpass = dict["register_users"]["obj_createpass"]
    obj_retypepass = dict["register_users"]["obj_retypepass"]

    data_list = generate_dummy_users(5)
    for data in data_list:
        firstName = data['first_name']
        lastname = data['last_name']
        username = data['username']
        user_email = data['email']
        pass_word = data['password']
        
        page_instance.locator(obj_firstnameEdit).fill(firstName)
        page_instance.locator(obj_lastnameEdit).fill(lastname)
        page_instance.locator(obj_contactEmail).fill(user_email)
        page_instance.locator(obj_retypecontactEmail).fill(user_email)
        page_instance.locator(obj_username).fill(username)
        page_instance.locator(obj_createpass).fill(pass_word)
        page_instance.locator(obj_retypepass).fill(pass_word)
        page_instance.wait_for_timeout(1000)
    


    