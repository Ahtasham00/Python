#isAww
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
Product_name=[]
Product_price=[]
Product_rating=[]
i=1
headers = {
    'origin': 'https://flipkart.com'
 }
#Total page you want to capture
total_pages=15
disastor_error=0
while(True):
 url=f"https://www.flipkart.com/search?q=mobiles+under+100000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_19_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_19_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles+under+50000%7CMobiles&requestId=0f2d29af-1c84-4754-8382-4fc831547fd9&as-searchtext=Mobiles+under+50000&page={i}"
 html_text=requests.get(url,headers=headers).text
 soup=BeautifulSoup(html_text,"lxml")
 element=soup.find("div",id="container")
 if element:
     print("Page found")
     boxis=soup.find_all("div",class_="_2kHMtA")
     
     for box in boxis:
         name=box.find("div",class_="_4rR01T")
         price=box.find("div",class_="_30jeq3 _1_WHN1")
         #Product_name.append(name)
         #Product_price.append(price)
         if name and price:
          name = name.text
          if price:
           price = price.text
          else:
              price="Nill"
          print(name, "   :  ", price)
          Product_name.append(name)
          Product_price.append(price)
         #print(name,"   :  ",price)
     '''
     names=soup.find_all("div",class_="_4rR01T")
     for j in names:
      name=j.text
      Product_name.append(name)
      prices=soup.find_all("div",class_="_1_WHN1")
     for j in prices:
      price=j.text
      Product_price.append(price)
      '''
     print(f"Page {i} Record stored successfully")
     i=i+1
     disastor_error=0
 else:
     disastor_error=disastor_error+1
     print("Page not found")
     if(disastor_error>15):
         print("Due to server invalid responce script closed")
         break;
 if(i>total_pages):
     print("All pages clear")
     break;
if(disastor_error<8):
 df=pd.DataFrame({"Product Name":Product_name,"Prices":Product_price})
 csv_file_path = 'output1.csv'
 df.to_csv(csv_file_path)
