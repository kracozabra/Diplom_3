import allure
from pages.base_page import BasePage
from pages.forgot_password_page import ForgotPasswordPage
import locators


class ResetPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем страницу восстановления пароля')
    def open_reset_password_url(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_forgot_password_url()
        forgot_password_page.click_forgot_password_button()
        self.wait_for_load_reset_password_page()

    @allure.step('Ожидаем загрузку страницы "Восстановить пароль"')
    def wait_for_load_reset_password_page(self):
        self.wait_for_element_visible(locators.RESET_PASSWORD_ENTER_CODE_FIELD)

    @allure.step('Кликаем на иконку "Показать пароль')
    def click_show_password_password_button(self):
        self.click_element(locators.RESET_PASSWORD_SHOW_PASSWORD_ICON)

    @allure.step('Кликаем на кнопку "Сохранить')
    def click_reset_password_button(self):
        self.click_element(locators.RESET_PASSWORD_SAVE_BUTTON)

    @allure.step('Ожидаем, пока поле "Пароль" перейдет в активное состояние')
    def wait_for_password_field_active(self):
        self.wait_for_element_visible(locators.RESET_PASSWORD_ENTER_CODE_FIELD)

    @allure.step('Проверяем, что поле "Пароль" находится в активном состоянии')
    def check_password_field_active(self):
        return self.element_is_present(locators.RESET_PASSWORD_ENTER_CODE_FIELD)
