import unittest
from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By
import pyautogui as pg#鼠标移动输入
import os
import random

class MyTestCase(unittest.TestCase):


    def setUp(self) -> None:

        self.dr = Chrome()
        self.dr.maximize_window()
        self.dr.get("http://192.168.190.17/ ")
        self.dr.implicitly_wait(30)
        self.dr.find_element(By.XPATH,"//*[@id='username']").send_keys("admin")
        self.dr.find_element(By.XPATH, "//*[@id='password']").send_keys("admin123")
        self.dr.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/form/button/span").click()
        self.dr.find_element(By.XPATH, "//*[@id='root']/div/section/aside/div/div[2]/ul/li[1]/div/span/span/span[2]").click()
        time.sleep(3)


    def tearDown(self) -> None:

        self.dr.quit()

    def test_SystemSetup(self):#系统设置
        seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sa = []
        for i in range(4):
            sa.append(random.choice(seed))
        salt = ''.join(sa)
        self.dr.find_element_by_link_text("banner").click()#banner
        self.dr.find_element(By.XPATH," // *[ @ id = 'root'] / div / section / div[2] / main / div / div / div[1] / button / span").click()
        self.dr.find_element(By.XPATH,"//*[@id='validate_other_name']").send_keys(f"{salt}")
        self.dr.find_element(By.XPATH, "//*[@id='validate_other_url']").send_keys("baidu.com")
        time.sleep(3)
        self.dr.find_element(By.XPATH,'//*[@id="validate_other"]/div[3]/div[2]/div[1]/div/span/div/div/span/button/span[2]').click()
        time.sleep(5)
        os.system(r"D:\tupian\shangchuan.exe")
        time.sleep(10)
        pg.moveTo(1212, 662)
        pg.click()

    def test_AccountSettings(self):
        seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sa = []
        for i in range(4):
            sa.append(random.choice(seed))
        salt = ''.join(sa)
        self.dr.find_element_by_link_text("账号设置").click()#账号设置
        time.sleep(3)
        pg.moveTo(1830, 284)
        pg.click()
        self.dr.find_element(By.XPATH, "//*[@id='validate_other_nickName']").send_keys(f"{salt}")
        self.dr.find_element(By.XPATH, "//*[@id='validate_other_password']").send_keys("123456")
        time.sleep(3)
        pg.moveTo(1010, 466)
        pg.click()
        time.sleep(3)
        pg.moveTo(1022, 527)
        pg.click()
        time.sleep(3)
        pg.moveTo(1207, 557)
        pg.click()

    def test_TheArticleSet(self):#文章设置
        seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sa = []
        for i in range(4):
            sa.append(random.choice(seed))
        salt = ''.join(sa)
        self.dr.find_element_by_link_text("文章设置").click()
        self.dr.find_element(By.XPATH, "//*[@id='root']/div/section/div[2]/main/div/div/div[1]/button/span").click()
        self.dr.find_element(By.XPATH, "//*[@id='validate_other_title']").send_keys(f"{salt}")
        time.sleep(3)
        pg.moveTo(652,488)
        pg.click()
        pg.write("65465",interval=1)
        time.sleep(2)

        self.dr.find_element(By.XPATH, "//*[@id='validate_other_id']/span").click()


if __name__ == '__main__':
    unittest.main()
