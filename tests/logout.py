from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constant import Constant

class TestLogOut:

    def test_log_out_in_main_page(self, driver, page):
        # Проверка выхода по кнопке «Выйти» в личном кабинете.
        driver.get(Constant.LOGIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.header_log_in_page)))

        driver.find_element(*page.input_email).send_keys(Constant.EMAIL)
        driver.find_element(*page.input_password).send_keys(Constant.PASSWORD)
        driver.find_element(*page.button_log_in).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.button_set_an_order)))
        driver.find_element(*page.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.menu_item_profile)))
        driver.find_element(*page.menu_item_log_in).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.input_email)))
        assert driver.find_element(*page.header_log_in_page)