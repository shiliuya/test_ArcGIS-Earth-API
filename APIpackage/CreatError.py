#创造错误URL和参数的库
import copy

class urlErrorclass():
    def __init__(self, url):
        self.url = url
    def CreatErrorUrlList(self):
        urllist = [[self.url[:-7], 'url缺少后缀'], [self.url[:-9] + '    ' + self.url[-9:], 'url中间有空格']]
        return urllist

class ParErrorclass():
    def __init__(self, data):
        self.data = data
    def LackParRequired(self):
        data1=copy.deepcopy(self.data)
        if 'URI' in data1:
            del data1['URI']
        if 'URIs' in data1:
            del data1['URIs']
        if 'position' in data1:
            del data1['position']
        return str(data1)
    def IncompleteParRequired(self):
        data1=copy.deepcopy(self.data)
        if 'URI' in data1:
            data1['URI']=data1['URI'][:-3]
        if 'URIs' in data1:
            for i in data1['URIs']:
                i=i[:-3]
        if 'position' in data1:
            del data1['position']['x']
        return str(data1)
    def ErrorParRequired(self):
        data1=copy.deepcopy(self.data)
        if 'URI' in data1:
            data1['URI']='www.esri.com'
        if 'URIs' in data1:
            data1['URIs']=['www.esri.com','www.esri1.com','www.esri2.com']
        if 'position' in data1:
            data1['position']['x']='A'
        return str(data1)
    def ErrorParOptiona(self):
        data1=copy.deepcopy(self.data)
        if 'heading' in data1:
            data1['heading'] = 'A'
        if 'type' in data1:
            data1['type'] = 'B'
        return str(data1)
    def ErrorParFormat(self):
        data1=copy.deepcopy(self.data)
        data1=str(data1)
        return data1
    def ParErrorList(self):
        ParList=[[ParErrorclass.LackParRequired(self),"缺少必要参数"],[ParErrorclass.IncompleteParRequired(self),'必要参数不完整'],[ParErrorclass.ErrorParRequired(self),'必要参数错误'],[ParErrorclass.ErrorParOptiona(self),'可选参数错误'],[ParErrorclass.ErrorParFormat(self),'参数数据格式错误']]
        return ParList