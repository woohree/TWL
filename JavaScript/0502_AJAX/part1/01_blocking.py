# 1. sleep
from time import sleep

# print('hi')
# sleep(3)
# print('bye')

# 2. requests

import requests
URL = 'https://jsonplaceholder.typicode.com/todos/1'
print('start')
res = requests.get(URL).json()
print('end')




