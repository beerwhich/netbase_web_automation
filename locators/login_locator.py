from selenium.webdriver.common.by import By


class LoginPageLocator:
    ACCOUNT_INPUT_FIELD = (By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    PASSWORD_INPUT_FIELD = (By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="loginForm"]/div/div[3]')
    ERROR_MESSAGE_PARAGRAPH = (By.XPATH, '//*[@id="slfErrorAlert"]')
