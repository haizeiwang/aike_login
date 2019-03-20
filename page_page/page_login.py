import page_page
from base_base.base_login import BaseLogin


class PageLogin(BaseLogin):
    # 输入用户名
    def page_username(self, username):
        self.base_input(page_page.login_user, username)

    # 密码
    def page_pwd(self, pwd):
        self.base_input(page_page.login_pwd, pwd)

    # 点击登录
    def page_click(self):
        self.base_click(page_page.login_click)

    # 封装步骤
    def page_login(self, username, pwd):
        self.page_username(username)
        self.page_pwd(pwd)
        self.page_click()
