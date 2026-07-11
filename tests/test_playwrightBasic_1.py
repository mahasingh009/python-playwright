from playwright.sync_api import Page, expect
import pytest
import re

@pytest.mark.uat
def test_corelocators(page_instance, target_env):
    app_url = target_env['base_url']
    app_user = target_env['username']
    app_pass = target_env['password']

    page_instance.goto(app_url)
    page_instance.get_by_label("Username:").fill(app_user)
    page_instance.get_by_label("Password:").fill(app_pass)
    page_instance.get_by_text("Sign In").click()
    page_instance.wait_for_selector("//a[text()='ProtoCommerce']",state="visible")
    expect(page_instance.get_by_role("heading",name="Shop Name")).to_be_visible()
    expect(page_instance.locator("h1")).to_have_text("Shop Name")

@pytest.mark.uat
def test_add_products_tocart(page_instance):
    iphone_x = page_instance.locator("app-card").filter(has_text="iphone X")
    iphone_x.get_by_role("button").click()
    page_instance.wait_for_timeout(1000)
    Nokia_Edge = page_instance.locator("app-card").filter(has_text="Nokia Edge")
    Nokia_Edge.get_by_role("button").click()
    page_instance.wait_for_timeout(4000)


@pytest.mark.uat
def test_goto_checkout(page_instance):
     page_instance.get_by_text("Checkout").click()
     expect(page_instance.locator(".media-body")).to_have_count(2)
     page_instance.wait_for_timeout(9000)


@pytest.mark.smoke
def test_handle_newPage(page_instance, target_env):
     app_url = target_env['base_url']
     page_instance.goto(app_url, wait_until="domcontentloaded")

     with page_instance.expect_popup() as new_page_info:
        page_instance.get_by_text("Free Access to InterviewQues").click()
        child_page = new_page_info.value
        obj_text = child_page.locator("//p[contains(text(), 'Please email us at')]")
        text= obj_text.text_content()
        string_text = text.split("at")
        exp_email = string_text[1].split("with")
        
        # Define regex for a valid email
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        assert re.match(pattern, exp_email[0].strip())
        
        
        
