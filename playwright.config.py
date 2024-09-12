from playwright.sync_api import Playwright, sync_playwright

def pytest_playwright_config(playwright: Playwright):
    return {
        "browser": "chromium",
        "headless": True,
        "baseURL": "https://example.com"
    }
