from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from time import sleep

sleep(5)

driver = webdriver.Remote('http://selenium:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
driver.get("https://www.python.org/")
driver.save_screenshot("screenshot/python_main_page.png")
print("screenshot from python main page saved")
driver.find_element(By.CSS_SELECTOR, "a[title='Python Package Index']").click()
driver.find_element(By.ID, "search").send_keys("selenium")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
driver.save_screenshot("screenshot/search_results.png")
print("screenshot for selenium search results saved")
