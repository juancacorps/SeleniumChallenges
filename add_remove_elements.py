from selenium import webdriver
import unittest
from time import sleep

class AddRemoveElements(unittest.TestCase):
    def setUp(self):   # inicialitation of test
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/add_remove_elements/')    # url of challengs
        driver.maximize_window()

    def test_add_remove(self):    # run test
        driver = self.driver
        elements_addend = int(input('how many elements you want to add? '))
        elements_removed = int(input('how many elements you want to remove? '))
        diferent_elements = elements_addend - elements_removed
        button_add_element = driver.find_element_by_xpath('//div[@class="example"]/button')
        sleep(3)
        for i in range(elements_addend):
            button_add_element.click()   
        for i in range(elements_removed):
            try:
                button_remove_element = driver.find_element_by_xpath('//div[@id="elements"]/button[@class="added-manually"]')
                button_remove_element.click()
            except:
                print('is deleted more than the account')
                break
        if diferent_elements>0:
            print(f'you will see {diferent_elements} elements on the screen')
        else:
            print('you will see 0 elements on the screen')

    def tearDown(self):    # function for close the chrome
        sleep(5)
        driver = self.driver
        driver.close()
        
if __name__ == '__main__':
    unittest.main(verbosity =  2)