#请求Get Camera和Get Layer API的库
import requests

def GetInformation(url):
    resp = requests.get(url)
    strback=resp.json()
    print(strback)
    return strback

class GetAPIclass():
    def __init__(self,url):
        self.url= url

    def GetCamera(self):
        strGetCamera=GetInformation(self.url)
        #如果返回的字符串中包含有'position',则返回"successful call"
        if 'position' in strGetCamera:
            return "successful call"

    def GetLayer(self):
        strGetLayer=GetInformation(self.url)
        # 如果返回的字符串中包含有'displayName',则返回"successful call"
        if 'displayName' in strGetLayer:
            return "successful call"