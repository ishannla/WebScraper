from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.PhantomJS("/Users/ishannarula/phantomjs/bin/phantomjs")
driver.get("https://www.seedandspark.com/fund/paradise-usa#community")

list = driver.find_elements_by_class_name("supporter-item-container")
for element in list:
    print(element.text)

element = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div/ul/li[6]/div/div[1]/div[2]/a[5]")
element.click()

time.sleep(0.5)
print()
print("1st printed")
print()

list = driver.find_elements_by_class_name("supporter-item-container")
for element in list:
    print(element.text)

print()
print("2nd printed")
print()

# millis1 = time.time()
#
# # driver = webdriver.PhantomJS("/Users/ishannarula/phantomjs/bin/phantomjs")
# driver = webdriver.Chrome("/Users/ishannarula/phantomjs/bin/chromedriver")
# driver.get("https://www.seedandspark.com/fund/paradise-usa#community")
#
# millis2 = time.time()
# print (millis2 - millis1)
#
# millis1 = time.time()
#
# list = driver.find_elements_by_class_name("team-card-module-list")
# for element in list:
#     print(element.text)
#
# millis2 = time.time()
# print (millis2 - millis1)
#
# millis1 = time.time()
#
#
# millis2 = time.time()
# print (millis2 - millis1)
#
# millis1 = time.time()
#
# list = driver.find_elements_by_class_name("supporter-item-container")
# for element in list:
#     print(element.text)
#
# millis2 = time.time()
# print (millis2 - millis1)
#
# print("1st printed")
#
# element = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div/ul/li[6]/div/div[1]/div[2]/a[5]")
# element.click()
#
# wait = WebDriverWait(driver, 10)
# list = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "supporter-item-container")))
#
#
# #list = driver.find_elements_by_class_name("supporter-item-container")
# for element in list:
#     print(element.text)
#
#
#
#
# # list = driver.find_elements_by_xpath("/html/body/div[1]/div[4]/div[2]/div/ul/li[4]/div/div[1]")
# # list = driver.find_elements_by_class_name("team-card-module-list")
# # list = driver.find_elements_by_class_name("update-item")
