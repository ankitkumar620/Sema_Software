import unittest


class MyTestCase(unittest.TestCase):
    def testadd(self):
        #selenium code here - validations, reports, groups , suite, ordering
        x = 5
        y = 5
        print(x + y)
        #self.assertEqual(True, False)
    def testmultiply(self):
        x = 5
        y = 5
        print(x * y)

if __name__ == '__main__':
    unittest.main()
