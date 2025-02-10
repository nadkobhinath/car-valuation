from pages.base_page import BasePage

class MoreDetailsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_input_field = page.locator("input[data-cy='emailInputField']")
        self.email_input = page.locator("input[data-cy='emailInput']")
        self.see_valuation_button = page.locator("button[data-cy='seeValuationButton']")
        self.name_input = page.locator("input[data-cy='nameInput']")
        self.sign_in_button = page.locator("button[data-cy='signInButton']")
        self.phone_input = page.locator("input[data-cy='phoneInput']")

    def enter_more_details(self, personal_details):
        self.email_input_field.fill(personal_details["email"])
        self.sign_in_button.click()
        self.email_input.fill(personal_details["email"])
        self.name_input.fill(personal_details["name"])
        self.phone_input.fill(personal_details["phone"])
        self.see_valuation_button.click()

