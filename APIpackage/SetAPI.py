#请求Set Camera和Add Layer API的库
import requests
def setSth(url,data):
    resp = requests.put(url,json=data)
    strback = resp.json()
    print(strback)
    return strback
def addSth(url,data):
    resp = requests.post(url,json=data)
    strback = resp.json()
    print(strback)
    return strback
class SetAPIclass():
    def __init__(self,url,data):
        self.data=data
        self.url= url

    def SetCamera(self):
        strSetCamera=setSth(self.url, self.data)
        # 如果返回的字符串中包含有'result',则返回"successful call"
        if "result" in strSetCamera:
            return "successful call"

    def AddLayer(self):
        strAddLayer=addSth(self.url, self.data)
        # 如果返回的字符串中包含有‘displayName',则返回"successful call"
        if 'displayName' in strAddLayer:
            return "successful call"