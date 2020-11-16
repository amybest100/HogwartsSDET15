import yaml
from selenium.webdriver.common.by import By

from frame_demo.base_page import BasePage
from frame_demo.market import Market


class Main(BasePage):
    def goto_market(self):
        # 制造假的弹框
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        # self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        # 将数据存储在yaml中
        # with open("./main.yaml", encoding="utf-8") as f:
        #     data = yaml.safe_load(f)
        # steps = data['goto_market']
        # for step in steps:
        #     if 'click'== step['action']:
        #         self.find(step['by'],step['locator']).click()
        self.parse_yaml("main.yaml", "goto_market")

        return Market(self.driver)
