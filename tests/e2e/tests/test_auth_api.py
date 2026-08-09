import pytest

from config import AuthConfig
from pages.main_page import MainPage


@pytest.mark.e2e
@pytest.mark.authorization
class TestAuthAPI:
    def test_admin(self, admin: MainPage, env_config: AuthConfig) -> None:
        admin.should_be_logged_in(env_config.admin_email)

    def test_buyer(self, buyer: MainPage, env_config: AuthConfig) -> None:
        buyer.should_be_logged_in(env_config.buyer_email)

    def test_seller(self, seller: MainPage, env_config: AuthConfig) -> None:
        seller.should_be_logged_in(env_config.seller_email)
