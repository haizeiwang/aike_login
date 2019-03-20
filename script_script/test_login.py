import os
import sys
sys.path.append(os.getcwd())

import pytest
import yaml


from base_base.get_driver import GetDriver
from page_page.page_login import PageLogin

def get_data():
    with open("./data/data_login.yaml", "r", encoding="utf-8") as i:
        data = yaml.load(i)
        list = []
        for data in data.values():
            list.append((data.get("username"), data.get("pwd")))
        return list

class TestLogin():
    def setup_class(self):
        self.driver = GetDriver()
        self.login = PageLogin(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("username,pwd",get_data())
    def test_login(self, username, pwd):
        self.login.page_login(username, pwd)
