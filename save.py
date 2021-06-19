#!/usr/bin/python3
import re
import sys
from elasticsearch import Elasticsearch

es_host="127.0.0.1"
es_port="9200"
es = Elasticsearch([{'host':es_host, 'port':es_port}], timeout = 30)

def save_data(weather, food):
    # ID - hot : 1, cold : 2, rainy : 3, snowy : 4

    if (weather == "hot"):
        r = es.get(index='food', doc_type='weather', id=1)
        food_list = list(r['_source']['Food'])
        frequency_list = list(r['_source']['Frequency'])

        merge_list = []

        is_food = False
        for j in range(0, len(food_list)):
            if (food == food_list[j]):
                frequency_list[j] = frequency_list[j] + 1
                is_food = True
            merge_list.append((frequency_list[j], food_list[j]))

        if not (is_food): #new food add
            food_list.append(food)
            frequency_list.append(1)
            dic = {
                "Weather" : "hot",
                "Food" : tuple(food_list),
                "Frequency" : tuple(frequency_list)
            }
            res = es.index(index='food', doc_type='weather', id=1, body=dic)
            print(res)
            return

        merge_list.sort(reverse=True)
        
        new_freq_list = []
        new_food_list = []

        for j in range (0, len(merge_list)):
            new_freq_list.append(merge_list[j][0])
            new_food_list.append(merge_list[j][1])
        
        dic = {
            "Weather" : "hot",
            "Food" : tuple(new_food_list),
            "Frequency" : tuple(new_freq_list)
        }
        
        res = es.index(index='food', doc_type='weather', id=1, body=dic)
        print(res)
        return

    elif (weather == "cold"):
        r = es.get(index='food', doc_type='weather', id=2)
        food_list = list(r['_source']['Food'])
        frequency_list = list(r['_source']['Frequency'])

        merge_list = []

        is_food = False
        for j in range(0, len(food_list)):
            if (food == food_list[j]):
                frequency_list[j] = frequency_list[j] + 1
                is_food = True
            merge_list.append((frequency_list[j], food_list[j]))

        if not (is_food): #new food add
            food_list.append(food)
            frequency_list.append(1)
            dic = {
                "Weather" : "cold",
                "Food" : tuple(food_list),
                "Frequency" : tuple(frequency_list)
            }
            res = es.index(index='food', doc_type='weather', id=2, body=dic)
            print(res)
            return

        merge_list.sort(reverse=True)
        
        new_freq_list = []
        new_food_list = []

        for j in range (0, len(merge_list)):
            new_freq_list.append(merge_list[j][0])
            new_food_list.append(merge_list[j][1])
        
        dic = {
            "Weather" : "cold",
            "Food" : tuple(new_food_list),
            "Frequency" : tuple(new_freq_list)
        }
        
        res = es.index(index='food', doc_type='weather', id=2, body=dic)
        print(res)
        return

    elif (weather == "rainy"):
        r = es.get(index='food', doc_type='weather', id=3)
        food_list = list(r['_source']['Food'])
        frequency_list = list(r['_source']['Frequency'])

        merge_list = []

        is_food = False
        for j in range(0, len(food_list)):
            if (food == food_list[j]):
                frequency_list[j] = frequency_list[j] + 1
                is_food = True
            merge_list.append((frequency_list[j], food_list[j]))

        if not (is_food): #new food add
            food_list.append(food)
            frequency_list.append(1)
            dic = {
                "Weather" : "rainy",
                "Food" : tuple(food_list),
                "Frequency" : tuple(frequency_list)
            }
            res = es.index(index='food', doc_type='weather', id=3, body=dic)
            print(res)
            return

        merge_list.sort(reverse=True)
        
        new_freq_list = []
        new_food_list = []

        for j in range (0, len(merge_list)):
            new_freq_list.append(merge_list[j][0])
            new_food_list.append(merge_list[j][1])
        
        dic = {
            "Weather" : "rainy",
            "Food" : tuple(new_food_list),
            "Frequency" : tuple(new_freq_list)
        }
        
        res = es.index(index='food', doc_type='weather', id=3, body=dic)
        print(res)
        return

    elif (weather == "snowy"):
        r = es.get(index='food', doc_type='weather', id=4)
        food_list = list(r['_source']['Food'])
        frequency_list = list(r['_source']['Frequency'])

        merge_list = []

        is_food = False
        for j in range(0, len(food_list)):
            if (food == food_list[j]):
                frequency_list[j] = frequency_list[j] + 1
                is_food = True
            merge_list.append((frequency_list[j], food_list[j]))

        if not (is_food): #new food add
            food_list.append(food)
            frequency_list.append(1)
            dic = {
                "Weather" : "snowy",
                "Food" : tuple(food_list),
                "Frequency" : tuple(frequency_list)
            }
            res = es.index(index='food', doc_type='weather', id=4, body=dic)
            print(res)
            return

        merge_list.sort(reverse=True)
        
        new_freq_list = []
        new_food_list = []

        for j in range (0, len(merge_list)):
            new_freq_list.append(merge_list[j][0])
            new_food_list.append(merge_list[j][1])
        
        dic = {
            "Weather" : "snowy",
            "Food" : tuple(new_food_list),
            "Frequency" : tuple(new_freq_list)
        }
        
        res = es.index(index='food', doc_type='weather', id=4, body=dic)
        print(res)
        return

def get_info(weather):
    if (weather == "hot"):
        dic = es.get(index='food', doc_type='weather', id=1)
        return dic
    elif (weather == "cold"):
        dic = es.get(index='food', doc_type='weather', id=2)
        return dic
    elif (weather == "rainy"):
        dic = es.get(index='food', doc_type='weather', id=3)
        return dic
    elif (weather == "snowy"):
        dic = es.get(index='food', doc_type='weather', id=4)
        return dic

'''
#test
if __name__== '__main__':
    save_data("hot", "삼계탕")
'''