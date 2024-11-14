
import time


from selenium import webdriver


from selenium.webdriver.support.ui import WebDriverWait


from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.by import By








import re


#вы пишите свой код
try:
    #инициализирую драйвер
    driver = webdriver.Chrome()
    #говорим WebDriver каждый элемент искать 5 секунд.
    # путь до страницы
    driver.get('https://erikdark.github.io/QA_autotest_16/')






    # ниже пишем свой код
    #говорим selenium проверять, в течении 5 секунд, пока кнопка не станет доступной
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,'price1'))).click()

    


   


   
    # конец блока с моим кодом




#вы пишите то что должно сработать даже если блок try не отработал себя
finally:
    time.sleep(3)
    driver.quit()



