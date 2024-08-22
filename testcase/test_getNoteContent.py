import unittest
import requests

from businessCommon.data_clear import ClearData
from businessCommon.data_create import CreateData


class TestPro(unittest.TestCase):
    user_id = 429577729
    wps_sid = 'V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601'

    def setUp(self) -> None:
        # 前置清理便签和分组数据
        ClearData.clear_notes(self.user_id, self.wps_sid)
        ClearData.clear_recycle(self.user_id, self.wps_sid)
        # 前置构造便签数据
        create_data = CreateData.create_notes(self.user_id, self.wps_sid, addGroupId=False)
        self.note_id = create_data

    def testCase01_getNoteContent_major(self):
        """
        获取便签内容_主流程
        :return:
        """
        host = "http://note-api.wps.cn"
        path = "/v3/notesvr/get/notebody"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        data = {
            "noteIds": [
                self.note_id
            ]
        }
        res = requests.post(url, headers=headers, json=data)
        r_json = res.json()
        # print(res.json())
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
        self.assertEqual(2, len(r_json), msg='接口返回字段数 != 2')
        self.assertEqual(self.note_id, r_json['noteBodies'][0]['noteId'], msg='noteId != 前置构建数据的noteId')
        self.assertEqual(9, len(r_json['noteBodies'][0]), msg='noteBodies数组字段数 != 9')
