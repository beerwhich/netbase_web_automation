import os

# Reward system portal in pre production
INSTAGRAM_LOGIN_PAGE = 'https://www.instagram.com'

# Login account info
ACCOUNT_USERNAME = 'netbasetesting'
ACCOUNT_PASSWORD = 'netbaseP@ssw0rd'
ACCOUNT_PHONE_NUMBER = '0920321322'
ACCOUNT_EMAIL = 'netbasetesting@gmail.com'

LOG_DIR_PATH = os.path.join(os.path.dirname(__file__), '..', 'log')
SCREENSHOTS_DIR_PATH = os.path.join(os.path.dirname(__file__), '..', 'screenshots')

# Default criteria between page to page (seconds)
DEFAULT_TIMEOUT = 4

# Common logger config
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
LOG_MSG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_FILE_DIRECTORY = 'log'
LOG_PROJECT_NAME = "Instagram_login"
LOG_TYPE = "WEB"
LOGFILE_NAME = "automation.web.log"
LOG_IS_STDOUT = True
