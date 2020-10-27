#CreatError的单元测试
import unittest
from APIpackage import CreatError

class MyTestCase(unittest.TestCase):
    def test_urlErrorclass(self):
        url = 'http://localhost:8000/arcgisearth/camera'
        url1 = CreatError.urlErrorclass(url)
        urllist = url1.CreatErrorUrlList()
        print(urllist)
        self.assertEqual(urllist , [['http://localhost:8000/arcgisearth','url缺少后缀'], ['http://localhost:8000/arcgisear    th/camera', 'url中间有空格']])
    def test_ParErrorclass(self):
        data1 = {"position": {"x": 0, "y": 0, "z": 1000000, "spatialReference": {"wkid": 4326}, "heading": 2.3335941892764884E-17, "tilt": 6.144145559063083E-15, "roll": 0}, "duration": 2}
        data=CreatError.ParErrorclass(data1)
        datalist=data.ParErrorList()
        print(datalist)
        self.assertEqual(datalist,[["{'duration': 2}", '缺少必要参数'], [
            "{'position': {'y': 0, 'z': 1000000, 'spatialReference': {'wkid': 4326}, 'heading': 2.3335941892764884e-17, 'tilt': 6.144145559063083e-15, 'roll': 0}, 'duration': 2}",
            '必要参数不完整'], [
             "{'position': {'x': 'A', 'y': 0, 'z': 1000000, 'spatialReference': {'wkid': 4326}, 'heading': 2.3335941892764884e-17, 'tilt': 6.144145559063083e-15, 'roll': 0}, 'duration': 2}",
             '必要参数错误'], [
             "{'position': {'x': 0, 'y': 0, 'z': 1000000, 'spatialReference': {'wkid': 4326}, 'heading': 2.3335941892764884e-17, 'tilt': 6.144145559063083e-15, 'roll': 0}, 'duration': 2}",
             '可选参数错误'], [
             "{'position': {'x': 0, 'y': 0, 'z': 1000000, 'spatialReference': {'wkid': 4326}, 'heading': 2.3335941892764884e-17, 'tilt': 6.144145559063083e-15, 'roll': 0}, 'duration': 2}",
             '参数数据格式错误']])


if __name__ == '__main__':
    unittest.main()
