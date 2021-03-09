from utilities.Utility import Utility


class Demo3(Utility):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    bmwRadio = "bmwradio"
    benzRadio = "benzradio"
    hondaRadio = "hondaradio"
    mouseHover = "mousehover"

    def RadioButton(self):
        self.clickElement(locator=self.bmwRadio)
        radioBtn = self.driver.find_element_by_id(self.bmwRadio).is_selected()
        self.takeScreenshot()
        return radioBtn

    def MouseHover(self):
        self.moveToElement(locator=self.mouseHover)
        self.takeScreenshot()

"""
        driver.find_element_by_id("benzradio").click()
        time.sleep(1)
        radioBtn = driver.find_element_by_id('benzradio').is_selected()
        print("benzradio:- ", radioBtn)
        assert radioBtn == True

        driver.find_element_by_id("hondaradio").click()
        time.sleep(1)
        radioBtn = driver.find_element_by_id('hondaradio').is_selected()
        print("hondaradio:- ", radioBtn)
        time.sleep(1)
        assert radioBtn == True
"""