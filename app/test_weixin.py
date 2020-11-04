from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWeixin:
    def setup(self):
        disired_caps = {
            "platformName": "android",
            "platformversion": "10",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset": "true",
            # "dontStopAppOnReset": "true",
            "skipDeviceInitialization": "true",
            "unicodeKeyBoard": "true",
            "resetKeyBoard": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", disired_caps)
        self.driver.implicitly_wait(6)

    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text=‘工作台’]").click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("工作台")').click()
        # 滚动查找元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("打卡").instance(0));').click()
        self.driver.update_settings({"waitForIdleTimeout": 0})
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡']").click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("外出打卡")').click()
        # self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'次外出')]").click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("次外出")').click()
        # 检查点
        # assert "外出打卡成功" in self.driver.page_source
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)


if __name__ == '__main__':
    pytest.main('test_weixin.py')
