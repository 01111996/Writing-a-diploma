#•	Покупка кредита: покупатель заходит на сайт, 
# оформляет тур в кредит. (позитивный сценарий)

import pytest
from pages.main_pages import MainPages
from pages.base_pages import BasePages
from pages.payment_pages import PaymentPages
from data.cards import APPROVED_CARD

def test_credit(driver):
    driver.get("http://localhost:8080")
    main_pages = MainPage(driver)
    main_pages.click_credit()

    base_pages = PaymentPages(driver)
    base_pages.fill_card_data(APPROVED_CARD)
    base_pages.submit()

    assert "Одобрено" in driver.page_source