import requests

def getUserSkills(name, accessToken):
    URL = "https://api.linkedin.com/v2/skills/" + name

    LANGUAGE = r"en"
    COUNTRY = r"US"

    PARAMS = {"oauth2_access_token":accessToken,"local.language":LANGUAGE,"locale.country":COUNTRY}

    request = requests.get(url = URL, params=PARAMS)

    print(request.url)


TOKEN = "AQULerpUTWGzpliqYCVI_LGrejHWh2E_UosOZx6vP4Ye_ey5KvkeIkbPXk0NzyTyOv3yaxc0ktLkKuy1lO7UplORh73qvahUpy5YQEfaRilG9qOgZ7crP0jnxa0nrGUo767SSpivA_CGXVAQPACszNqxnsAQpolDrkFbQaFzP2ZEaxD_KoaOvnnBa0of_a_mikqv3veOGjLUgab2FoDidmT1zSVLhRDbCpGb-14DV5kvXjI3anMfQRb1eifS697ZuE6yd0IEI-fQ_3NEnuViC_ACsOyuCY3yohOwwCzPwqVLiBxF30Od7epreFZkKmghiSRMKsYwKTCr90MqfpfczB8Oq_QPfQ"

getUserSkills("nicholas-c-brown",TOKEN)