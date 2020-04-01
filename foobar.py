
import requests

URL = "https://www.linkedin.com/oauth/v2/authorization"

RESPONSE_TYPE = r"code"

CLIENT_ID = r"867nxtorfvyz78"
CLIENT_SECRET = r"eSn4kF8wysqNA6XF"

REDIRECT_URI = r"http://localhost:8000"

SCOPE = r"r_liteprofile"

PARAMS = {"response_type":RESPONSE_TYPE,"client_id":CLIENT_ID,"redirect_uri":REDIRECT_URI,"scope":SCOPE}

request = requests.get(url = URL, params=PARAMS)

print(request.text)











