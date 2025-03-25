from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 访问在线待办事项应用的首页
        self.browser.get('http://localhost:8000')

        # 检查网页标题是否包含"To-Do"
        self.assertEqual("To-Do lists", self.browser.title, "browser title was:" + self.browser.title)
        self.fail("Finish the test!")

        # 应用有一个输入待办事项的文本输入框
        # 检查文本输入框中输入了"Buy flowers"

if __name__ == '__main__':
    unittest.main()