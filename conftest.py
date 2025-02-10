import os
import toml
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from pages.home_page import HomePage

# Load .env file if present
load_dotenv()

# Load TOML config
CONFIG_FILE = "config.toml"
config = toml.load(CONFIG_FILE) if os.path.exists(CONFIG_FILE) else {}

def pytest_addoption(parser):
    parser.addini("browser", "Browser to use for testing", default=os.getenv("BROWSER", "chromium"))
    parser.addini("headless", "Browser to use for testing", default=False)
    parser.addini("base_url", "Browser to use for testing", default="https://motorway.co.uk")
    
def get_config_value(key, default=None):
    return os.getenv(key.upper()) or config.get("settings", {}).get(key, default)

@pytest.fixture(scope="session")
def config(pytestconfig):
    return {
        "base_url": get_config_value("base_url", pytestconfig.getini("base_url")),
        "browser": get_config_value("browser", pytestconfig.getini("browser")),
        "headless": get_config_value("headless", pytestconfig.getini("headless")) == "true"
    }

@pytest.fixture(scope="session")
def browser(config, request):
    with sync_playwright() as p:
        browser_type = getattr(p, request.config.getini("browser"), p.chromium)
        browser = browser_type.launch(headless=config["headless"])
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()