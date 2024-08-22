import unittest
import requests


class TestPro(unittest.TestCase):
    # def setUp(self):
    # print("========== 开始测试 ==========")

    def testCase01_updateNoteContent_major(self):
        """上传/更新便签内容_主流程"""
        host = "http://note-api.wps.cn"
        path = "/v3/notesvr/set/notecontent"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        data = {
            "noteId": "81699a386cf05f1c94f09032bd54301e",
            "title": "tCIzAHOuVrb88Q5/74qwgQ==",
            "summary": "ozxMCwC2na8/6IRTteKxVGshh/aqRz77dWlJ4EP2LKY=",
            "body": "ozxMCwC2na8/6IRTteKxVLbIt+MdOg45sEkXG7LMzWg=",
            "localContentVersion": "21",
            "BodyType": "0"
        }
        res = requests.post(url, headers=headers, json=data)
        # print(res.json())
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
        self.assertIn('contentVersion', str(res.json()), msg="contentVersion字段断言失败")
