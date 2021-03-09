import logging
import time

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import customLogger


class Utility:
    log = customLogger(logLevel=logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'class':
            return By.CLASS_NAME
        elif locatorType == 'link':
            return By.LINK_TEXT
        elif locatorType == 'plink':
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.info("Locator type"+ locatorType +" is not correct / supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element is found with locator: " + locator + " and locator Type:" +locatorType)
        except:
            self.log.info("Element is not found with locator: " + locator + " and locator Type:" +locatorType)
        return element

    def clickElement(self, locator, locatorType="id"):
        try:
            self.waitForElementToClickable(locator, locatorType)
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Element is clicked")
        except:
            self.log.info("Element is not clicked with locator:"+locator+" and locator type:"+locatorType)

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data '"+data+"' on element with locator :"+locator+ " and locator type :"+locatorType)
        except:
            self.log.info("Can not sent data '"+data+"' on element with locator :"+locator+ " and locator type :"+locatorType)

    def waitForElementToClickable(self, locator, locatorType="id", timeOut=60, pollingFre=2):
        byType = self.getByType(locatorType)
        wait = WebDriverWait(self.driver, timeout=timeOut, poll_frequency=pollingFre, ignored_exceptions=
        [NoSuchElementException, ElementNotVisibleException])
        wait.until(EC.element_to_be_clickable((byType, locator)))

    def moveToElement(self, locator, locatorType="id"):
        element = self.getElement(locator, locatorType)
        try:
            action = ActionChains(self.driver)
            self.log.info("Move to element is working in Try block")
            action.move_to_element(element).perform()
        except:
            self.log.info("Move to element is working in Except block")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def takeScreenshot(self):
        fileName = str(round(time.time() * 1000 )) + ".png"
        screenshotDirectory = r"C:\Users\gktom\Desktop\test"
        name = screenshotDirectory + "\\" +fileName
        self.driver.save_screenshot(name)

        """try:
            self.driver.save_screenshot(name)
        except NotADirectoryError:
            self.log.error("Directory is not available")"""


