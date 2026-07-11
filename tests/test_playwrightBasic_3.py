# https://rahulshettyacademy.com/client/#/auth/login
# username - jeshirly615@gmail.com
# pass - Testing_009@
import re
import pytest
from playwright.sync_api import Page, expect

@pytest.mark.skip(reason="Feature not implemented yet")
def test_homepage_has_correct_title_and_link(page: Page):
    # 1. Navigate to the website
    page.goto("https://playwright.dev/")

    # 2. Assert the page title contains a specific substring
    expect(page).to_have_title(re.compile("Playwright"))


    # 3. Locate an element (the 'Get started' link) and click it
    page.wait_for_timeout(5000)
    get_started_link = page.get_by_role("link", name="Get started")
    get_started_link.click()
    page.wait_for_timeout(5000)

    # 4. Assert the new page has the expected heading text
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()



