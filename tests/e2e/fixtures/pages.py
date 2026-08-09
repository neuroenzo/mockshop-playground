from collections.abc import Generator

import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.main_page import MainPage
from support.utils.reports import finalize_tracing, setup_tracing


@pytest.fixture
def prepared_page(request, page: Page) -> Generator[Page, None, None]:
    """Playwright page + tracing + fail attachments (pytest-playwright `page`)."""
    setup_tracing(request, page)
    yield page
    finalize_tracing(request, page)


@pytest.fixture
def ui_login_page(prepared_page: Page) -> LoginPage:
    return LoginPage(page=prepared_page)


@pytest.fixture
def main_page(prepared_page: Page) -> MainPage:
    return MainPage(page=prepared_page)
