from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def open_inventory_page(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    def get_page_heading(self):
        return self.driver.find_element(By.CLASS_NAME, "title").text

    def select_sort_option(self, option):
        dropdown = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        Select(dropdown).select_by_value(option)

    def get_first_product_name(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    def add_backpack_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def get_cart_count(self):
        return self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def get_cart_product_name(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text
