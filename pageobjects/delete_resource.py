import requests

class Del_res():
    def __init__(self,url):
        self.url = url

    def del_res(self):
        #url = "https://jsonplaceholder.typicode.com/posts/1"
        response = requests.delete(self.url)
        # Fetch response code
        print(response.status_code)
        #assert response.status_code == 200
        return response


