import unittest
import  jingdong,jingdong_login


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)


if __name__ == 'jingdong_suit':
    testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器中
    testunit.addTest(jingdong_login.JingdongLogin("test_jingdong_login"))
    testunit.addTest(jingdong.Jingdong("test_jingdong"))

    unittest.TextTestRunner().run(testunit)


