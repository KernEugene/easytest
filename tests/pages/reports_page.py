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

    def open_tile(self, tile: Locator):
        tile.click()

    def navigate_back(self):
        self.page.go_back()
