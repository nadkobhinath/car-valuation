from playwright.async_api import Page

class CookiesBanner:
    def __init__(self, page: Page):
        self.page = page
        self.accept_button = page.locator("text=Accept all cookies")

    def accept_cookies_if_present(self):
        self.accept_button.wait_for(timeout=5000)
        if self.accept_button.is_visible():
            self.accept_button.click()
            print("Clicked Accept all cookies button")
        else:
            print("Accept all cookies button not found")
