import logging
from page.Demo3PageObject import Demo3
from utilities.BaseClass import BaseClass
from utilities.logger import customLogger


class TestDemo3(BaseClass):
    log = customLogger(logLevel=logging.DEBUG)

    def test_ValidateRadio(self):
        demo = Demo3(self.driver)
        self.log.info("Validate Radio test")
        assert demo.RadioButton() == True

    def test_Scrolling(self):
        demo = Demo3(self.driver)
        self.log.info("Scrolling test")
        demo.MouseHover()

    def test_Scroll(self):
        demo = Demo3(self.driver)
        self.log.info("Scrolling test")
        demo.MouseHover()
