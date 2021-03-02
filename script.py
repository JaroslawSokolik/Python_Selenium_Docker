from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

sleep(5)

driver = webdriver.Remote('http://selenium-hub:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
driver.get("https://www.python.org/")
driver.save_screenshot("python_main_page.png")
print("screenshot from python main page saved")
driver.find_element_by_css_selector("a[title='Python Package Index']").click()
driver.find_element_by_id("search").send_keys("selenium")
driver.find_element_by_css_selector("button[type='submit']").click()
driver.save_screenshot("search results.png")
print("screenshot for selenium search results saved")
