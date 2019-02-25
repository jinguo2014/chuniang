# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Jingdong(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.jd.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_jingdong(self):
        driver = self.driver
        driver.get(self.base_url + "/")

        js = "window.scrollTo(0,600);"
        driver.execute_script(js)

        time.sleep(10)

        driver.find_element_by_xpath(u"//img[@alt='小米(MI)Pro 15.6英寸金属轻薄笔记本(i5-8250U 8G 256GSSD MX150 2G独显 FHD 指纹识别 预装office)深空灰']").click()

        time.sleep(20)

        # 获取当前浏览器所有的窗口
        w_h_s = driver.window_handles
        # 让程序聚焦在第二个窗口
        driver.switch_to.window(w_h_s[1])

        time.sleep(10)

        driver.find_element_by_css_selector("img.seckill_mod_goods_link_img").click()

        time.sleep(10)

        # 获取当前浏览器所有的窗口
        w_h_s = driver.window_handles
        # 让程序聚焦在第二个窗口
        driver.switch_to.window(w_h_s[2])

        js = "window.scrollTo(0,600);"
        driver.execute_script(js)

        time.sleep(20)
        driver.find_element_by_css_selector("div.tab-main.large > ul > li.current").click()

        time.sleep(10)
        # 选择颜色
        driver.find_element_by_xpath("//div[@id='choose-attr-1']/div[2]/div[4]/a/i").click()

        time.sleep(10)
        js = "window.scrollTo(0,600);"
        driver.execute_script(js)

        #延长保一年
        driver.find_element_by_xpath(".//*[@id='choose-service']/div[2]/div/div[2]/div[1]/span[1]").click()
        time.sleep(10)

        # 添加数量
        driver.find_element_by_link_text("+").click()
        time.sleep(10)

        # 加入购物车
        driver.find_element_by_id("InitCartUrl").click()

        time.sleep(10)

        # 去购物车结算
        driver.find_element_by_id("GotoShoppingCart").click()
        time.sleep(10)


    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
