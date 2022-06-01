import requests
import json


class Put_res:
    def __init__(self,url):
        self.url = url

    def put_res(self):
        #url = "https://jsonplaceholder.typicode.com/posts/1"
        file = open('/home/shraddha/PycharmProjects/API_Framework_1/testdata/new1.json')
        json_input = file.read()
        request_json = json.loads(json_input)
        response = requests.put(self.url, request_json)
        print(response.content)
        return response





        # Parse response contents
        #response_json = json.loads(response.text)
        # updated_li= jsonpath.jsonpath(response_json,'count')
        # print(updated_li[0])


