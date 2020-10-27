#Get Camera的测试
import requests
from APIpackage import GetAPI
from APIpackage import CreatError
url='http://localhost:8000/arcgisearth/camera'

#正向验证
testGetcamera = GetAPI.GetAPIclass(url)
GetCamera_str=testGetcamera.GetCamera()
print(GetCamera_str)

#url 错误
url1=CreatError.urlErrorclass(url)
urllist=url1.CreatErrorUrlList()
for i in urllist:
  testGetcamera = GetAPI.GetAPIclass(i[0])
  try:
      GetCamera_str = testGetcamera.GetCamera()
      print(GetCamera_str)
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

