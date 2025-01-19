from auth import Auth
import requests, json

#市區公車之路線站序資料
url1 = r"https://tdx.transportdata.tw/api/basic/v2/Bus/StopOfRoute/City/{}/{}?%24format=JSON"

#公車動態定點資料
ur12 = r"https://tdx.transportdata.tw/api/basic/v2/Bus/RealTimeNearStop/City/{}/{}?%24format=JSON"

class Data():
    def __init__(self) -> None:
        self.data_header = Auth().get_data_header()

    def get_data_responce(self, url):
        data_response = requests.get(url, headers=self.data_header)
        return json.loads(data_response.text)
    
    def get_stop_of_route(self, cname, rname):
        return self.get_data_responce(url1.format(cname, rname))
    
    def get_real_time_near_stop(self, cname, rname):
        return self.get_data_responce(ur12.format(cname, rname))