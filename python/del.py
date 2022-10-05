food_list = ['떡볶이', '피자', '빙수', '치킨', '곱창']

# print(food_list[0])

import random 
# print(random.choice(food_list)) # alt : 멀티 선택 가능
# print(random.choice(food_list))

# for _ in range(3):  
#     print(random.choice(food_list))

import requests
url = 'https://api.agify.io?name=jun'

rlt_data = requests.get(url).json()

print(rlt_data['name'])   # dict형식의 인덱싱 방법 : ['key값']
