import re
import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class Dist_test(unittest.TestCase):
    def setUp(self):
        dri = pwd()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_semester_report()

    def test_clusterbtn(self):

        time.sleep(5)
        self.driver.find_element_by_xpath(Data.SRD30).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Data.SRB2).click()
        time.sleep(8)
        amccount = self.driver.find_elements_by_class_name(Data.dots)
        cnt = len(amccount)-1
        self.assertNotEqual(0,cnt,msg="Failed")
        driver = cqube(self.driver)
        driver.dots_dist()
    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()











