from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.pim_button_xpath = "//span[text()='PIM']"
        self.add_button_xpath = "//button[text()=' Add ']"
        self.firstname_textbox_name = "firstName"
        self.lastname_textbox_name = "lastName"
        self.save_button_xpath = "//button[@type='submit']"
        self.edit_button_xpath = "//div[text() = '0212']//../following-sibling::div/div/button/i[@class='oxd-icon bi-pencil-fill']"
        self.license_number_xpath = "//label[contains(text(), 'License Number')]//../following-sibling::div/input"
        self.license_expiry_date_xpath = "//label[contains(text(), 'License Expiry Date')]//../following-sibling::div/div/div/input"
        self.date_of_birth = "//label[contains(text(), 'Date of Birth')]//../following-sibling::div/div/div/input"
        self.gender_choose_xpath = "//input[@type = 'radio' and @value = '1']"
        self.submit_button_xpath = "//p[text() = ' * Required']/following-sibling::button"
        self.delete_button_xpath = "//div[text()='0217']//..//../div/div/button/i[@class='oxd-icon bi-trash']//.."
        self.accept_button_xpath = "// div[ @class ='orangehrm-modal-footer'] / button[@ class ='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']"

    def click_pim(self):
        self.driver.find_element(By.XPATH, self.pim_button_xpath).click()

    def add_employee(self, firstname, lastname):
        self.driver.find_element(By.XPATH, self.add_button_xpath).click()
        self.driver.find_element(By.NAME, self.firstname_textbox_name).clear()
        self.driver.find_element(By.NAME, self.firstname_textbox_name).send_keys(firstname)
        self.driver.find_element(By.NAME, self.lastname_textbox_name).clear()
        self.driver.find_element(By.NAME, self.lastname_textbox_name).send_keys(lastname)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

    def edit_employee(self):
        self.driver.find_element(By.XPATH, self.edit_button_xpath).click()

    def license_details(self, license_number, expiry_date):
        my_actions = ActionChains(self.driver)
        element1 = self.driver.find_element(By.XPATH, self.license_number_xpath)
        my_actions.move_to_element(element1).click(element1).send_keys(license_number).perform()
        #self.driver.find_element(By.XPATH, self.license_number_xpath).clear()
        #element11 = self.driver.find_element(By.XPATH, self.license_number_xpath)
        element2 = self.driver.find_element(By.XPATH, self.license_expiry_date_xpath)
        my_actions.move_to_element(element2).click(element2).send_keys(expiry_date).perform()
        #self.driver.find_element(By.XPATH, self.license_expiry_date_xpath).clear()
        #self.driver.find_element(By.XPATH, self.license_expiry_date_xpath).send_keys(expiry_date)

    def date_of_birth(self, dob):
        my_actions = ActionChains(self.driver)
        birth = self.driver.find_element(By.XPATH, self.date_of_birth)
        my_actions.move_to_element(birth).click(birth).clear().send_keys(dob).perform()
        #self.driver.find_element(By.XPATH, self.date_of_birth).clear()
        #self.driver.find_element(By.XPATH, self.date_of_birth).send_keys(dob)

    def gender_details(self):
        my_actions = ActionChains(self.driver)
        gen = self.driver.find_element(By.XPATH, self.gender_choose_xpath)
        my_actions.move_to_element(gen).click(gen).perform()

    def click_submit(self):
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()

    def employee_delete(self):
        my_actions = ActionChains(self.driver)
        delete = self.driver.find_element(By.XPATH, self.delete_button_xpath)
        my_actions.move_to_element(delete).click().perform()
        accept = self.driver.find_element(By.XPATH, self.accept_button_xpath)
        my_actions.move_to_element(accept).click().perform()

