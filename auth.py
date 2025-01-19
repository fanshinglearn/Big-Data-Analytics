import json, requests

auth_url = "https://tdx.transportdata.tw/auth/realms/TDXConnect/protocol/openid-connect/token"

class Auth():
    def __init__(self) -> None:
        with open("config.json", "r") as f:
            acc = json.load(f)
            self.app_id = acc["app_id"]
            self.app_key = acc["app_key"]

    def get_auth_header(self):
        content_type = 'application/x-www-form-urlencoded'
        grant_type = 'client_credentials'

        return{
            'content-type': content_type,
            'grant_type': grant_type,
            'client_id': self.app_id,
            'client_secret': self.app_key
        }

    def get_data_header(self):
        self.auth_response = requests.post(auth_url, self.get_auth_header())
        auth_JSON = json.loads(self.auth_response.text)
        access_token = auth_JSON.get('access_token')
        return {
            'authorization': 'Bearer '+ access_token,
            'Accept-Encoding': 'gzip'
    }