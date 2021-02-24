from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

sleep(5)

driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
driver.get("https://www.clicktrans.pl/")
driver.save_screenshot("screenshot_main_page.png")
print("screenshot saved from Clicktrans main page")
driver.get("https://clicktrans.pl/przegladaj-przesylki/")
driver.save_screenshot("screenshot_search_page.png")
print("screenshot saved from Clicktrans search auction page")
driver.get("https://clicktrans.pl/info/o-nas")
driver.save_screenshot("screenshot_about_page.png")
print("screenshot saved from Clicktrans about us page")