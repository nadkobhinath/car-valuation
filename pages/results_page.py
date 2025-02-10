from pages.base_page import BasePage


class ResultsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.vehicle_make_model = page.locator("h1.VehicleHeader-module__model-zw5I")
        self.vehicla_reg_year = page.locator("ol li:first-child")
        self.vehicle_reg = page.locator("div.VRM-module__vrm-hdeF.VRM-module__small-X7lq.VRM-module__front-BTQb")

    def collect_vehicle_details(self):
        vehicle_details = []
        vehicle_details.append(self.vehicle_reg.text_content)
        vehicle_details.append(self.vehicle_make_model.text_content)
        vehicle_details.append(self.vehicla_reg_year.text_content)
        return vehicle_details

        