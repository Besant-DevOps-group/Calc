from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service



driver = webdriver.Chrome()
# executable_path = "drivers/chromedriver.exe"
# driver = webdriver.Chrome(service=Service(executable_path))
# executable_path = chromedriver_autoinstaller.install()
# driver = webdriver.Chrome(service=Service(executable_path))
# driver =webdriver.Firefox()
driver.maximize_window()

driver.get("https://github.com/")
print("Successfully redirected")
