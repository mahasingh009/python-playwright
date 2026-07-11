import pytest
import json
import os

# 1. Create a fixture that lives for the entire class/module
# @pytest.fixture(scope="module")
# def shared_page(playwright):
#     """Creates a single page session shared by all tests in the module."""
#     # browser = playwright.chromium.launch(headless=False,slow_mo=100, channel="msedge")
#     # browser = playwright.chromium.launch(headless=False,slow_mo=100, channel="chrome")
#     # Channel can be "chrome", "msedge", "chrome-beta", "msedge-beta" or "msedge-dev".
#     browser= playwright.chromium.launch(headless=False)
    
    
#     # Define viewport size for the entire context
#     # context = browser.new_context(viewport={'width': 1900, 'height': 1000}, record_video_dir="videos/")
#     context = browser.new_context(viewport={'width': 1900, 'height': 1000})
#     # 2. Start recording trace details
#     # context.tracing.start(screenshots=True, snapshots=True, sources=True)

#     page = context.new_page()
#     yield page

#     # 3. Stop recording and package it out to disk
#     # context.tracing.stop(path="trace.zip")
#         # Cleanup after all tests finish
#     page.close()
#     context.close()
    

@pytest.fixture(scope="module")
def page_instance(browser):
    """Creates a single page instance shared by all tests in the session."""
    context = browser.new_context(viewport={'width': 1900, 'height': 1000})
    page = context.new_page()
    
    yield page  # This page is passed to all tests
    
    # Teardown: Closes after all tests complete
    page.close()
    context.close()

#Selecting the config file with a command line argument
def pytest_addoption(parser):
  parser.addoption(
    '--target-env',
    action='store',
    default='dev.json',
    help='Path to the target environment config file')

@pytest.fixture(scope="session")
def target_env(request):
  config_path = request.config.getoption('--target-env')
  with open(config_path) as config_file:
    config_data = json.load(config_file)
  return config_data  
