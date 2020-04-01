import requests
import webbrowser
import socket

def getAccessToken(code):
    URL = "https://www.linkedin.com/oauth/v2/accessToken"

    GRANT_TYPE = r"authorization_code"
    CODE = rf"{code}"
    REDIRECT_URI = r"http://192.168.56.1:8000"
    CLIENT_ID = r"867nxtorfvyz78"
    CLIENT_SECRET = r"eSn4kF8wysqNA6XF"

    PARAMS = {"grant_type":GRANT_TYPE,"code":CODE,"redirect_uri":REDIRECT_URI,"client_id":CLIENT_ID,"client_secret":CLIENT_SECRET}

    request = requests.get(url = URL, params=PARAMS)

    data = request.json

    print(data)

    return data