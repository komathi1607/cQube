import re
import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

# script to choose district , block ,cluster and mouse over on last
from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class Choose16(unittest.TestCase):
    def setUp(self):
        driver_path = pwd()
        self.driver = webdriver.Chrome(driver_path.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver = cqube(self.driver)
        driver.login_cqube()

        time.sleep(5)

    def test_District(self):
        self.driver.find_element_by_xpath(Data.SARD16).click()
        self.driver.find_element_by_xpath(Data.SARD3).click()
        self.driver.find_element_by_xpath(Data.SARC2).click()
        time.sleep(15)
        data = self.driver.find_elements_by_xpath(Data.directory)
        for i in range(len(data)):
            print(data[i].text)


        lists = self.driver.find_elements_by_class_name(Data.dots)
        def mouseover(i):

            action = ActionChains(self.driver)
            action.move_to_element(lists[i]).perform()
            time.sleep(2)
            del action

        i = 0
        while i < len(lists):
            mouseover(i)
            i = i + 1
        count = len(lists) - 1
        school = self.driver.find_element_by_xpath(Data.schoolcount).text
        res = re.sub("\D", "", school)
        self.assertEqual(res, str(count), "both are not having matching records")

    def tearDown(self):
            time.sleep(5)
            # print(self.driver.get_screenshot_as_file(""))
            self.driver.close()

if __name__ == "__main__":
        unittest.main()
