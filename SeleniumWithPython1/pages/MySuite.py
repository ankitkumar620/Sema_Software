import unittest
from pages.MyTest1 import MyTestCase1
from pages.MyTest2 import MyTestCase2
import HtmlTestRunner

suite=unittest.TestSuite()
loader=unittest.TestLoader()
"""
suite.addTest(MyTestCase1('test2'))
suite.addTest(MyTestCase2('test4'))
suite.addTest(MyTestCase1('test1'))
suite.addTest(MyTestCase2('test3'))
"""

suite.addTest(loader.loadTestsFromTestCase(MyTestCase1))
suite.addTest(loader.loadTestsFromTestCase(MyTestCase2))
#unittest.TextTestRunner().run(suite)
HtmlTestRunner.HTMLTestRunner(output='test-reports',report_title='Test report').run(suite)