#-*-coding:utf-8-*-
#@Time    :2020/11/11 15:04
#@Author  :JS_ErvinChiu
#@Email   :qiuxiongfei@jushiwangedu.com
#@File    :Test_Case.py
#@Software:PyCharm
#from selenium.webdriver.support.select import Select
#from selenium.webdriver.common.keys import Keys

#import win32con
#import win32gui
from selenium import webdriver
from unittestreport import rerun
from unittestreport import TestRunner
import unittest
import time
#import HTML
import os
#import HTMLTestRunnerNew



"""
class public_def():

    #登录开始
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
    """
class Test_JS_Cases(unittest.TestCase):

    @rerun(count=2,interval=5)
    def setUp(self):

        #初始化浏览器会话
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.url = "https://betaweb.jushixl.net.cn/#/home"
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def Login(self):
        # 开始登录
        driver = self.driver
        driver.get(self.url)
        time.sleep(5)
        driver.find_elements_by_class_name("nav_item")[3].click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div/div[1]/div[1]/div').click()
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div/div[2]/div[2]/input').clear()
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div/div[2]/div[2]/input').send_keys("18515817789")
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div/div[2]/div[4]/input').clear()
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div/div[2]/div[4]/input').send_keys("a123456")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div/div[2]/button').click()
        # 结束登录
    """
    #=======================================================上传图片=====================================================
    def upload_chrome(self, filepath):
        # 一级窗口
        dialog = win32gui.FindWindow("#32770", "打开")
        # 二级窗口
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
        # 三级窗口
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
        # 四级窗口--文件路径输入
        edit = win32gui.FindWindowEx(comboBox, 0, "Edit", None)
        # 二级窗口-打开按钮
        button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&0)")
        # 操作--添加发送文件路径
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)
        # 点击打开按钮
        # time.sleep(3)
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        time.sleep(5)
        # file_path = r"D:\PycharmProjects\JS_UIAuto_Test\test_data\001.png"
        # upload_chrome(file_path)
        """
    @rerun(count=2, interval=5)
    #@unittest.skip("测试跳过用例")
    def test_watch_replay(self):

        self.Login()
        driver = self.driver
        time.sleep(3)
        driver.find_elements_by_class_name("nav_item")[2].click()  # 进入我的班级列表
        time.sleep(3)
        driver.find_elements_by_class_name("fast_button")[0].click()  # 进入班级
        time.sleep(5)
        # 选择全部课（默认定位全部课程可省略）
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div/i").click()
        windows_handle = driver.window_handles  # 获取当前所有handles
        driver.switch_to.window(windows_handle[-1])  # 切换到最新窗口
        time.sleep(5)
        driver.switch_to.frame([0][0])  # 切换到frame
        # 定位获取时间进度
        time_test = driver.find_elements_by_class_name("time")[0].text#获取初始时间
        print( "\n初始时间为%r:"%time_test)
        time.sleep(8)
        time_test01 = driver.find_elements_by_class_name("time")[0].text#获取进度时间
        print("进度时间为%r:"%time_test01)
        # self.assertEqual(time_test,init_time)
        try:
            assert (time_test == time_test01), '测试结果：Test Pass!!'
        except AssertionError as msg:
            print(msg)

        else:
            print("测试结果:Test Fail!!!")

    @rerun(count=2, interval=5)
    def test_Order(self):

        self.Login()
        driver = self.driver
        time.sleep(3)
        driver.find_elements_by_class_name("nav_item")[1].click()  # 进入班级课程[1]
        time.sleep(3)
        driver.find_elements_by_class_name("pic")[0].click()
        time.sleep(5)
        # driver.find_elements_by_class_name("el-button sku_buy_btn el-button--primary")[0].click()
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/button').click()
        time.sleep(3)
        driver.find_element_by_xpath(
            '//*[@id="app"]/div[2]/div/div[3]/div[5]/div[4]/label/span[1]/span').click()  # checkbox
        time.sleep(3)
        #driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[3]/div[6]/div').click()#提交订单
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[3]/div[7]/div').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[4]/div/div[3]').click()
        #driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[4]/div/div[1]/div[6]/span').click()  # 选择线下转账（取消功能）
        time.sleep(5)
        ordertext = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/span[1]').text
        ordertext2 = '订单提交成功，请尽快付款！'

        try:
            assert (ordertext == ordertext2), '测试结果：Test Fail'

        except AssertionError as msg:
            print(msg)
        else:
            print("\n%r\n测试结果:Test Pass!!"%ordertext)


        """
        #driver.find_elements_by_class_name("payorder_btn")[0].click()
        ddtext=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]').text()
        ddtext2='订单提交成功，请尽快支付。'
        try:
            assert (ddtext == ddtext2), 'Test Fail'
        except AssertionError as msg:
            print(msg)
        else:
            print("Test Pass!!!")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div/input').send_keys("tester")
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/div').click()  # 上传图片
        # driver.find_elements_by_class_name("el-upload el-upload--picture-card")[0].click()
        time.sleep(3)  # app > div.underlinepay.box > div.underlinepay_body > div:nth-child(4) > div:nth-child(1)
        file_path = (r"D:\PycharmProjects\JS_UIAuto_Test\test_data\001.png")
        self.upload_chrome(file_path)
        time.sleep(8)  # 等待时间略长
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[4]/div[1]').click()  # 提交订单
        time.sleep(10)
        # 判断订单是否已提交，校验弹窗文本
        Text01 = "请耐心等待系统人员审核您提交的凭证哦～"
        # Text02=driver.switch_to_alert()
        Text02 = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div/div[2]').text
        print(Text01)
        print(Text02)
        try:
            assert (Text01 == Text02), 'Test Fail！！'
        except AssertionError as msg:
            print(msg)
        else:
            print("Test Pass!!!")
        """
    # 判断是否已经选中
    """
        selected = check_box.is_selected()
        if selected:
            print("it's select")
        else:
            print("")
            check_box
    """
    #@rerun(count=2, interval=20)
    @unittest.skip("演示跳过用例")
    def test_Buy_classes_one(self):
        self.Login()
        driver = self.driver
        time.sleep(3)
        # 进入班级课程
        driver.find_elements_by_class_name("nav_item")[1].click()
        time.sleep(3)
        # 选择幼儿
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[1]/div[2]/span[4]').click()
        time.sleep(5)
        # 选择课程
        driver.find_elements_by_class_name("intro")[0].click()
        #time.sleep(5)
        #driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[7]/div/div[2]/div[1]/span').click()  # 选择中学
        # time.sleep(3)
        # driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[1]/span').click()
        # driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[9]/div/div[2]/div[1]/span').click()
        # time.sleep(5)
        # tj = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/button')

        # dis1=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[3]/span')
        # print(dis1.is_displayed())
        # a = driver.find_elements_by_class_name("norms_item norms_item_enable")
       
    #@unittest.skip("验证邮件")
    @rerun(count=1, interval=30)
    def test_Buy_classes_two(self):
        self.Login()
        driver = self.driver
        time.sleep(3)
        # 进入班级课程
        driver.find_elements_by_class_name("nav_item")[1].click()
        #time.sleep(3)
        # 选择幼儿
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[1]/div[2]/span[4]').click()
        time.sleep(5)
        # 选择课程
        driver.find_elements_by_class_name("intro")[0].click()
        time.sleep(5)
        #提交
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/button/span').click()
        time.sleep(8)
        #勾选服务协议
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[3]/div[5]/div[4]/label/span[1]/span').click()
        #提交订单
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[3]/div[7]/div').click()
        time.sleep(3)
        #跳转第三方支付
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[4]/div/div[3]').click()
        Paytext = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/span[1]').text
        Paytext2 = '订单提交成功，请尽快付款！'
        try:
            assert (Paytext == Paytext2), '测试结果：Test Fail!!!'

        except AssertionError as msg:
            print(msg)

        else:
            print("\n%r\n测试结果:Test Pass!!!"%Paytext)

    def tearDown(self):

        self.driver.quit()

#添加测试用例类
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test_JS_Cases)
#生成测试报告
runner = TestRunner(suite=suite)
#runner.run()
runner.rerun_run(count=1, interval=5)
runner.send_email(host="smtp.qq.com",
                  port=465,
                  user="2551451515@qq.com",
                  password="boqvynjdduztecgj",
                  to_addrs="qiuxiongfei@jushiwangedu.com")

"""
if __name__ == "__main__":
    # 构造测试集
    suit = unittest.TestSuite()
    suit.addTest(Test_JS_Cases("Test_watch_Replay"))
    #suit.addTest(Test_JS_Cases("Test_Order"))
    #suit.addTest(Test_JS_Cases("Test_Buy_classes_one"))
    #suit.addTest(Test_JS_Cases("Test_Buy_classes_two"))
    # 案例执行
    #runner = unittest.TestRunner(suite=suit)


    # 报告保存路径
    # 报告路径

    date_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    report_abspath = date_time + '.html'
    Re_local = 'D:\PycharmProjects\JS_UIAuto_Test\Test_Report\Test_Report'
    report_local = Re_local + report_abspath
    # 定义测试报告
   
    with open(report_local, 'wb+') as tf:
            runner = HTMLTestRunnerNew.HTMLTestRunner(
                tf,
                2,
                title = '聚师网UI自动化测试',
                description = '自动化测试报告',
                tester="XiongfeiQiu"
                )
            runner.run(suit)  # 运行测试用例
            tf.close()

    with open(report_local, 'wb+') as tf:
        runner = HTMLTestRunnerNew.HTMLTestRunner(
            tf,
            2,
            title='聚师网UI自动化测试',
            description='自动化测试报告',
            tester="XiongfeiQiu"
        )
        runner.run(suit)  # 运行测试用例
        tf.close()
"""

