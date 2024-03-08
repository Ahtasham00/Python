#isAww
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from checkproxy import get_ip
import time
import pandas as pd
#-------------------------------------------------------------

#------------------------Setting proxy--------------------
def setproxy(proxylist):
 PROXY=get_ip(proxylist)
 options = webdriver.ChromeOptions()
 options.add_argument(f"--proxy-server={PROXY}")
 options.add_argument("--ignore-certificate-errors")
 options.add_argument("--headless")
 return options
try:
 s = Service(r"D:\Selenium\chromedriver-win64\chromedriver.exe")
 #------------------------opening proxy file-----------------
 filename="workingproxies3"
 proxy_list=[]
 with open(f'{filename}.txt', 'r') as file:
    proxy_list = [line.strip() for line in file]   
 
 chrome_options = setproxy(proxy_list)
 #chrome_options.add_argument("--headless")
 driver=webdriver.Chrome(service=s, options=chrome_options)
 city=input("Cityname :")
 service=input("information you need :")
 query=f"{service} in {city}"
 print(query)
 link=f"https://www.google.com/localservices/prolist?&q={query}&src=2"
 if(link!=0):
  driver.get(f"{link}")
  data_list = []
  while(True):
   subdirectories = driver.find_elements(By.CLASS_NAME, "E94Gcd")
   print("list of compines found")
   for subdirectory in subdirectories:
       infolist=subdirectory.find_elements(By.CLASS_NAME, "NwqBmc")
       print("company info list found")
       i=1
       for info in infolist:
           company_name = info.find_element(By.CLASS_NAME, "rgnuSb").text
           sublist = info.find_elements(By.CLASS_NAME, "hGz87c")
           phone_number = sublist[-1].text
           data_list.append({'Company Name': company_name, 'Phone Number': phone_number})
           print("Company Name:", company_name)
           print("Phone Number:", phone_number)
           print("==========================\n")
   try:
    next_button = driver.find_element(By.XPATH, "//button[@aria-label='Next']")
    next_button.click()
    driver.implicitly_wait(5)
    print("********Next found********")
   except NoSuchElementException as e:
    print("First next link not found")
    try:
        #next_button=driver.find_element(By.CLASS_NAME,"d6cvqb")
        next_link=driver.find_element(By.ID,"pnnext")
        next_link.click()
        driver.implicitly_wait(5)
        print("********Next found********")
    except NoSuchElementException as e:
           print("********Next Page Not found********\n") 
           break
 df = pd.DataFrame(data_list)
 # Save the DataFrame to a CSV file
 csv_filename = f"{city}{service}.csv"
 df.to_csv(csv_filename, index=False)
except:
    print("Unknow error occur")
finally:
    try:
     driver.quit()
     print("Script Exit")
    except:
     print("Script Exit")
    
