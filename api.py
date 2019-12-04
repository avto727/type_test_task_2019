import requests
import json

def one(enver, login, pasw):
    data = '{ "password": "' + pasw + '", "userName": "' + login + '"}'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    url = enver + '/api/ClientApi/Login'
    print(url)
    response = (requests.post(url, headers=headers, data=data)).text
    return response

login_1 = 'manag3'
pas = '12345678'
test_env = "https://master.edo-paritet.ru:9443"
token_02 = one(test_env, login_1, pas)
print(f"token = {token_02}")
