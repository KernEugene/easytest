from playwright.sync_api import Page, Locator

class ReportsPage:
    def __init__(self, page: Page):
        self.page = page
        self.reports_url = "https://usko.dev.easyboosted.com/"
        self.settings_dropdown = page.locator(".Toolbar_icon__Gnbkl")
        self.rfq_dropdown = page.get_by_text("RFQ")
        self.trucks_button = page.get_by_role("link", name="TRUCKS")
        self.reports_dropdown = page.get_by_text("REPORTS")
        self.calls_button = page.get_by_role("link", name="CALLS", exact=True)
        self.calls_tracking_button = page.get_by_role("link", name="CALLS & TRACKING")
        self.working_hours_button = page.locator("text=WORKING HOURS")
        self.commissions_check = page.locator("text=COMMISSIONS CHECK")
        self.employee_completeness_info = page.locator("text=Employee completness info")
        self.data_update_button = page.locator("text=DATA UPDATE")
        self.profile_button = page.locator("text=PROFILE")
        self.rfq_all = page.get_by_role("link", name="All")
        self.rfq_dispatched_trucks = page.get_by_role("link", name="Dispatched trucks")

    def open_tile(self, tile: Locator):
        tile.click()

    def navigate_back(self):
        self.page.go_back()



