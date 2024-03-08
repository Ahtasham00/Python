#isAww
from bs4 import BeautifulSoup
import requests
import pandas as pd


url="https://www.businesslist.pk/location/islamabad/9"
#for i in range(1,10):
responce=requests.get(url).text
soup=BeautifulSoup(responce,"lxml")
company_Box=soup.find("div",class_="company with_img g_0")
company_half_link=company_Box.find("a")
company_link="https://www.businesslist.pk"+company_half_link["href"]
company_Page=requests.get(company_link).text
company_soup=BeautifulSoup(company_Page,"lxml")
company_name=company_soup.find("h1").text
company_address=company_soup.find("div",class_="text location").text
company_phone=company_soup.find("div",class_="text phone").text
company_mobile=company_soup.find("div",class_="text").text
company_website=company_soup.find("div",class_="text weblinks").text
print(company_name)
print(company_address)
print(company_phone)
print(company_mobile)
print(company_website)
#print(company_link)
# url="https://www.businesslist.pk/location/islamabad/"+f"{i}"
#print(url)
