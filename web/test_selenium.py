import shelve

import selenium
from selenium import webdriver
from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(5)#隐式等待

    def teardown_method(self, method):
        self.driver.quit()

    # def test_hogwarts(self):
    #     # self.driver.get("https://ceshiren.com")
    #     # self.driver.find_element_by_link_text("所有分类").click()
    #     # #断言
    #     # element=self.driver.find_element_by_link_text("所有分类")
    #     # result=element.get_attribute("class")
    #     # assert 'active'==result
    #     self.driver.get("https://www.baidu.com")
    #     sleep(3)

    # def test_weixin(self):
    #     self.driver.find_element(By.ID,"menu_contacts").click()
    #     sleep(3)

    def test_cookie(self):
        # get_cookies() 可以获取当前打开页面的cookie信息
        # add_cookie() 可以把cookie添加到当前的页面中去
        cookies = self.driver.get_cookies()
        if 'expiry' in cookies:
            del cookies['expiry']
        db = shelve.open("cookies")
        # 将cookie信息存在shelve中
        db['cookie'] = cookies
        db.close()
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # for cookie in cookies:
        #     self.driver.add_cookie(cookie)
        #
        # self.driver.refresh()
        # # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # sleep(3)

    def test_shelve(self):
        # shelve python 内置模块，专门用来对数据进行持久化存储的库，相当于一个小型数据库
        # 可以通过key value 来把数据保存到shelve中
        db = shelve.open("cookies")
        # 将cookie信息存在shelve中
        # db['cookie'] = cookies
        # db.close()
        cookies = db['cookie']
        db.close()
        # 利用读取的cookie完成登录操作
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        sleep(3)

        # 找到导入联系人按钮
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 上传文件
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
            "C:\\Users\\zhaox\\Downloads\\通讯录批量导入模板.xlsx")
        # 验证上传文件名
        filename = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert "通讯录批量导入模板.xlsx" == filename
        sleep(3)
