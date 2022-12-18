import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest

from practice_python.HomePage import HomePage
from practice_python.LoginPage import LoginPage


class PimTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        driver = cls.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        driver = cls.driver
        home = HomePage(driver)
        home.click_pim()

    def test_addition_of_employee(self):
        driver = self.driver
        home = HomePage(driver)
        firstname = 'Livinesh'
        lastname = 'sastha'
        home.add_employee(firstname, lastname)
        home.click_save()
        expected_text = firstname + ' ' + lastname
        assert WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//div[@class='orangehrm-edit-employee-name']/h6"), expected_text))

    def test_edit_employee_details(self):
        driver = self.driver
        home = HomePage(driver)
        home.edit_employee()
        license_number = "4567"
        expiry_date = "2024-12-24"
        home.license_details(license_number, expiry_date)
        #home.date_of_birth('1999-11-20')
        home.gender_details()
        home.click_submit()

    def test_delete_employee(self):
        driver = self.driver
        home = HomePage(driver)
        home.employee_delete()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")