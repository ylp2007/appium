import unittest
import selenium
import time
from appium import webdriver

class MyTestCase(unittest.TestCase):

    def setUp(self):
        # super().setUp()
        #print('selenium version = ', selenium.__version__)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'c695d8ac'
        desired_caps['appPackage'] = 'com.ss.android.article.news'
        desired_caps["noReset"] = True
        desired_caps['appActivity'] = 'com.ss.android.article.news.activity.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(10)
    def testdianjibofang(self):
        time.sleep(10)
        self.driver.find_element_by_id("com.ss.android.article.news:id/eql").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.ss.android.article.news:id/erq").send_keys("斗罗大陆")
        time.sleep(7)
        self.driver.find_element_by_id("com.ss.android.article.news:id/eit").click()
        time.sleep(5)
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    # unittest框架的TextTestRunner（）类，通过该类下面的run（）方法来运行suite所组装的测试用例，入参为suite测试套件
    unittest.TextTestRunner(verbosity=2).run(suite)
    #unittest.main()