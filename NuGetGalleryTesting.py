#Basic testing for NuGet.org

from selenium import webdriver

#Send web driver path as parameter
driver = webdriver.Edge(r"D:\WebDriver\MicrosoftWebDriver.exe")
driver.get("https://www.nuget.org/")

xpaths = {'signinTab': "//*[@href='/users/account/LogOn?returnUrl=%2F']",
          'packagesTab' : "//*[@href='/packages']"
         }

#Get Sign In and click it
driver.find_element_by_xpath(xpaths['signinTab']).click()

