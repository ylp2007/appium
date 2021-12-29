import unittest
import selenium
import time
from appium import webdriver
from huadong import huadong

class MyTestCase4(unittest.TestCase):

    def setUp(self):
        # super().setUp()
        print('selenium version = ', selenium.__version__)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'c695d8ac'
        desired_caps['appPackage'] = 'com.ss.android.article.news'
        desired_caps["noReset"] = True
        desired_caps['appActivity'] = 'com.ss.android.article.news.activity.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(10)
    def testxinwen(self):
        huadong.swipRight(self.driver)
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase4)
    # unittest框架的TextTestRunner（）类，通过该类下面的run（）方法来运行suite所组装的测试用例，入参为suite测试套件
    unittest.TextTestRunner(verbosity=2).run(suite)
    #unittest.main()