#SetAPI的单元测试
import unittest
from APIpackage import SetAPI

class GetAPItest(unittest.TestCase):
    def test_SetCamer(self):
        data = {"position": {"x": 0, "y": 0, "z": 1000000, "spatialReference": {"wkid": 4326}, "heading": 2.3335941892764884E-17, "tilt": 6.144145559063083E-15, "roll": 0}, "duration": 2}
        testSetcamera = SetAPI.SetAPIclass('http://localhost:8000/arcgisearth/camera',data)
        SetCamera_str=testSetcamera.SetCamera()
        self.assertEqual(SetCamera_str, "successful call")

    def test_AddLayer(self):
        portal_item = {"URI": "https://www.arcgis.com/home/item.html?id=19dcff93eeb64f208d09d328656dd492","target": "operationalLayers", "type": "PortalItem"}
        testAddLayer = SetAPI.SetAPIclass('http://localhost:8000/arcgisearth/layer',portal_item)
        AddLayer_str=testAddLayer.AddLayer()
        self.assertEqual(AddLayer_str, "successful call")


if __name__ == '__main__':
    unittest.main()