#Set Camera的测试
import requests
from APIpackage import SetAPI
from APIpackage import CreatError
url='http://localhost:8000/arcgisearth/camera'

#正向验证
data = {"position": {"x": 0, "y": 0, "z": 1000000, "spatialReference": {"wkid": 4326}, "heading": 2.3335941892764884E-17, "tilt": 6.144145559063083E-15, "roll": 0}, "duration": 2}
testSetcamera = SetAPI.SetAPIclass(url,data)
SetCamera_str=testSetcamera.SetCamera()
print(SetCamera_str)

#url 错误
url1=CreatError.urlErrorclass(url)
urllist=url1.CreatErrorUrlList()
for i in urllist:
  testGetcamera = SetAPI.SetAPIclass(i[0],data)
  try:
      SetCamera_str = testGetcamera.SetCamera()
      print(SetCamera_str)
  except Exception as e:
      print(i[1],e)

#requests方法错误
try:
  resp = requests.get(url,data)
  strback=resp.json()
  print(strback)
except Exception as e:
  print('requests错误使用get方法', e)

try:
  resp = requests.post(url,data)
  strback=resp.json()
  print(strback)
except Exception as e:
  print('requests错误使用post方法', e)

#参数错误
data1 = CreatError.ParErrorclass(data)
parlist = data1.ParErrorList()
for iparerror in parlist:
  testGetcamera = SetAPI.SetAPIclass(url,iparerror[0])
  try:
      SetCamera_str = testGetcamera.SetCamera()
  except Exception as e:
      print(iparerror[1], e)