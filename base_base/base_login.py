from selenium.webdriver.support.wait import WebDriverWait


class BaseLogin:
    def __init__(self, driver):
        self.driver = driver

    # 定位查找
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda d: d.find_element(*loc))

    # 点击
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)
