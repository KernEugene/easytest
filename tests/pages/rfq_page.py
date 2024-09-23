import time
from playwright.sync_api import Page, Locator, expect
from tests.utils.statuses import TruckStatus
from tests.utils.users_list import UserList
from tests.utils.truck_info import TruckInfo
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError

class RfqPage:
    def __init__(self, page: Page):
        self.page = page
        self.available_trucks_counter = page.locator(".Dashboard_trucks__yZFOX")
        self.my_bids_header = page.locator("text=MY BIDS")
        self.bided_time = page.locator("text=Bided Time")
        self.customer_name_email = page.locator("text=Customer Name/ Email")
        self.from_to = page.locator("text=From/ To")
        self.cust_rate_driver_rate = page.locator("text=Cust.Rate/ Driv.Rate")
        self.rfq_information_header = page.locator("text=RFQ INFORMATION")
        self.company_name = page.locator("text=Company Name:")
        self.mc_number = page.locator("text=MC number")
        self.order_number = page.locator("text=Order Number")
        self.pick_up_at = page.locator("text=Pick-up at:")
        self.pick_up_date = page.locator("text=Pick-up date")
        self.deliver_to = page.locator("text=Deliver to:")
        self.delivery_date = page.locator("text=Delivery date:")
        self.miles = page.locator("//span[contains(@class, 'DataCard_title__dVqGF') and text()='Miles:']")
        self.sug_truck_size = page.locator("text=Sug. truck size")
        self.pieces = page.locator("text=Pieces")
        self.weight = page.locator("text=Weight")
        self.dims = page.locator("text=Dims")
        self.stackable = page.locator("text=Stackable")
        self.hazardous = page.locator("text=Hazardous")
        self.fast_load = page.locator("text=FAST load")
        self.dock_level = page.locator("text=Dock level")
        self.unit_number = page.locator("text=Unit #")
        self.name = page.locator("//div[contains(@class, 'AvailableTrucks_cell__daYOg') and text()='Name']")
        self.phone_number = page.locator("text=Phone Number")
        self.driver_miles_out = page.locator("//div[contains(@class, 'AvailableTrucks_cell__daYOg') and text()='Miles']")
        self.ai_cust_rate = page.locator("text=AI cust. rate")
        self.ai_driv_rate = page.locator("text=AI driv. rate")
        self.skip_rfq_button = page.locator("button:has-text('SKIP RFQ')")
        self.take_rfq_button = page.locator("button:has-text('TAKE RFQ')")
        self.no_options_button = page.locator("button:has-text('NO OPTIONS')")
        self.bid_button = page.locator("button:has-text('BID')")
        self.rfq_dropdown = page.locator("#rfqsettings")
        self.blind_bid_checkbox = page.locator('#blindBid')
        self.customer_rate = page.locator('#customerRate')

    def check_elements_exist(self) -> bool:
        elements = [
            self.available_trucks_counter,
            self.my_bids_header,
            self.bided_time,
            self.customer_name_email,
            self.from_to,
            self.cust_rate_driver_rate,
            self.rfq_information_header,
            self.company_name,
            self.mc_number,
            self.order_number,
            self.pick_up_at,
            self.pick_up_date,
            self.deliver_to,
            self.delivery_date,
            self.miles,
            self.sug_truck_size,
            self.pieces,
            self.weight,
            self.dims,
            self.stackable,
            self.hazardous,
            self.fast_load,
            self.dock_level,
            self.unit_number,
            self.name,
            self.phone_number,
            self.driver_miles_out,
            self.ai_cust_rate,
            self.ai_driv_rate,
            self.skip_rfq_button,
            self.take_rfq_button
        ]

        try:
            for element in elements:
                element.wait_for(state="visible", timeout=5000)
        except PlaywrightTimeoutError as e:
            raise AssertionError(f"Element not found or not visible: {str(e)}")

    def go_to_rfq_page(self):
        self.rfq_dropdown.wait_for(state="visible", timeout=10000)
        self.page.goto("https://usko.dev.easyboosted.com/request_for_quote_page")

    def click_skip_rfq(self):
        self.skip_rfq_button.click()

    def click_take_rfq(self):
        self.take_rfq_button.click()

    def click_no_options(self):
        self.no_options_button.click()
        time.sleep(10)

    def blind_bid(self):
        self.bid_button.click()
        self.blind_bid_checkbox.click()
        self.customer_rate.fill('1000')
        self.bid_button.click()

