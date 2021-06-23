#!/usr/bin/python3
#-*- coding:utf-8 -*- 
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import sys
 
def crawling(gu, dong, food):

    region = quote("대구")
    string = "https://search.naver.com/search.naver?where=nexearch&sm=top_sly.hst&fbm=1&acr=1&acq=%EB%8C%80%EA%B5%AC+%EB%B6%81%EA%B5%AC+&qdt=0&ie=utf8&query=" + region + "+" + quote(gu) + "+" + quote(dong) + "+" + quote(food)
    tmp = urlopen(string)
    url = tmp.read().decode("utf-8")

    soup = BeautifulSoup(url, "html.parser")
    divs = soup.findAll('ul', {'class' : '_3bohv _1V_Nc'}) 

    infos = []
    name = ""
    link = ""
    rating = ""
    for div in divs:
        sects = div.findAll('div', {'class' : '_3hn9q'})
        for sect in sects:
            name = ""
            rating = ""
            name_sects = sect.findAll('span', {'class' : 'OXiLu'})
            for name_sect in name_sects:
                name = name_sect.text
        
            link_sects = sect.findAll('a', href=True)
            for link_sect in link_sects:
                link = link_sect['href']

            rating_sects = sect.findAll('span', {'class' : '_2FqTn _1mRAM'})
            for rating_sect in rating_sects:
                rating = rating_sect.text

            infos.append([name, rating, link])
    return infos

if __name__== '__main__':

   kdong = "산격3동"
   kgu = "북구"   
   kfood = "떡볶이"
   #print(crawling(kgu, kdong, kfood))