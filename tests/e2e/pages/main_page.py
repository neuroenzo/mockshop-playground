import allure

from components.navbar_component import NavbarComponent
from pages.base_page import BasePage
from playwright.sync_api import Page


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.home_page_hero = page.get_by_test_id('home-page')

    @allure.step('Check user with "{expected_email}" login')
    def should_be_logged_in(self, expected_email: str) -> None:
        self.navbar.should_have_email(expected_email)
        self.navbar.should_have_enabled_logout_button()

    @allure.step('Click logout button')
    def click_logout(self) -> None:
        self.navbar.click_logout()
