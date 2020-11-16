from selenium.webdriver.common.by import By

from frame_demo.base_page import BasePage
from frame_demo.search import Search


class Market(BasePage):
    def goto_search(self):
        # self.driver.find_element(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        self.parse_yaml("./market.yaml", "goto_search")
        return Search(self.driver)
