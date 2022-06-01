import requests
import json

class Get_res():
    def __init__(self,url):
        self.url=url

    def get_res(self):
        #url = "https://jsonplaceholder.typicode.com/posts/1"
        response = requests.get(self.url)
        print(response)
        print(response.content)
        print(response.status_code)
        return response






