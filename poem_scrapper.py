import requests, csv
from bs4 import BeautifulSoup
# Collect first page of artists’ list
page = requests.get('https://100.best-poems.net/top-100-best-poems.html')
# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
poem_name_list = soup.find(id='content')
base_url = 'https://100.best-poems.net'
# Pull text from all instances of <a> tag within BodyText div
poem_name_list_items = poem_name_list.find_all('a', href=True)
file = open('poem_file_names.csv', 'w')
f = csv.writer(file)
for poem_name in poem_name_list_items:
	f.writerow([poem_name.contents[0].replace(" ", "").replace("'", "").replace("?", "").replace(":", "").replace(";", "").replace(",", ""),
				(base_url + poem_name['href'])])
file.close()