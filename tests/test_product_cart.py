from pages.inventory_page import InventoryPage

def test_products_page_opens_after_login(driver):
    page = InventoryPage(driver)
    page.open_inventory_page()

    assert page.get_page_heading() == "Products"


def test_sort_products_by_name_z_to_a(driver):
    page = InventoryPage(driver)
    page.open_inventory_page()
    page.select_sort_option("za")

    # SauceDemo's Z-to-A sort puts Test.allTheThings() T-Shirt (Red) first.
    assert page.get_first_product_name() == "Test.allTheThings() T-Shirt (Red)"


def test_add_backpack_and_verify_cart(driver):
    page = InventoryPage(driver)
    page.open_inventory_page()
    page.add_backpack_to_cart()

    assert page.get_cart_count() == "1"

    page.open_cart()
    assert page.get_cart_product_name() == "Sauce Labs Backpack"
