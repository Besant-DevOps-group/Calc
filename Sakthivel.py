import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

# ----- Chrome Browser --------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
executable_path = chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service(executable_path),options=chrome_options)

# -------- Firefox Browser ---------
# firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument("--headless")
# driver = webdriver.Firefox(options=firefox_options)

# Maximise Window
driver.maximize_window()

driver.get("https://github.com/")
print("Successfully redirected")
