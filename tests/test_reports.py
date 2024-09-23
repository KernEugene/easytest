import pytest
from dotenv import load_dotenv
from .pages.reports_page import ReportsPage
import os
from .pages.login_page import LoginPage

load_dotenv()


@pytest.fixture(scope="function")
def login(page):
    login_page = LoginPage(page)
    login_page.page.goto(login_page.login_url)
    login_page.login(os.getenv("ADMIN_EMAIL"), os.getenv("ADMIN_PASSWORD"))
    return login_page.page


def test_settings_access(login):
    settings_page = ReportsPage(login)

    def open_settings_pages(tile_locator):
        settings_page.open_tile(settings_page.settings_dropdown)
        settings_page.open_tile(tile_locator)
        settings_page.navigate_back()

    open_settings_pages(settings_page.data_update_button)
    open_settings_pages(settings_page.profile_button)


def test_reports_access(login):
    reports_page = ReportsPage(login)

    def open_report_pages(tile_locator):
        reports_page.open_tile(reports_page.reports_dropdown)
        reports_page.open_tile(tile_locator)
        reports_page.navigate_back()

    open_report_pages(reports_page.calls_button)
    open_report_pages(reports_page.calls_tracking_button)
    open_report_pages(reports_page.working_hours_button)
    open_report_pages(reports_page.commissions_check)
    open_report_pages(reports_page.employee_completeness_info)


def test_rfq_access(login):
    rfq_page = ReportsPage(login)

    def open_rfq_pages(tile_locator):
        rfq_page.open_tile(rfq_page.rfq_dropdown)
        rfq_page.open_tile(tile_locator)
        rfq_page.navigate_back()

    open_rfq_pages(rfq_page.rfq_all)
    open_rfq_pages(rfq_page.rfq_dispatched_trucks)


def test_trucks_access(login):
    trucks_page = ReportsPage(login)
    trucks_page.trucks_button.wait_for(state="visible", timeout=10000)
    trucks_page.page.goto('https://usko.dev.easyboosted.com/trucks')
