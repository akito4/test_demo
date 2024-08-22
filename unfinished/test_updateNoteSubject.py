import unittest
import requests


class TestPro(unittest.TestCase):
    # def setUp(self):
    # print("========== 开始测试 ==========")

    def testCase01_getNoteContent_major(self):
        """获取便签内容_主流程"""
        host = "http://note-api.wps.cn"
        path = "/v3/notesvr/get/notebody"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        data = {
            "noteIds": [
                "81699a386cf05f1c94f09032bd54301e"
            ]
        }
        res = requests.post(url, headers=headers, json=data)
        # print(res.json())
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
        self.assertIn('noteBodies', str(res.json()), msg="noteBodies字段断言失败")
        self.assertFalse(res.json()['noteBodies'] == [], msg="noteBodies不为空断言失败")
