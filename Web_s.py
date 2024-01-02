from bs4 import BeautifulSoup
import requests

try:
    for j in range(1, 4):
        url = 'https://dealers.skoda-auto.co.in/location/tamil-nadu?&page=' + str(j)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        box = soup.find('body', class_="ethemeforskodaupdatedpro")
        showrooms = box.find('section', class_='storelocator-default').findAll('ul')
        for car in showrooms:
            a1 = car.find('li', class_='outlet-name')
            if a1 is not None:
                print("Outlet_name :",a1.text)
            else:
                continue
            a2 = car.find('li', class_='outlet-address')
            if a2 is not None:
                print("Address :",a2.text)
            else:
                continue
            a3 = car.find('li', class_='outlet-phone')
            if a3 is not None:
                print("Contact info :",a3.text)
            else:
                continue

except Exception as e:
    print(e)
