import unittest
from unittestreport import TestRunner
from Test_Case import Test_JS_Cases
suite=unittest.defaultTestLoader.loadTestsFromTestCase(Test_JS_Cases)
runner=TestRunner(suite=suite)
runner.run
