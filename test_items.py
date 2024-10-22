from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_add_to_cart_exists(browser):
    browser.get(link)
    add_to_cart_buttons = browser.find_elements(
        By.CSS_SELECTOR, 'button.btn-add-to-basket')
    assert len(add_to_cart_buttons) > 0, \
        f'Button does not exist'
