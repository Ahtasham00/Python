#isAww
from bs4 import BeautifulSoup
import requests
import pandas as pd
from checkproxy import get_ip
import time
Product_name=[]
Product_price=[]
Product_rating=[]
i=1
filename="workingproxies1"
proxy_list=[]
with open(f'{filename}.txt', 'r') as file:
    proxy_list = [line.strip() for line in file]

headers = {
    'origin': 'https://flipkart.com/home'
 }
#Total page you want to capture
total_pages=5
disastor_error=0
while(True):
 url=f"https://www.flipkart.com/search?q=mobiles+under+50000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_19_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_19_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles+under+50000%7CMobiles&requestId=0f2d29af-1c84-4754-8382-4fc831547fd9&as-searchtext=Mobiles+under+50000&page={i}"
 proxy_ip=get_ip(proxy_list)
 proxy = {
    'http': f'http://{proxy_ip}',
    'https': f'https://{proxy_ip}'
 }
 html_text=requests.get(url,headers=headers,proxies=proxy).text
 soup=BeautifulSoup(html_text,"lxml")
 element=soup.find("div",id="container")
 if element:
     print("Page found")
     names=soup.find_all("div",class_="_4rR01T")
     for j in names:
      name=j.text
      Product_name.append(name)
      prices=soup.find_all("div",class_="_1_WHN1")
     for j in prices:
      price=j.text
      Product_price.append(price)
     print(f"Page {i} Record stored successfully")
     i=i+1
     disastor_error=0
 else:
     disastor_error=disastor_error+1
     print("Page not found")
     if(disastor_error>8):
         print("Due to server invalid responce script closed")
         break;
 if(i>total_pages):
     print("All pages clear")
     break;
if(disastor_error<8):
 df=pd.DataFrame({"Product Name":Product_name,"Prices":Product_price})
 csv_file_path = 'output2.csv'
 df.to_csv(csv_file_path)
