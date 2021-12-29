import unittest
import selenium
import time
from appium import webdriver


class MyTestCase3(unittest.TestCase):

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
    def testdianjibofang(self):
        def get_size():
            x = self.driver.get_window_size()['width']
            y = self.driver.get_window_size()['height']
            return x, y

        print(get_size())

        # 屏幕向上滑动
        def swipeUp(t):
            l = get_size()
            x1 = int(l[0] * 0.5)  # x坐标
            y1 = int(l[1] * 0.75)  # 起始y坐标
            y2 = int(l[1] * 0.25)  # 终点y坐标
            self.driver.swipe(x1, y1, x1, y2, t)

        # 屏幕向下滑动
        def swipeDown(t):
            l = get_size()
            x1 = int(l[0] * 0.5)  # x坐标
            y1 = int(l[1] * 0.25)  # 起始y坐标
            y2 = int(l[1] * 0.75)  # 终点y坐标
            self.driver.swipe(x1, y1, x1, y2, t)

        # 屏幕向左滑动
        def swipLeft(t):
            l = get_size()
            x1 = int(l[0] * 0.75)
            y1 = int(l[1] * 0.5)
            x2 = int(l[0] * 0.05)
            self.driver.swipe(x1, y1, x2, y1, t)

        # 屏幕向右滑动
        def swipRight(t):
            l = get_size()
            x1 = int(l[0] * 0.05)
            y1 = int(l[1] * 0.5)
            x2 = int(l[0] * 0.75)
            self.driver.swipe(x1, y1, x2, y1, t)

        # 调用向左滑动
        swipLeft(1000)
        print("向左滑动")
        time.sleep(3)
        # 调用向右滑动
        swipRight(1000)
        print("向右滑动")
        time.sleep(3)
        # 调用向上滑动
        swipeUp(1000)
        swipeUp(1000)
        swipeUp(1000)
        print("向上滑动")
        time.sleep(3)
        # 调用向下滑动
        swipeDown(1000)
        swipeDown(1000)
        swipeDown(1000)
        print("向下滑动")
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase3)
        # unittest框架的TextTestRunner（）类，通过该类下面的run（）方法来运行suite所组装的测试用例，入参为suite测试套件
        unittest.TextTestRunner(verbosity=2).run(suite)
        # unittest.main()