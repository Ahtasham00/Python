from bs4 import BeautifulSoup
import requests
import pandas as pd

Product_data = []
headers = {
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': '124312312313212312313132',
    'Referer': 'https://www.flipkart.com/',
    'Sec-Ch-Ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Linuk"',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site'
 }

for i in range(1, 8):
    url = f"https://www.flipkart.com/search?q=mobiles+under+50000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_19_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_19_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles+under+50000%7CMobiles&requestId=0f2d29af-1c84-4754-8382-4fc831547fd9&as-searchtext=Mobiles+under+50000&page={i}"
    html_text = requests.get(url,headers=headers).text
    soup = BeautifulSoup(html_text, "lxml")
    print(soup)
    products = soup.find_all("div", class_="_1AtVbE")
    for product in products:
        name = product.find("div", class_="_4rR01T")
        price = product.find("div", class_="_30jeq3 _1_WHN1")
        print(name)
        rating_tag = product.find("div", class_="_3LWZlK")
        if rating_tag:
            rating = rating_tag
        else:
            rating = "N/A"
        
        Product_data.append({
            "Product Name": name,
            "Price": price,
            "Rating": rating
        })
    
    print("Page:", i, "Total Products:", len(Product_data))

df = pd.DataFrame(Product_data)
print(df)
df.to_csv("filpcarunder5000.csv", index=False)
