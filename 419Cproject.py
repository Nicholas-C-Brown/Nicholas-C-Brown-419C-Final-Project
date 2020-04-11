import authorizationcode
import accesstoken

code = authorizationcode.getAuthCode()

Token,expires = accesstoken.getAccessToken(code)

print("ACCESS TOKEN:",Token,"\nEXPIRES:",expires)

