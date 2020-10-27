#Take Snapshot的测试
import shutil
import requests
from PIL import Image
from APIpackage import TakeAPI
from APIpackage import CreatError
url='http://localhost:8000/arcgisearth/snapshot'

#正向验证
TakeSnapshot_str = TakeAPI.TakeSnapshot('http://localhost:8000/arcgisearth/snapshot')
print(TakeSnapshot_str )

#url 错误
url1=CreatError.urlErrorclass(url)
urllist=url1.CreatErrorUrlList()
for i in urllist:
  try:
      TakeSnapshot_str  = TakeAPI.TakeSnapshot(i[0])
  except Exception as e:
      print(i[1],e)

#requests方法错误
try:
    resp = requests.put(url, stream=True)
    with open('img.png', 'wb') as out_file:
        shutil.copyfileobj(resp.raw, out_file)
    img = Image.open('img.png')
    img.show()
    print(img.tell())
except Exception as e:
    print('requests错误使用put方法', e)

try:
    resp = requests.post(url, stream=True)
    with open('img.png', 'wb') as out_file:
        shutil.copyfileobj(resp.raw, out_file)
    img = Image.open('img.png')
    img.show()
    print(img.tell())
except Exception as e:
  print('requests错误使用post方法', e)
