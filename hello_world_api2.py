import requests

def fetch_hello_world():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    print(response.json()['title'])

if __name__ == "__main__":
    fetch_hello_world()
