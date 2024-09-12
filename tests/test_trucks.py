
import pytest
from dotenv import load_dotenv
from .pages.trucks_page import TrucksPage
import os
from .pages.login_page import LoginPage
from tests.test_reports import test_trucks_access
from tests.utils.statuses import TruckStatus
from tests.utils.users_list import UserList
from tests.utils.truck_info import TruckInfo

load_dotenv()


@pytest.fixture(scope="function")
def login(page):
    login_page = LoginPage(page)
    login_page.page.goto(login_page.login_url)
    login_page.login(os.getenv("ADMIN_EMAIL"), os.getenv("ADMIN_PASSWORD"))
    return login_page.page


def test_select_all_filters(login):
    trucks_page = TrucksPage(login)
    test_trucks_access(login)
    trucks_page.verify_results_page_is_available()
    trucks_page.fill_location()
    trucks_page.fill_status(TruckStatus.SELECT_ALL)
    trucks_page.fill_users()
    trucks_page.click_apply_button()
    trucks_page.verify_results_page_is_available()


def test_select_location_filter(login):
    trucks_page = TrucksPage(login)
    test_trucks_access(login)
    trucks_page.verify_results_page_is_available()
    trucks_page.fill_location()
    trucks_page.click_apply_button()
    trucks_page.verify_results_page_is_available()


def test_select_status_filter_all(login):
    trucks_page = TrucksPage(login)
    test_trucks_access(login)
    trucks_page.verify_results_page_is_available()
    trucks_page.fill_status(TruckStatus.SELECT_ALL)
    trucks_page.click_apply_button()
    trucks_page.verify_results_page_is_available()


def test_select_status_filter_available(login):
    trucks_page = TrucksPage(login)
    test_trucks_access(login)
    trucks_page.verify_results_page_is_available()
    trucks_page.fill_status(TruckStatus.AVAILABLE)
    trucks_page.click_apply_button()
    trucks_page.verify_results_page_is_available()


def test_select_status_filter_not_available(login):
    trucks_page = TrucksPage(login)
    test_trucks_access(login)
    trucks_page.verify_results_page_is_available()
    trucks_page.fill_status(TruckStatus.NOT_AVAILABLE)
    trucks_page.click_apply_button()
    trucks_page.verify_results_page_is_available()


def test_select_status_filter_not_en_route(login):
    trucks_page = TrucksPage(login)
    test_trucks_access(login)
    trucks_page.verify_results_page_is_available()
    trucks_page.fill_status(TruckStatus.EN_ROUTE)
    trucks_page.click_apply_button()
    trucks_page.verify_results_page_is_available()


def test_create_truck(login):
    trucks_page = TrucksPage(login)
    test_trucks_access(login)
    trucks_page.go_to_create_truck_page()
    trucks_page.fill_general_truck_info(UserList.YEVHENII_KERN, TruckInfo)
    trucks_page.fill_driver_info(TruckInfo)
    trucks_page.fill_truck_dims_info(TruckInfo)
    trucks_page.create_truck()



