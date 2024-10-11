from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constant import Constant

class TestTransitAccountPage:
    def test_transit_to_account_page(self, driver, page):
        # Проверка перехода по клику на «Личный кабинет».
        driver.get(Constant.MAIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.button_log_in_account)))
        driver.find_element(*page.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.button_log_in)))
        assert driver.find_element(*page.header_log_in_page)

    def test_transit_to_constructor_from_account_page(self, driver, page):
        # Проверка перехода из личного кабинета в конструктор по клику на «Конструктоо».
        driver.get(Constant.LOGIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.header_log_in_page)))
        driver.find_element(*page.input_email).send_keys(Constant.EMAIL)
        driver.find_element(*page.input_password).send_keys(Constant.PASSWORD)
        driver.find_element(*page.button_log_in).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.button_personal_account)))
        driver.find_element(*page.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.menu_item_profile)))
        driver.find_element(*page.main_header_constructor).click()
        assert driver.find_element(*page.header_constructor)
        assert Constant.MAIN_PAGE == driver.current_url

    def test_tap_logo_transfer_to_constructor_from_account_page(self, driver, page):
        # Проверка перехода из личного кабинета в конструктор по клику на логотип сайта
        driver.get(Constant.LOGIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.header_log_in_page)))
        driver.find_element(*page.input_email).send_keys(Constant.EMAIL)
        driver.find_element(*page.input_password).send_keys(Constant.PASSWORD)
        driver.find_element(*page.button_log_in).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((page.button_personal_account)))
        driver.find_element(*page.logo_main_page).click()
        assert driver.find_element(*page.header_constructor)
        assert Constant.MAIN_PAGE == driver.current_url