#Get Layer的测试
import requests
from APIpackage import GetAPI
from APIpackage import CreatError
url='http://localhost:8000/arcgisearth/layer/02c0972d-1874-4b68-8db5-c74acb25672c'

#正向验证
testGetLayer = GetAPI.GetAPIclass(url)
GetLayer_str=testGetLayer.GetLayer()
print(GetLayer_str)

#url 错误
url1=CreatError.urlErrorclass(url)
urllist=url1.CreatErrorUrlList()
for i in urllist:
  testGetLayer = GetAPI.GetAPIclass(i[0])
  try:
      GetLayer_str = testGetLayer.GetLayer()
      #print(GetLayer_str)
  except Exception as e:
      print(i[1],e)

#requests方法错误
try:
  resp = requests.put(url)
  strback=resp.json()
  print(strback)
except Exception as e:
  print('requests错误使用put方法', e)

try:
  resp = requests.post(url)
  strback=resp.json()
  print(strback)
except Exception as e:
  print('requests错误使用post方法', e)

