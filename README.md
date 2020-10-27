# test_ArcGIS-Earth-API
本项目是用于测试如下5个ArcGIS Earth API:

1.Get Camera
2.Set Camera
3.Add Layer
4.Get Layer
5.Take Snapshot

每个API都有对应的测试
1.test_GetCamera
2.test_SetCamera
3.test_AddLayer
4.test_GetLayer
5.test_TakeSnapshot

每个API的反向测试用例都按如下原则设计：
1.url错误：缺少后缀、中间包含空格
2.request方法错误（以本应使用get方法为例）：错误使用put方法，错误使用post方法
3.传入参数错误:必须参数缺少,必须参数错误,可选参数错误,参数格式错误

除此之外，API package是一个提供测试中可复用方法的包
其中包含4个模块
1.GetAPI
2.SetAPI
3.TakeAPI
4.CraetError

每个模块都有对应的单元测试：
1.unittest_GetAPI
2.unittest_SetAPI
3.unittest_TakeAPI
4.unittest_CreatError


