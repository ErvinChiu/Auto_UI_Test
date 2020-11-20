#-*-coding:utf-8-*-
#@Time    :2020/11/20 11:25
#@Author  :JS_ErvinChiu
#@Email   :qiuxiongfei@jushiwangedu.com
#@File    :SendEmail.py
#@Software:PyCharm
import unittest

from unittestreport import ddt,list_data
@ddt
class TestClass(unittest.TestCase):
    cases = [{'title': '用例1', 'data': '用例参数', 'expected': '预期结果'},
             {'title': '用例2', 'data': '用例参数', 'expected': '预期结果'},
             {'title': '用例3', 'data': '用例参数', 'expected': '预期结果'}]
    @list_data(cases)
    def test_case(self, data):
        print(data)