from pages.base_page import BasePage
from pages.cookies_banner import CookiesBanner

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cookies_banner = CookiesBanner(page)
        self.registration_input = page.locator("input#vrm-input") 
        self.submit_reg_button = page.locator("button[data-cy='valueButton']")
        self.submit_milage_button = page.locator("button[data-cy='continueButton']")

    def enter_registration(self, reg_number: str):
        self.registration_input.fill(reg_number)
        self.submit_reg_button.click()
        self.submit_milage_button.click()        
