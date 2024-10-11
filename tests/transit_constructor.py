from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constant import Constant

class TestTransitSection:

    def test_open_sauce_section(self, driver, page):
        #переход к разделу «Соусы» в конструкторе:
        driver.get(Constant.MAIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.button_log_in_account))
        driver.find_element(*page.sauce_constructor).click()
        assert driver.find_element(*page.select_tab_constructor).text == 'Соусы'

    def test_open_filling_section(self, driver, page):
        #переход к разделу «Начинки» в конструкторе:
        driver.get(Constant.MAIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.button_log_in_account))
        driver.find_element(*page.filling_constructor).click()
        assert driver.find_element(*page.select_tab_constructor).text == 'Начинки'

    def test_open_bread_section(self, driver, page):
        #переход к разделу «Булки» в конструкторе:
        driver.get(Constant.MAIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.button_log_in_account))
        #Раздел «Булки» при заходе на сайт выбраны по дефолту, поэтому я выбираю другую категорию, чтобы проверить переход к «Булкам»
        driver.find_element(*page.filling_constructor).click()
        assert driver.find_element(*page.select_tab_constructor).text == 'Начинки'
        driver.find_element(*page.bread_constructor).click()
        assert driver.find_element(*page.select_tab_constructor).text == 'Булки'
