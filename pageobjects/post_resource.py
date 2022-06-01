import requests
import json

class Post_res:
    def __init__(self,url):
        self.url = url

    def post_res(self):
        #url = "https://jsonplaceholder.typicode.com/posts"
        file = open("/home/shraddha/PycharmProjects/API_Framework_1/testdata/new1.json", 'r')
        json_input = file.read()
        request_json = json.loads(json_input)
        print(request_json)
        response = requests.post(self.url, request_json)
        print(response.content)
        return response






