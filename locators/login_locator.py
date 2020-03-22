from selenium.webdriver.common.by import By


class LoginPageLocator:
    ACCOUNT_INPUT_FIELD = (By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
    PASSWORD_INPUT_FIELD = (By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
    ERROR_MESSAGE_PARAGRAPH = (By.XPATH, '//*[@id="slfErrorAlert"]')
