import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from frame_demo.hand_black import handle_black


class BasePage:
    black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    # 计数器
    max_num = 3
    error_num = 0

    def __init__(self, driver: WebDriver = None):
        """初始化应用"""
        if driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "True"
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver = driver

    @handle_black
    def find(self, by, locator=None):
        """查找元素"""
        if locator is None:
            # 如果传的元素只有1个，就是by
            result = self.driver.find_element(*by)
        else:
            # 如果传的元素有两个，既有by，又有locator
            result = self.driver.find_element(by, locator)
        return result
        # 捕获黑名单中的元素

    def parse_yaml(self, path, func_name):
        """
        读取yaml,取出关键数据，用parse解析
        """
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        self.parse(data[func_name])

    def parse(self, steps):
        """
        解析yaml内容
        """
        # 遍历每个步骤
        for step in steps:
            # 如果是点击
            if 'click' == step['action']:
                self.find(step['by'], step['locator']).click()
            # 如果是发送内容
            elif 'send' == step['action']:
                self.find(step['by'], step['locator']).send_keys(step['content'])
