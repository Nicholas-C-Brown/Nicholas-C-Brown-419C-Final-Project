
import requests
import webbrowser
import socket

URL = "https://www.linkedin.com/oauth/v2/authorization"

RESPONSE_TYPE = r"code"

CLIENT_ID = r"867nxtorfvyz78"
CLIENT_SECRET = r"eSn4kF8wysqNA6XF"

REDIRECT_URI = r"http://192.168.56.1:8000"

SCOPE = r"r_liteprofile"

PARAMS = {"response_type":RESPONSE_TYPE,"client_id":CLIENT_ID,"redirect_uri":REDIRECT_URI,"scope":SCOPE}

request = requests.get(url = URL, params=PARAMS)

webbrowser.open(request.url)

#create an INET, STREAMing socket
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host,
# and a well-known port
serversocket.bind((socket.gethostname(), 8000))
#become a server socket

serversocket.listen(1)

while 1:
    #accept connections from outside
    (clientsocket, address) = serversocket.accept()

    print("CLIENT:",clientsocket)











