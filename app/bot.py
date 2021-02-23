from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

sleep(5)

driver = webdriver.Remote('http://selenium:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
driver.get("https://www.python.org/")
driver.save_screenshot("screenshot.png")
print("screenshot saved from python.org")
driver.get("https://www.wp.pl/")
print("screenshot saved from wp.pl")
driver.get("https://www.onet.pl/")
print("screenshot saved from onet.pl")