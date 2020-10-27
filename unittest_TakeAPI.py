#TakeAPI的单元测试
import unittest
from APIpackage import TakeAPI

class TakeAPItest(unittest.TestCase):
    def test_TakeSnapshot(self):
        TakeSnapshot_str = TakeAPI.TakeSnapshot('http://localhost:8000/arcgisearth/snapshot')
        self.assertEqual(TakeSnapshot_str,0)


if __name__ == '__main__':
    unittest.main()
