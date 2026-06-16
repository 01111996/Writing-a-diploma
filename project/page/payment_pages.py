from selenium.webdriver.common.by import By
from pages.base_pages import BasePages

class PaymentPages(BasePages):
    CARD_NUMBER = (By.ID, 'cardNumberField')
    EXPIRY_MONTH = (By.ID, 'expiryMonthField')
    EXPIRY_YEAR = (By.ID, 'expiryYearField')
    OWNER_NAME = (By.ID, 'cardOwnerField')
    CVC = (By.ID, 'cvcField')
    PAY_BUTTON = (By.ID, 'submit-payment-btn') 

    def fill_card(self, card_data):
        self.find(self.CARD_NUMBER).send_keys(card_data['number'])
        self.find(self.EXPIRY_MONTH).send_keys(card_data['month'])
        self.find(self.EXPIRY_YEAR).send_keys(card_data['year'])
        self.find(self.OWNER_NAME).send_keys(card_data['owner'])
        self.find(self.CVC).send_keys(card_data['cvc'])

    def pay(self):
        self.find(self.PAY_BUTTON).click()