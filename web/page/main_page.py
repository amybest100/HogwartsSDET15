from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web.page.add_member_page import AddMemberPage
from web.page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self):
    #     options = Options()
    #     options.debugger_address = '127.0.0.1:9222'
    #     self.driver = webdriver.Chrome(options=options)

    def goto_addmember(self):
        # click addmember
        # 在首页点击添加联系人
        # self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        # return AddMemberPage(self.driver)
        # 点击通讯录，再点击添加联系人
        self.find(By.CSS_SELECTOR, "#menu_contacts").click()
        # sleep(3)
        # self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click()
        locator = (By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)")

        # element = self.wait_for_click(locator)
        # element.click()

        # 当点击添加联系人按钮没有跳转页面时，反复点击
        def wait_for_next(x: WebDriver):
            try:
                x.find_element(*locator).click()
                return x.find_element(By.ID, "username")
            except:
                return False

        WebDriverWait(self.driver, 10).until(wait_for_next)

        return AddMemberPage(self.driver)

    def goto_index(self):
        self.find(By.CSS_SELECTOR, ".frame_nav_item_title:nth-child(1)").click()
