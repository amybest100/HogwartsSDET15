from selenium.webdriver.remote.webdriver import WebDriver

from web.POdemo.index_page import IndexPage


class TestWx:
    def setup(self):
        self.index = IndexPage()
        # self.driver = driver

    # def teardown(self):
    #     self.driver.quit()

    def test_register(self):
        assert self.index.goto_register().register()

        # assert self.index.test_goto_login().test_goto_register().register()
