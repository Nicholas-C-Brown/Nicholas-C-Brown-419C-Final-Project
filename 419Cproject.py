import authorizationcode
import accesstoken

code = authorizationcode.getAuthCode()

accessToken = accesstoken.getAccessToken(code)

print(accesstoken)