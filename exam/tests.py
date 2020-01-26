from django.test import TestCase
from selenium import webdriver

class Test_Case(TestCase):

    def setup(self):
        self.browser = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')

    def Homepage_fest(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('install', self.browser.page_source)

    def Tear_down(self):
        self.browser.quit()