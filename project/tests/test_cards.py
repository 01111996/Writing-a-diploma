#•	Покупка тура дебетовой картой: покупатель заходит на сайт, вводит данные карты, 
# оплачивает. (позитивный сценарий)

import pytest
from pages.main_page import MainPage
from pages.base_page import BasePage
from data.cards import APPROVED_CARD, DECLINED_CARD

#Одобрено
def test_payment_with_approved_card(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_buy()
    base_page = BasePage(driver)
    base_page.fill_card(APPROVED_CARD) 
    base_page.pay()
    notification = driver.switch_to.notification
    actual_result = notification.text.split('\n')[0]
    assert 'Успешно' in actual_result

#Отклонено
def test_payment_with_declined_card(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_buy()
    base_page = BasePage(driver)
    base_page.fill_card(DECLINED_CARD)
    base_page.pay()
    notification = driver.switch_to.notification
    actual_result = notification.text.split('\n')[0]
    assert 'Отклонено' in actual_result