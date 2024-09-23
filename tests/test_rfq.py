import pytest
from dotenv import load_dotenv
from .pages.rfq_page import RfqPage
import os
from .pages.login_page import LoginPage

load_dotenv()


@pytest.fixture(scope="function")
def login(page):
    login_page = LoginPage(page)
    login_page.page.goto(login_page.login_url)
    login_page.login(os.getenv("ADMIN_EMAIL"), os.getenv("ADMIN_PASSWORD"))
    return login_page.page


def test_check_elements_exists(login):
    rfq_page = RfqPage(login)
    rfq_page.go_to_rfq_page()
    rfq_page.check_elements_exist()


def test_skip_rfq(login):
    rfq_page = RfqPage(login)
    rfq_page.go_to_rfq_page()
    rfq_page.click_skip_rfq()

def test_take_rfq_no_options(login):
    rfq_page = RfqPage(login)
    rfq_page.go_to_rfq_page()
    rfq_page.click_take_rfq()
    rfq_page.click_no_options()
    #add catcher for "RFQ is taken"

def test_take_rfq_and_bid(login):
    rfq_page = RfqPage(login)
    rfq_page.go_to_rfq_page()
    rfq_page.click_take_rfq()
    rfq_page.blind_bid()
    #Resolve Bid locator (106 elems)