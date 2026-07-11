from playwright.sync_api import  expect
import pytest
from robot.api import logger
from pytest_robotframework import keyword

def test_login_app(page_instance, target_env):

     #read all env crdentials from json file
    app_url = target_env['base_url']
    app_user = target_env['username']
    app_pass = target_env['password']
    
    page_instance.goto(app_url)
    try:
        page_instance.get_by_label("Username:").fill(app_user)
        page_instance.get_by_label("Password:").fill(app_pass)
        page_instance.get_by_text("Sign In").click()
        page_instance.wait_for_selector("//a[text()='ProtoCommerce']",state="visible")
        expect(page_instance.get_by_role("heading",name="Shop Name")).to_be_visible()
        expect(page_instance.locator("h1")).to_have_text("Shop Name")
        page_instance.wait_for_timeout(1000)
    except Exception as e:
        pytest.fail(f"Logging specific failure: Elements did not load in time. {e}")
           
   
def test_add_products_tocart(page_instance):
    try:
        iphone_x = page_instance.locator("app-card").filter(has_text="iphone X")
        iphone_x.get_by_role("button").click()
        page_instance.wait_for_timeout(1000)
        Nokia_Edge = page_instance.locator("app-card").filter(has_text="Nokia Edge")
        Nokia_Edge.get_by_role("button").click()
        page_instance.wait_for_timeout(4000) 
    except Exception as e:
        pytest.fail(f"Logging specific failure: Elements did not load in time. Details: {e}")   
    

