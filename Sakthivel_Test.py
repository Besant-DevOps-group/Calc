import Sakthivel as fileData
from selenium.webdriver.common.by import By

# Get Value using XPATH
textValue = fileData.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[1]/div[2]/div/div/div[2]/h1/span").text
# print(textValue)

# Compare value using Assertion method
assert textValue == "Let’s build from here"
print("Validated....")
fileData.driver.quit()