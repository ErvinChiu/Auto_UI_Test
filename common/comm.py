from selenium import webdriver
import time
class public_def:
    def login(self):
        driver = webdriver.Chrome()
        driver.get("https://betaweb.jushixl.net.cn/#/home")
        driver.implicitly_wait(10)
        driver.maximize_window()
        time.sleep(5)
        driver.find_elements_by_class_name("nav_item")[3].click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div/div[1]/div[1]/div').click()
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div/div[2]/div[2]/input').send_keys("18515817789")
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div/div[2]/div[4]/input').send_keys("a123456")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div/div[2]/button').click()
     # 登录结束
