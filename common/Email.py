#config=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import HTMLTestRunnerNew
import unittest
import time
import os
from Test_case.Test_kangke import *

#邮件发送
def send_mail(Auto_UI_report):
    Reports=open(Auto_UI_report,'rb')
    maii_body=Reports.read()
    Reports.close()
    Msg=MIMEText(maii_body,'html','utf-8')
    Msg['Subject']=Header("UI自动化测试报告","utf-8")
    stmp=smtplib.SMTP()

    stmp.connect("stmp.126.com")
    stmp.login("username","123456")
    #邮件发送
    stmp.sendmail("123@126.com","456@126.com",Msg.as_string())
    stmp.quit()
    print("邮件已经发出！")

    #查找邮件报告目录，获取最新生成的测试报告文件
def test_report_new(Testreport):
    lists=os.listdir(Testreport)
    lists.sort(key=lambda fn: os.path.getmtime(Testreport + '\\' + fn))
    Auto_UI_report=os.path.join(Testreport,lists[-1])
    print(Auto_UI_report)
    return Auto_UI_report

if __name__ == "__main__":
    testcase_dir = "D:\PycharmProjects\JS_UIAuto_Test\Test_case"
    restreport="D:\PycharmProjects\JS_UIAuto_Test\Test_Report"
    discover=unittest.defaultTestLoader.discover(testcase_dir,pattern='test_*.py')
    # 报告路径
    date_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    report_abspath = 'report_' + date_time + '.html'
    Re_local = 'D:\PycharmProjects\JS_UIAuto_Test\Test_Report\Test_Report'
    report_local = Re_local + date_time + report_abspath
    # 定义测试报告
    with open(report_local, 'wb+') as rf:
        runner = HTMLTestRunnerNew.HTMLTestRunner(
            rf,
            2,
            title='自动化测试DEMO',
            description='自动化测试.',
            tester="XiongfeiQiu"
        )

        runner.run(discover)  # 运行测试用例
        rf.close()
