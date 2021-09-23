# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')

soup = BeautifulSoup(html.text, 'html.parser')

data1 = soup.find('div', {'class':'weather_info'})

data2 = soup.find('div', {'class':'title_area _area_panel'})

find_currentlocation = data2.find('h2',{'class': 'title'}).text
print('현재 위치: '+find_currentlocation)

find_currentcloud = data1.find('span',{'class': 'blind'}).text
print('현재 기상: '+find_currentcloud)

find_currenttemp = data1.find('strong').text
print('현재 온도: '+find_currenttemp+'℃')