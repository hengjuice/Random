from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

USERNAME = 'HENG0225'
PASSWORD = 'Qwertyuiop1'

PATH = 'C:/Users/Serenity4/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(PATH)

#driver.get('https://sso.wis.ntu.edu.sg/webexe88/owa/sso_login1.asp?t=&p2=https://venus2.wis.ntu.edu.sg/iNTULinks/Login.aspx&extra=&pg=')

driver.get('https://www3.ntu.edu.sg/cits2/iNTU_CR.html')

other_services = driver.find_element_by_xpath('/html/body/div[7]/span/a')

other_services.click()

undergraduate = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[2]')

undergraduate.click()

# AT THIS POINT NEW TAB WILL BE GENERATED
p = driver.current_window_handle
child_window = driver.window_handles

for w in child_window:
#switch focus to child window
    if(w!=p):
        driver.switch_to_window(w)

time.sleep(0.9)

user_name = driver.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input')

user_name.send_keys(USERNAME)

domain = driver.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/select')

domain.click()

student_option = driver.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/select/option[2]')

student_option.click()

ok_button = driver.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[4]/td/input[1]')

ok_button.click()

password = driver.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input')

password.send_keys(PASSWORD)

ok_button2 = driver.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr/td/form/center[1]/table/tbody/tr/td/table/tbody/tr[5]/td/input[1]')
ok_button2.click()


#Sports facilities booking page
driver.get('https://venus.wis.ntu.edu.sg/PortalServices/ServiceListModule/LaunchService.aspx?type=1&launchSvc=https%3A%2F%2Fsso%2Ewis%2Entu%2Eedu%2Esg%2Fwebexe88%2Fowa%2Fsso%5Fredirect%2Easp%3Ft%3D1%26app%3Dhttps%3A%2F%2Fwis%2Entu%2Eedu%2Esg%2Fwebexe%2Fowa%2Fsrce%5Fsmain%5Fs%2Emain')

apply_button = driver.find_element_by_xpath('/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[1]/div/div/div[2]/div[3]/div[1]/a')
apply_button.click()

facility = driver.find_element_by_xpath('/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/ul/li[4]/table[2]/tbody/tr[14]/td/input')
facility.click()

slot = driver.find_element_by_xpath('/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/table[2]/tbody/tr[24]/td[8]/input')
slot.click()

#Confirm button
confirm = driver.find_element_by_xpath('/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/table[2]/tbody/tr[29]/td[9]')
confirm.click()

driver.close()