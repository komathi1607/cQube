
import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class Cluster_Dots(unittest.TestCase):
    def setUp(self):
        driver_path = pwd()
        self.driver = webdriver.Chrome(driver_path.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver = cqube(self.driver)
        driver.login_cqube()
        driver.navigate_to_student_report()
        time.sleep(5)

    def Click_On_Cluster(self):
        self.driver.find_element_by_xpath(Data.Clusters).click()
        lists = self.driver.find_elements_by_class_name(Data.dots)
        def mouseover(i):
            action = ActionChains(self.driver)
            action.move_to_element(lists[i]).perform()
            time.sleep(3)
            del action

        i = 0
        while i < len(lists):
            mouseover(i)
            i = i + 1

    def tearDown(self):
        print(self.driver.current_url)
        time.sleep(5)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
