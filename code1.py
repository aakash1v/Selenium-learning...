from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.selenium.dev/")
title = driver.title
print(title)

assert "Selenium" in title
abc = driver.find_element(By.XPATH,
                    "/html/body/div/main/section[2]/div/div/div[1]/div/div[1]/h4")
print(abc)

