from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome Browser
#----------------------------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
executable_path = chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service(executable_path),options=chrome_options)

# Firefox Browser
#---------------------------------
# firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument("--headless")
# driver = webdriver.Firefox(options=firefox_options)

# Maximize browser
driver.maximize_window()

# Redirect the link
driver.get("https://github.com/")
print("Successfully redirected")
