from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import json

def city_exists(query):
    city = query.replace(' ','-').lower()
    url = 'https://api.teleport.org/api/urban_areas/slug:'+city+'/scores/'
    try:
        json_obj = urlopen(url)
    except HTTPError as e:
        print('Could not find city')
        return None
    except URLError as e:
        print('Reason: ', e.reason)
        return None
    return json_obj

def city_compare(json_obj_city1,json_obj_city2,city1,city2):
    data_city1 = json.load(json_obj_city1)
    data_city2 = json.load(json_obj_city2)

    sector = []
    city1_scores = []
    city2_scores = []

    print('\n'+city1+' scores.')
    for item in data_city1['categories']:
        print(item['name'],'=',item['score_out_of_10'])
        sector.append(item['name'])
        city1_scores.append(item['score_out_of_10'])
        
    print('\n'+city2+' scores.')
    for item in data_city2['categories']:
        print(item['name'],'=',item['score_out_of_10'])
        city2_scores.append(item['score_out_of_10'])

    city1_counter = 0
    city2_counter = 0
    sector_superiority = []
    print('\n')
    for i in range(16):
        if(city1_scores[i] > city2_scores[i]):
            city1_counter+=1
            sector_superiority = city1
        else:
            city2_counter+=1
            sector_superiority = city2
        print('In sector '+sector[i]+' '+sector_superiority+' is superior.')   
    print('\n')
    print(city1+' is superior in '+str(city1_counter)+' sectors.')
    print(city2+' is superior in '+str(city2_counter)+' sectors.')
    print('\n')
    if( city1_counter > city2_counter ):
        print('As a result '+city1+' is overall superior.')
    elif( city1_counter == city2_counter ):
        print('As a result both cities are equal.')
    else:
        print('As a result '+city2+' is overall superior.')
    
            


json_obj_city1 = None
while (json_obj_city1 is None ):
    city_entered_1 = input('Please enter a city: ')
    json_obj_city1 = city_exists(city_entered_1)

json_obj_city2 = None
while (json_obj_city2 is None ):
    city_entered_2 = input('Please enter a second city for comparison:  ')
    json_obj_city2 = city_exists(city_entered_2)

city_compare(json_obj_city1,json_obj_city2,city_entered_1,city_entered_2)


