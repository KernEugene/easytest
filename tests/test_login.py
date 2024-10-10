import pytest
from playwright.sync_api import Page
from dotenv import load_dotenv
import os
from .pages.login_page import LoginPage

load_dotenv()


@pytest.fixture(scope="function")
def login_page(page: Page):
    return LoginPage(page)


def test_valid_login(login_page):
    login_page.page.goto(login_page.login_url)
    login_page.login(os.getenv("ADMIN_EMAIL"), os.getenv("ADMIN_PASSWORD"))
    assert login_page.home_page_url == "https://usko.dev.easyboosted.com/"


def test_select_domain(login_page):
    login_page.page.goto(login_page.domain_url)
    login_page.select_domain()
    assert login_page.page.get_by_text("Enter you Domain to Login").is_visible()


def test_log_out(login_page):
    test_valid_login(login_page)
    login_page.logout()


def test_error_message_incorrect_email_or_password(login_page):
    login_page.page.goto(login_page.login_url)
    login_page.login(os.getenv("ADMIN_EMAIL"), os.getenv("NO_PERMISSIONS_PASSWORD"))
    login_page.page.wait_for_selector(login_page.no_user_with_matching_data_found, state="visible", timeout=10000)


def test_error_message_empty_email_or_password(login_page):
    login_page.page.goto(login_page.login_url)
    login_page.login(os.getenv("EMPTY_EMAIL"), os.getenv("EMPTY_PASSWORD"))
    login_page.page.wait_for_selector(login_page.empty_email_or_password_text, state="visible", timeout=10000)


def test_error_message_invalid_email_or_password(login_page):
    login_page.page.goto(login_page.login_url)
    login_page.login(os.getenv("INVALID_EMAIL"), os.getenv("INVALID_PASSWORD"))
    login_page.page.wait_for_selector(login_page.invalid_email_or_password_text, state="visible", timeout=10000)
