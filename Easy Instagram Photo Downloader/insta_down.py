import requests
from bs4 import BeautifulSoup

start_url = input("Enter the link : ")

response = requests.get(start_url)

html = response.text

soup = BeautifulSoup(html, "lxml")
photo_url = soup.find("meta",property="og:image")['content']
print(photo_url)

photo_name = 'ig_downloaded' + start_url[28:-1]

print("photo name :" , photo_name)

get_photo_url = requests.get(photo_url)

f = open(photo_name + '.jpg', 'ab')

f.write(get_photo_url.content)
print('Processing')
f.close()
print("download complete")
