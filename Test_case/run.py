import  unittest
from Test_case.Test_kangke import *
suit=unittest.TestSuite()
suit.addTest(Test_watch_vido("Buy_classes"))
if __name__== "__main__":
    runner=unittest.TextTestRunner()
    runner.run(suit)