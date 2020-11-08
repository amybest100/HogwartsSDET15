from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.page.base_page import BasePage


class AddMemberPage(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver=driver

    # 添加联系人
    def add_member(self, username, acountId, phone):
        # 显式等待
        checkbox = (By.CSS_SELECTOR, ".ww_checkbox")
        self.wait_for_click1(checkbox)
        # sleep(4)
        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(acountId)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        # sleep(4)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        sleep(4)
        return True

    # 检查是否添加成功
    def get_member(self, value):
        # contactlist = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        # titlelist = [element.get_attribute("title") for element in contactlist]
        # print(titlelist)
        # titlelist=[]
        # for element in contactlist:
        #     titlelist.append(contactlist.get_attribute("title"))

        total_list = []
        while True:
            contactlist = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
            titlelist = [element.get_attribute("title") for element in contactlist]
            print(titlelist)
            if value in titlelist:
                return True
            total_list = total_list + titlelist

            result: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            num, total = result.split('/', 1)
            if int(num) == int(total):
                return False
            else:
                self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()
        return total_list
