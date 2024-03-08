#iSAww
from bs4 import BeautifulSoup
import requests
import pandas as pd
product_name=[]
produc_price=[]
product_review=[]

headers={
    "Sec-Ch-Ua-Platform": '"Window"',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36",
    
}
query=input("What would you like to scrap from Amazone")
modify_query=query.replace(" ", "+")
output_file=query.replace(" ","_")
url=f"https://www.amazon.com/s?k={modify_query}&page=1"
print(url)
while(True):
 result=requests.get(url,headers=headers).text
 print("====================================================")
 soup=BeautifulSoup(result,'lxml')
 boxes=soup.find_all("div",class_="s-asin")
 for box in boxes:
     name=box.find("span",class_="a-size-base-plus a-color-base a-text-normal")
     price=box.find("span",class_="a-offscreen")
     revw=box.find("span",class_="a-icon-alt")
     product_name.append(name.text)
     if price:
        produc_price.append(price.text)
     else:  
        other=box.find("div",class_="a-row a-size-base a-color-secondary puis-interactive-asin-expander-hide")
        if other:
            other_price=other.find("span",class_="a-color-base")
            if other_price:
                produc_price.append(other_price.text)
            else:
               produc_price.append("N/A")
        else:
            produc_price.append("N/A")
     if revw:
        product_review.append(revw.text)
     else:
        product_review.append("N/A")
     
    # print(name.text)
 next_url=soup.find('a',class_="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator")
 if(next_url):
  url="https://www.amazon.com"+next_url.get('href')
 else:
    break
 print("Next page url is :",url)

df=pd.DataFrame({"Product Name":product_name,"Prices":produc_price,"Review":product_review})
csv_file_path = f'{output_file}.csv'
df.to_csv(csv_file_path)
