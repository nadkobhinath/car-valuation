import allure
from pytest_bdd import scenarios, given, when, then, parsers
from pages.home_page import HomePage
from pages.more_details_page import MoreDetailsPage
from pages.results_page import ResultsPage
from utils.file_handler import extract_car_regs, get_vehicle_data_row
from utils.helper import generate_random_email

scenarios("../features/car_evaluation.feature")

@given("the browser is open")
def open_browser(page):
    """Ensure the browser is ready."""
    with allure.step("Open browser"):
        pass

@given(parsers.parse("An input file '{file_name}'"))
def extract_car_reg(file_name: str):
    global car_regs
    car_regs = extract_car_regs(file_name)
    print(f"car regs found: {car_regs}")

@given("Some personal details")
def given_personal_details():
    global user_email
    user_email = generate_random_email()

    global user_details 
    user_details = {
        "email" : user_email,
        "name": "Nad K",
        "phone": "07015585447"
    }
    return user_details

@when(parsers.parse("Searching for a reg number with output file name '{file_name}"))
def searchCarDetails(file_name, config, page):
    """Search for the details with a reg number"""
    global current_vehicle_details
    for car_reg in car_regs:
        with allure.step("Searching for car detals with reg number"):
            page.goto(config["base_url"])
            home_page = HomePage(page)
            home_page.enter_registration("WK20HRC")
            allure.attach(page.screenshot(), name="Car details returned Screenshot", attachment_type=allure.attachment_type.PNG)
            more_details_page = MoreDetailsPage(page)
            more_details_page.enter_more_details(user_details)
            
        with allure.step(f"Collect vehicle details step"):
            results_page = ResultsPage(page)
            current_vehicle_details = results_page.collect_vehicle_details()
            allure.attach(page.screenshot(), name="Results page Screenshot", attachment_type=allure.attachment_type.PNG)

        with allure.step(f"Validation step"):
            results_page = ResultsPage(page)
            expected_vehicle_details_row = get_vehicle_data_row(file_name, car_reg)
            allure.attach(page.screenshot(), name="Vehicle details validation Screenshot", attachment_type=allure.attachment_type.PNG)
            assert expected_vehicle_details_row == current_vehicle_details
           




