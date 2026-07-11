from playwright.sync_api import Page, expect
import pytest



# identify placeholder locator and assert hidden element
@pytest.mark.smoke
def test_placeholder_hidden(page_instance, target_env):
    app_url = target_env['app_url']
    page_instance.goto(app_url, wait_until="domcontentloaded")
    expect(page_instance.get_by_placeholder("Hide/Show Example")).to_be_visible
    page_instance.get_by_role("button", name="Hide").click()
    page_instance.wait_for_timeout(2000)
    expect(page_instance.get_by_placeholder("Hide/Show Example")).not_to_be_visible
    expect(page_instance.get_by_placeholder("Hide/Show Example")).to_be_hidden

# handle alert pop up
@pytest.mark.smoke
def test_alert_handle(page_instance, target_env):
    app_url = target_env['app_url']
    page_instance.goto(app_url, wait_until="domcontentloaded")
    
    # 1. Register the event listener FIRST
    page_instance.on("dialog", handle_dialog)
    
    # 2. Trigger the action that opens the alert
    page_instance.get_by_role("button", name="Confirm").click()
    page_instance.wait_for_timeout(1000)

def handle_dialog(dialog):
    # Print the alert text
    print(f"Dialog message: {dialog.message}")
    
    # Accept the alert (clicks 'OK')
    dialog.accept()


# handle frames
@pytest.mark.smoke
def test_frames(page_instance):
    framePage = page_instance.frame_locator("#courses-iframe")
    framePage.locator("(//a[contains(text(), 'JOIN NOW')])[1]").is_visible
    framePage.locator("(//a[contains(text(), 'JOIN NOW')])[1]").click()
    framePage.locator("(//a[contains(text(), 'JOIN NOW')])[1]").is_hidden



    