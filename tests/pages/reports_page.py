import time

from playwright.sync_api import Page, Locator


class ReportsPage:
    def __init__(self, page: Page):
        self.page = page
        self.reports_url = "https://usko.dev.easyboosted.com/"
        self.settings_dropdown = page.locator("#settings")
        self.rfq_dropdown = page.locator("#rfqsettings")
        self.trucks_button = page.locator("//a[contains(@href, 'trucks')]")
        self.reports_dropdown = page.locator("#reports")
        self.calls_button = page.get_by_role("link", name="calls", exact=True)
        self.calls_tracking_button = page.get_by_role("link", name="Calls & Tracking")
        self.working_hours_button = page.locator("text=Working Hours")
        self.commissions_check = page.locator("text=Commissions Check")
        self.employee_completeness_info = page.locator("text=Employee Info")
        self.data_update_button = page.locator("text=Data Update")
        self.profile_button = page.locator("text=Profile")
        self.rfq_all = page.get_by_role("link", name="All")
        self.rfq_dispatched_trucks = page.get_by_role("link", name="Dispatched trucks")
        self.team_selector = page.locator("//*[contains(@class, 'rmsc') and contains(@class, 'ReportForm_select__4frh6') and contains(@class, 'ReportForm_select_middle__JttMd')]")
        self.get_report_button = page.locator("button:has-text('Get Report')")
        self.calls_result_page = page.locator(".Table_content__Zt3js")
        self.calls_and_trucking_result_page = page.locator(".Tracking_tab_container__FRORm")
        self.working_hours_result_page = page.locator(".Table_wrapper__Hh-QA")
        self.not_found_message = page.locator("text=404 Not Found")


    def open_tile(self, tile: Locator):
        tile.click()

    def navigate_back(self):
        self.page.go_back()

    def get_calls_report(self):
        self.team_selector.click()
        self.page.get_by_text('Operations UA').click()
        self.get_report_button.click()
        self.calls_result_page.wait_for(state="visible", timeout=10000)


    def get_calls_and_trucking_report(self):
        self.team_selector.click()
        self.page.get_by_text('Operations PL').click()
        self.get_report_button.click()
        self.calls_and_trucking_result_page.wait_for(state="visible", timeout=10000)


    def get_working_hours_report(self):
        self.team_selector.click()
        self.page.get_by_text('Sales').click()
        self.get_report_button.click()
        self.working_hours_result_page.wait_for(state="visible", timeout=10000)


    def verify_404_massage_displayed(self):
        self.not_found_message.wait_for(state="visible", timeout=10000)



