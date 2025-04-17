import requests
api = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()
print(api)