from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service


executable_path = chromedriver_autoinstaller.install()
driver = webdriver.Chrome(service=Service(executable_path))
driver.maximize_window()

driver.get("https://github.com/")
print("Successfully redirected")
