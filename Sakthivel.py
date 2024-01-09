from selenium import webdriver
# import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
capabilities = {'pageLoadStrategy': 'normal', 'pageLoadTimeout': 60000}  # Set timeout in milliseconds
executable_path = "drivers/chromedriver.exe"
driver = webdriver.Chrome(service=Service("drivers/chromedriver.exe"), options=options, service_args=['--verbose', '--log-path=/path/to/chromedriver.log'])


# driver = webdriver.Chrome()
# executable_path = "drivers/chromedriver.exe"
# driver = webdriver.Chrome(service=Service(executable_path))
# executable_path = chromedriver_autoinstaller.install()
# driver = webdriver.Chrome(service=Service(executable_path))
# driver =webdriver.Firefox()
driver.maximize_window()

driver.get("https://github.com/")
print("Successfully redirected")
