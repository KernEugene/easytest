import time

from playwright.sync_api import Page, Locator

from tests.utils.statuses import TruckStatus
from tests.utils.users_list import UserList
from tests.utils.truck_info import TruckInfo


class TrucksPage:
    def __init__(self, page: Page):
        self.page = page
        self.california_address = page.locator(
            "//ul[contains(@class, 'Dropdown_list')]//li[text()='Sacramento, CA 95827']")
        self.location_input_field = page.locator(".FormField_input__5TMnt")
        self.status_drop_down = page.locator(
            "//span[label[contains(text(),'Availability Status')]]//div[contains(@class, 'dropdown-container')]")
        self.user_drop_down = page.locator(
            "//span[label[contains(text(),'Associated User')]]//div[contains(@class, 'dropdown-container')]")
        self.apply_button = page.locator("text=Apply")
        self.tbody_result_of_search = page.locator(".TrucksList_body__-S5IW")
        self.dropdown_content = page.locator(".dropdown_content")
        self.create_truck_button = page.locator("text=+ Create truck")
        self.associated_user = page.locator(
            "//div[contains(@class, 'rmsc GeneralInfo_select__kAa8I GeneralInfo_withPhotos__WQccL')]")
        self.unit = page.locator(
            "//label[contains(text(), 'Unit')]/following-sibling::div//input[contains(@class, 'FormField_input__5TMnt')]")
        self.dispatcher_name = page.locator(
            "//label[contains(text(), \"Dispatcher's Name\")]/following-sibling::div//input[contains(@class, 'FormField_input__5TMnt')]")
        self.dispatcher_phone_number = page.locator(
            "//label[contains(text(), \"Dispatcher's Phone Number\")]/following-sibling::div//input[contains(@class, 'FormField_input__5TMnt')]")
        self.driver_name_1 = page.locator(
            "//label[contains(text(), \"Driver Name 1 \")]/following-sibling::div//input[contains(@class, 'FormField_input__5TMnt')]")
        self.driver_name_2 = page.locator(
            "//label[contains(text(), \"Driver Name 2\")]/following-sibling::div//input[contains(@class, 'FormField_input__5TMnt')]")
        self.driver_phone_1 = page.locator(
            "//label[contains(text(), \"Driver Phone Number 1 \")]/following-sibling::div//input[contains(@class, 'FormField_input__5TMnt')]")
        self.driver_phone_2 = page.locator(
            "//label[contains(text(), \"Driver Phone Number 2\")]/following-sibling::div//input[contains(@class, 'FormField_input__5TMnt')]")
        self.length = page.locator(
            "//label[contains(text(), \"Length\")]/following-sibling::div//input[contains(@class, 'FormField_input__5TMnt')]")
        self.width = page.locator(
            "//label[contains(text(), \"Width\")]/following-sibling::div//input[contains(@class, 'FormField_input__5TMnt')]")
        self.height = page.locator(
            "//label[contains(text(), \"Height\")]/following-sibling::div//input[contains(@class, 'FormField_input__5TMnt')]")
        self.payload = page.locator(
            "//label[contains(text(), \"Payload\")]/following-sibling::div//input[contains(@class, 'FormField_input__5TMnt')]")
        self.create_truck_button_on_truck_page = page.locator(
            '//button[contains(text(), "Create Truck")]'
        )

    def navigate_back(self):
        self.page.go_back()

    def fill_location(self):
        self.location_input_field.fill("Sacramento")
        self.location_input_field.click()
        self.page.wait_for_selector("//ul[contains(@class, 'Dropdown_list')]")
        self.california_address.click()

    def fill_status(self, status: TruckStatus):
        self.status_drop_down.click()
        status_element = self.page.get_by_text(status.value, exact=True)
        status_element.wait_for(state="visible", timeout=5000)
        status_element.click()

    def fill_users(self):
        self.user_drop_down.click()
        self.page.get_by_text("Select all").click()

    def click_apply_button(self):
        self.apply_button.click()

    def verify_results_page_is_available(self):
        self.tbody_result_of_search.wait_for(timeout=5000, state="visible")

    def go_to_create_truck_page(self):
        self.create_truck_button.click()

    def fill_general_truck_info(self, user: UserList, truck_info: TruckInfo):
        self.associated_user.click()
        associated_user_from_list = self.page.get_by_text(user.value, exact=True)
        associated_user_from_list.wait_for(state="visible", timeout=5000)
        associated_user_from_list.click()
        self.unit.fill(truck_info.UNIT.value)
        self.dispatcher_name.fill(truck_info.DISPATCHER_NAME.value)
        self.dispatcher_phone_number.fill(truck_info.DISPATCHER_PHONE.value)

    def fill_driver_info(self, truck_info: TruckInfo):
        self.driver_name_1.fill(truck_info.DRIVER_NAME_1.value)
        self.driver_name_2.fill(truck_info.DRIVER_NAME_2.value)
        self.driver_phone_1.fill(truck_info.DRIVER_1_PHONE.value)
        self.driver_phone_2.fill(truck_info.DRIVER_2_PHONE.value)

    def fill_truck_dims_info(self, truck_info: TruckInfo):
        self.length.fill(truck_info.WIDTH.value)
        self.width.fill(truck_info.LENGTH.value)
        self.height.fill(truck_info.HEIGHT.value)
        self.payload.fill(truck_info.PAYLOAD.value)

    def create_truck(self):
        self.create_truck_button_on_truck_page.click()
        time.sleep(10)
