import json
import requests


class BaseApi:
    def __init__(self):
        self.header = {"Content-Type": "application/json;charset=UTF-8", 'Authorization': self.get_token()}

    def send(self, data):
        r = requests.request(**data)
        print(json.dumps(r.json(), indent=4, ensure_ascii=False))
        return r

    def get_token(self):
        data = {
            "method": "post",
            "url": "http://123.56.138.96:3012/api/ainews-user/user/login",
            "json": {"name": "lsj1", "password": "123123"},
            "headers": {"Content-Type": "application/json;charset=UTF-8"},
        }
        return self.send(data).json().get("access_token")


if __name__ == '__main__':
    print(BaseApi().get_token())
    print(BaseApi().get_id())
