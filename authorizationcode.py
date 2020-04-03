import requests
import webbrowser
import socket


def getAuthCode():
    URL = "https://www.linkedin.com/oauth/v2/authorization"

    RESPONSE_TYPE = "code"
    CLIENT_ID = "867nxtorfvyz78"
    REDIRECT_URI = "http://192.168.56.1:8000"
    SCOPE = "r_liteprofile+r_emailaddress+w_member_social"

    URL += "?response_type="+RESPONSE_TYPE+"&client_id="+CLIENT_ID+"&redirect_uri="+REDIRECT_URI+"&scope="+SCOPE

    print(URL)

    request = requests.get(url = URL)


    webbrowser.open(request.url)

    #create an INET, STREAMing socket
    serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    #bind the socket to a public host,
    # and a well-known port
    serversocket.bind((socket.gethostname(), 8000))
    #become a server socket

    serversocket.listen(1)

    while True:
        #accept connections from outside
        (clientsocket, address) = serversocket.accept()

        print("Connected to:",address)

        while True:
            data = clientsocket.recv(1024).decode("utf-8")
            value = data.split(" ")[1]
            code = value[value.index("=")+1:len(value)]
            break

        break

    serversocket.close()
    clientsocket.close()

    return code















