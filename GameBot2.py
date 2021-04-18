# this program opens the Firefox browser and starts playing a browser game
# called MATH BATTLE in the address you give

# written in python 3.7

# tested with Windows 10

# requires selenium library to work

# download geckodriver from https://github.com/mozilla/geckodriver/releases
# and add it to PATH or similiar

# use the latest version of Firefox

# works best with python IDLE


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# geckodriver.exe should be saved in PATH or similiar so that it can be found by the program
driver = webdriver.Firefox()

# give the address of your Telegram MATH BATTLE game  e.g. https://tbot.xyz/math/#eyJ1IjoxMjk4ODM3Njk5L...
driver.get("https://tbot.xyz/math/example") #put here the adress of your Telegram MATH BATTLE game

time.sleep(2.0)
button = driver.find_element_by_id('button_correct') # find button by ID.

button.click()  # starts the game
time.sleep(1.0)


for i in range(60):  # give the amount of equations to be solved, max allowed by website is around 1500 
    task = driver.find_element_by_class_name('task')
    taskX = driver.find_element_by_id('task_x')
    taskOp = driver.find_element_by_id('task_op')
    taskY = driver.find_element_by_id('task_y')
    taskRes = driver.find_element_by_id('task_res')

    yhd = taskX.get_attribute('innerHTML') + taskOp.get_attribute('innerHTML') + taskY.get_attribute('innerHTML')
    
    # optionally prints the part of HTML code that is used to check whether the equation is correct
    # print(task.get_attribute('innerHTML'))

    print(yhd) # prints left side of the equation e.g. 50/5
    yhdOK = yhd.replace('×', '*').replace('–', '-')
    
    
    print(eval(yhdOK)) # prints the answer e.g. 10

    if(eval(yhdOK)==eval(taskRes.get_attribute('innerHTML'))):
        button.click()
    else:
        element2 = WebDriverWait(driver, 20000).until(EC.element_to_be_clickable((By.ID,"button_wrong")))
        element2.click()
    


# optionally close the bot just after the target score is achieved so that the score is not shared with other players
# driver.close()

