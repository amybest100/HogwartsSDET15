from web.page.main_page import MainPage


class TestAddMember:
    def setup(self):
        self.main = MainPage()

    def test_add_member(self):
        # a = 28
        # b = 154
        # c = 13888888830
        # for i in range(1,15):
        #     a += 1
        #     b += 1
        #     c += 1
        #     username = "Amy"+str(a)
        #     acountId = str(b)
        #     phone = str(c)
        username = "Amy45"
        acountId = "170"
        phone = "13888888846"
        addmember = self.main.goto_addmember()
        addmember.add_member(username, acountId, phone)
        assert True == addmember.get_member(username)
        self.main.goto_index()
