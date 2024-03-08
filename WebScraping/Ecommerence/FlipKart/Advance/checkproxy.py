#isAww
import requests
import random
from bs4 import BeautifulSoup

def check(proxy):
    try:
        response = requests.get("https://dnsleaktest.com/", proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
           soup = BeautifulSoup(response.content, 'html.parser')
           info = soup.find('div', class_='welcome')
           subinfo=info.find_all('p')
           country=subinfo[1].get_text()[5:]
           print(f"\n Connected To {country}\n IP :{proxy}")
           return True
        else:
            return False
    except requests.RequestException as e:
        return False
def get_ip(proxy_list):
 print("\n\n\n\Connectin To Random Proxy  Server...",end="")
 while(True):
  print("...",end="")
  proxy=random.choice(proxy_list)
  if(check(proxy)==True):
     return proxy   

#-----------------------------------------------------
