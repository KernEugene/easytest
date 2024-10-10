from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.domain_input_field = page.locator(".FormField_input__5TMnt")
        self.continue_button = page.get_by_text('Continue')
        self.domain_url = 'https://dev.easyboosted.com/login'
        self.login_url = 'https://usko.dev.easyboosted.com/login'
        self.home_page_url = 'https://usko.dev.easyboosted.com/'
        self.login_button = page.get_by_role("button", name="Login")
        self.logout_button = page.locator("//a[contains(@href, 'login')]")
        self.empty_email_or_password_text = '//p[@class="Form_error_message__eWJpd" and text()="These fields are required."]'
        self.no_user_with_matching_data_found = '//p[@class="Form_error_message__eWJpd" and text()="No user with matching data found"]'
        self.invalid_email_or_password_text = '//p[@class="Form_error_message__eWJpd" and text()="Please, enter a valid email"]'

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def select_domain(self):
        self.domain_input_field.fill('usko')
        self.continue_button.click()

    def logout(self):
        self.logout_button.click()
