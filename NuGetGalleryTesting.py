#Basic testing for NuGet.org

from selenium import webdriver
from selenium.webdriver.common.by import By


#Send web driver path as parameter
driver = webdriver.Edge(r"D:\WebDriver\MicrosoftWebDriver.exe")
driver.get("https://www.nuget.org/")

xpaths = {'signinTab': "//*[@href='/users/account/LogOn?returnUrl=%2F']",
          'packagesTab' : "//*[@href='/packages']",
         'signinButton': "//section[@role='main']"
          }

#Get Sign In and click it
driver.find_element_by_xpath(xpaths['signinTab']).click()


# Verify in sign page
# driver.find_element_by_xpath(xpaths['signinButton'])
# driver.find_element_by_tag_name("section")
driver.find_element(By.TAG_NAME, "section")

