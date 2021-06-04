#!/usr/bin/python3
#-*- coding:utf-8 -*- 
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import sys
 
def crawling(gu, dong, food):

    region = quote("대구")
    string = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=" + region + "+" + quote(gu) + "+" + quote(dong) + "+" + quote(food)
    tmp = urlopen(string)
    url = tmp.read().decode("utf-8")
    
    soup = BeautifulSoup(url, "html.parser")
    divs = soup.findAll('div', {'class':'info_area'}) 
    addresses = soup.findAll('div', {'class':'txt address'})
    infos = []
    name = ""
    address = ""
    rating = ""
    for div in divs:
        name_sects = div.findAll('a')
        for name_sect in name_sects:
            name = name_sect.text
        name = name[2:] 
        
        address_sects = div.findAll('div', {'class' : 'txt address'})
        for address_sect in address_sects:
            addresses = address_sect.text
            if (len(str(addresses)) > 0 and str(addresses).find("지번") >= 0):
                address = str(addresses).split("지번")
        
        rating_sects = div.findAll('span', {'class' : 'rating'})
        for rating_sect in rating_sects:
            rating = rating_sect.text

        if (len(address) > 0):
            infos.append([name, address[0], rating])
        else:
            infos.append([name, address, rating])

    print(infos[0])
    print(infos[1])
    print(infos[2])
    return infos

if __name__== '__main__':

   kdong = sys.argv[2] 
   kgu = sys.argv[1]   
   kfood = sys.argv[3] 
   informations = crawling(kgu, kdong, kfood)