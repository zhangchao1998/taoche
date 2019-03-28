import requests
from lxml import etree
url = 'https://www.taoche.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
response = requests.get(url=url, headers=headers).text
tree = etree.HTML(response)
one_list = tree.xpath('//div[@class="header-city-province-text"]/a/@href')
city_list = []
for i in one_list:
    city_list.append(i.split('.')[0][2:])

url = 'https://beijing.taoche.com/all/'
response1 = requests.get(url=url, headers=headers).text
tree1 = etree.HTML(response1)
car_list = []
ul_list = tree1.xpath('//ul[@class="ul_C"]')[1:]
for ul in ul_list:
    two_list = ul.xpath('./li/a/@href')
    for i in two_list:
        car_list.append(i[1:-1])
with open('数据.txt', 'w', encoding='utf-8') as f:
    f.write(str(city_list))
    f.write('\n')
    f.write(str(car_list))

