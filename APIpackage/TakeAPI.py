#请求Take Snapshot API的库
import requests
import shutil
from PIL import Image

def TakeSnapshot(url,filename='img.png'):
    resp = requests.get(url, stream=True)
    with open(filename, 'wb') as out_file:
        shutil.copyfileobj(resp.raw, out_file)
    img = Image.open(filename)
    img.show()
    return (img.tell())
