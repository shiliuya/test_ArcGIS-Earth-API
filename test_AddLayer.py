#Add Layer的测试
import requests
from APIpackage import SetAPI
from APIpackage import CreatError
url='http://localhost:8000/arcgisearth/layer'
data={"URI": "http://ogc.bgs.ac.uk/cgi-bin/BGS_Bedrock_and_Superficial_Geology/wms?SERVICE=WMS&REQUEST=GetCapabilities","target": "baseMaps","type": "WMS"}
testAddLayer = SetAPI.SetAPIclass(url,data)
AddLayer_str=testAddLayer.AddLayer()
print(AddLayer_str)

#url 错误
url1=CreatError.urlErrorclass(url)
urllist=url1.CreatErrorUrlList()
for i in urllist:
  testGetcamera = SetAPI.SetAPIclass(i[0],data)
  try:
      AddLayer_str = testGetcamera.AddLayer()
      print(AddLayer_str )
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
  resp = requests.put(url,data)
  strback=resp.json()
  print(strback)
except Exception as e:
  print('requests错误使用put方法', e)

##参数错误
data1 = CreatError.ParErrorclass(data)
parlist = data1.ParErrorList()
for iparerror in parlist:
  testGetcamera = SetAPI.SetAPIclass(url,iparerror[0])
  try:
      AddLayer_str = testGetcamera.AddLayer()
  except Exception as e:
      print(iparerror[1], e)