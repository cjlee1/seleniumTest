from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
import unittest
from selenium.webdriver.support.ui import Select


class tester(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        # navigate to the application home page
        inst.driver.get('https://medo.ai/career/test-challenge/index.html')
    # def test1(self):
    #     self.inputEmail = self.driver.find_element_by_xpath("//form[@class='form-signin']/input[1]")
    #     self.inputPass=self.driver.find_element_by_xpath("//input[@id='inputPassword']")
    #     self.loginButton= self.driver.find_element_by_xpath("//button[@type='submit']")
        
    #     print("Testing if Email address input exists:")
    #     assert self.inputEmail.get_attribute('value') == ""
    #     print("True")

    #     print("Testing if password input exists:")
    #     assert self.inputPass.get_attribute('value') == ""
    #     print("True")

    #     print("Testing if password input exists:")
    #     assert self.loginButton.get_attribute('value') == ""
    #     print("True")

    #     self.inputEmail.send_keys("example@example.ca")
    #     self.inputPass.send_keys("password")
      
    #     time.sleep(5)
    # def test2(self): 
    #     self.div = len(self.driver.find_elements_by_class_name("list-group-item"))
    #     self.value  =self.driver.find_elements_by_class_name("list-group-item")[1].text.rsplit(' ')
       
    #     val= ' '.join([self.value[0],self.value[1],self.value[2]])
    #     self.assertEqual(self.div,3, "There are 3 items in the listgroup.")
    #     self.assertEqual(val,"List Item 2", "The second list item's value is set to 'List Item 2' ")
    #     self.assertEqual(self.value[3],'6', "the second list item's badge value is 6 ")
    def test3(self):
        mySelect = self.driver.find_element_by_id("dropdownMenuButton")
        option = mySelect.get_attribute("innerText")
        
        self.assertEqual(option[0:-1],"Option 1", "Option 1 is the default value.")

        self.driver.find_element_by_id("dropdownMenuButton").click();

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()



if __name__ == '__main__':
    unittest.main()