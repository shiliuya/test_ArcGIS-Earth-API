#GetAPI的单元测试
import unittest
from APIpackage import GetAPI

class GetAPItest(unittest.TestCase):
    def test_GetCamer(self):
        testGetcamera = GetAPI.GetAPIclass('http://localhost:8000/arcgisearth/camera')
        GetCamera_str=testGetcamera.GetCamera()
        self.assertEqual(GetCamera_str, "successful call")
    def test_GetLayer(self):
        testGetLayer = GetAPI.GetAPIclass('http://localhost:8000/arcgisearth/layer/91f496f5-9317-4dd3-b221-77f62bd37232')
        GetLayer_str=testGetLayer.GetLayer()
        self.assertEqual(GetLayer_str, "successful call")

if __name__ == '__main__':
    unittest.main()
