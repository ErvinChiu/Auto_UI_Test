# coding: utf-8
from selenium.webdriver.support.select import Select
from selenium import webdriver
import HTMLTestRunnerNew
import unittest
import win32con
import win32gui
from selenium import webdriver
import time
import os
class public_def():

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

class Test_watch_vido(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
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

    # ===================================上传图片===========================
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

    def watch_Replay(self):

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
        # 定位时间进度

        time_test = driver.find_elements_by_class_name("time")[0].text
        print(time_test)
        time.sleep(10)
        time_test01 = driver.find_elements_by_class_name("time")[0].text
        print(time_test01)
        # self.assertEqual(time_test,init_time)
        try:
            assert (time_test == time_test01), 'Test Pass'
        except AssertionError as msg:
            print(msg)
        else:
            print("Test Fail!!!")

        time.sleep(5)

    def DingDan(self):

        self.Login()
        driver = self.driver
        time.sleep(3)
        driver.find_elements_by_class_name("nav_item")[1].click()  # 进入班级课程
        time.sleep(3)
        driver.find_elements_by_class_name("pic")[0].click()
        time.sleep(5)
        # driver.find_elements_by_class_name("el-button sku_buy_btn el-button--primary")[0].click()
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/button').click()
        time.sleep(3)
        driver.find_element_by_xpath(
            '//*[@id="app"]/div[2]/div/div[3]/div[4]/div[4]/label/span[1]/span').click()  # checkbox
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[3]/div[6]/div').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[4]/div/div[3]').click()
        #driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[4]/div/div[1]/div[6]/span').click()  # 选择线下转账
        time.sleep(5)
        ddtext = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/span[1]').text
        ddtext2 = '订单提交成功，请尽快付款！'
        try:
            assert (ddtext == ddtext2), 'Test Fail'
        except AssertionError as msg:
            print(msg)
        else:
            print("Test Pass!!!")

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
    # sub_down.click()
    def Buy_classes(self):
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
        # 获取级别
        # ========级别=======学科========地区=========================
        a = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[7]/div/div[2]/div[1]/span')
        b = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[7]/div/div[2]/div[2]/span')
        c = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[7]/div/div[2]/div[3]/span')
        # 学科
        d = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[1]/span')  # 语文
        e = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[2]/span')  # 数学
        f = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[3]/span')  # 英语
        g = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[4]/span')  # 音乐
        k = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[5]/span')  # 体育
        i = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[6]/span')  # 美术
        l = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[7]/span')  # 物理
        z = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[8]/span')  # 化学
        x = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[9]/span')  # 生物
        v = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[10]/span')  # 政治
        n = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[11]/span')  # 历史
        m = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[12]/span')  # 地理
        pp = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[13]/span')  # 信息技术
        r = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[14]/span')  # 中职
        t = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[15]/span')  # 待定、
        y = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[16]/span')  # 社会
        u = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[17]/span')  # 科学
        s = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[18]/span')  # 心里健康
        j = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[19]/span')  # 小学全科
        o = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[20]/span')  # 幼儿园
        # 地区ea
        area1 = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[9]/div/div[2]/div[1]/span')  # 北京
        area2 = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[9]/div/div[2]/div[2]/span')  # 天津
        area3 = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[9]/div/div[2]/div[3]/span')  # 河北
        area4 = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[9]/div/div[2]/div[4]/span')  # 河南
        area5 = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[9]/div/div[2]/div[8]/span')  # 重庆
        area7 = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[9]/div/div[2]/div[7]/span')  # 四川
        area6 = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[9]/div/div[2]/div[9]/span')  # 江苏
        area8 = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[9]/div/div[2]/div[10]/span') # 浙江
        area9 = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[9]/div/div[2]/div[12]/span') # 安徽
        area10 = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[9]/div/div[2]/div[14]/span')# 全国通用
        area11 = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[9]/div/div[2]/div[15]/span')#上海
        area12 = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[8]/div/div[2]/div[16]/span')# 校园
        #获取级别列表
        jibie=[a,b,c]
        Xuekes=[d, e, f, g, k, i, l, z, x, v, n, m, pp, r, t, y, u, s, j, o]
        areas=[area1, area2, area3, area4, area5, area6, area7, area8, area9, area10, area11, area12]
        # 分别获取级别、班级、地区 状态为True 的元素，并自定义点击选择
        #jb=[]
        #xk=[]
        #area=[]
        try:
            jb = []
            for i in jibie:
                jibies = jibie.pop()
                if jibies.is_enabled():
                    jb.append(jibies)
                    #print(i.text)
                    jdtext=jb[0].text
            print('可选级别:%r'%jdtext)
            jb[0].click()

            xk = []
            for x in Xuekes:
                xueke = Xuekes.pop()
                if xueke.is_enabled():
                    xk.append(xueke)
                    #print(x.text)
                    xktext=xk[0].text
            print('可选学科：%r'%xktext)
            xk[0].click()
            dq = []
            for d in areas:
                area = areas.pop()
                if area.is_enabled():
                    dq.append(area)
                    #print(d.text)

                    dqtext=dq[-1].text
            print("可选地区：%r"%dqtext)
            dq[-1].click()
            print("Test Pass!!")
        except Exception as e:
               print("Exception found",format(e))
    def Buy_classes_two(self):
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
        zftext = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/span[1]').text
        zftext2 = '订单提交成功，请尽快付款！'
        try:
            assert (zftext == zftext2), 'Test Fail'
        except AssertionError as msg:
            print(msg)
        else:
            print("Test Pass!!!")
        """
        while len(Xuekes) > 0:
            xueke = Xuekes.pop()
            if xueke.is_enabled() == True:
                xk.append(xueke)
                if len(xk) == 0:
                    return False
                else:
                    xk[0].click()
                    print("可选择学科：%r" % xk)
                    print(xk[0].text)
                    # return xk
                    # print(xk)
                    # time.sleep()
                   # break

        while len(areas) > 0:

            ar = areas.pop()
            if ar.is_enabled() == True:
                area.append(ar)
                if len(area) == 0:
                    return False
                else:
                    area[-1].click()
                    print("可选择地域：%r" % area)
                    print(area[-1].text)
                    driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/button').click()
                    #break
              """
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    # 构造测试集
    suit = unittest.TestSuite()
    suit.addTest(Test_watch_vido("watch_Replay"))
    suit.addTest(Test_watch_vido("DingDan"))
    suit.addTest(Test_watch_vido("Buy_classes"))
    suit.addTest(Test_watch_vido("Buy_classes_two"))
    # 案例执行
    runner = unittest.TextTestRunner()
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
            title='自动化测试DEMO',
            description ='自动化测试.',
            tester="XiongfeiQiu"
        )
        runner.run(suit)  # 运行测试用例
        tf.close()





