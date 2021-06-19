#!/usr/bin/python3
import re
import sys
from elasticsearch import Elasticsearch

es_host="127.0.0.1"
es_port="9200"

hot_food = ['팥빙수', '냉면', '초계국수', '메밀소바', '콩국수', '비빔국수', '삼계탕']
cold_food = ['칼국수', '짬뽕', '수제비', '매운탕', '국밥']
rainy_food = ['파전', '칼국수', '삼겹살', '짬뽕']
snowy_food = ['우동', '분식', '칼국수', '전골', '만두', '샤브샤브', '수제비', '찌개']

frequency_hot = [30, 30, 30, 30, 30, 30, 30]
frequency_cold = [30, 30, 30, 30, 30]
frequency_rainy = [30, 30, 30, 30]
frequency_snowy = [30, 30, 30, 30, 30, 30, 30, 30]

hot = {
    "Weather" : "hot",
    "Food" : tuple(hot_food),
    "Frequency" : tuple(frequency_hot)
}

cold = {
    "Weather" : "cold",
    "Food" : tuple(cold_food),
    "Frequency" : tuple(frequency_cold)
}

rainy = {
    "Weather" : "rainy",
    "Food" : tuple(rainy_food),
    "Frequency" : tuple(frequency_rainy)
}

snowy = {
    "Weather" : "snowy",
    "Food" : tuple(snowy_food),
    "Frequency" : tuple(frequency_snowy)
}

if __name__== '__main__':
    es = Elasticsearch([{'host':es_host, 'port':es_port}], timeout=30)

    res = es.index(index='food', doc_type='weather', id=1, body=hot)
    print(res)
    res = es.index(index='food', doc_type='weather', id=2, body=cold)
    print(res)
    res = es.index(index='food', doc_type='weather', id=3, body=rainy)
    print(res)
    res = es.index(index='food', doc_type='weather', id=4, body=snowy)
    print(res)