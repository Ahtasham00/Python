from bs4 import BeautifulSoup
import requests
import pandas as pd
from checkproxy import get_ip
Product_name=[]
Product_price=[]
Product_rating=[]
import time
filename="workingproxies1"
proxy_list=[]
with open(f'{filename}.txt', 'r') as file:
    proxy_list = [line.strip() for line in file]
for j in range(1,10):
 headers = {
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': '32423942803492803920349238',
    'Referer': 'https://www.flipkart.com/',
    'Sec-Ch-Ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site'
 }
 
 proxy_ip=get_ip(proxy_list)
 proxy = {
    'http': f'http://{proxy_ip}',
    'https': f'https://{proxy_ip}'
 }
 print("Proxy set successfully")
 url=f"https://www.flipkart.com/search?q=mobiles+under+50000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_19_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_19_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles+under+50000%7CMobiles&requestId=0f2d29af-1c84-4754-8382-4fc831547fd9&as-searchtext=Mobiles+under+50000&page={j}"
 html_text=requests.get(url,headers=headers,proxies=proxy).text
 soup=BeautifulSoup(html_text,"lxml")
 #box=soup.find("div",class_="_1YokD2 _3Mn1Gg")
 names=soup.find_all("div",class_="_4rR01T")
 print(f"Current Page :{j}")
 for i in names:
     name=i.text
     Product_name.append(name)
     print(f"{name}")
 prices=soup.find_all("div",class_="_1_WHN1")
 for i in prices:
     price=i.text
     Product_price.append(price)
     print(f"{price}")
 time.sleep(10) 
 #ratings=box.find_all("div",class_="_3LWZlK")
 #for i in ratings:
  #   rating=i.text
  #   Product_rating.append(rating)
 #print("Name : ",len(Product_name),"Price : ",len(Product_price))
 
df=pd.DataFrame({"Product Name":Product_name,"Prices":Product_price,})
print(df)
df.to_csv("filpcarunder5000.csv")
