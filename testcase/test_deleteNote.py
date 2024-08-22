import unittest
import requests
from businessCommon.data_create import CreateData
from common.checkOutput import CheckPro


class TestPro(unittest.TestCase):
    user_id = 429577729
    wps_sid = 'V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601'

    def setUp(self) -> None:
        # 前置构建便签数据
        self.note_id = CreateData.create_notes(self.user_id, self.wps_sid, addGroupId=False)
        # print(self.note_id)

    def testCase01_deleteNote_major(self):
        """删除便签_主流程"""
        host = "http://note-api.wps.cn"
        path = "/v3/notesvr/delete"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        data = {
            "noteId": self.note_id
        }
        # print(self.note_id)
        res = requests.post(url, headers=headers, json=data)
        # print(res.json())
        r_json = res.json()
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")

        expected = {
            'responseTime': int
        }
        CheckPro().check_output(expected=expected, actual=r_json)

        self.assertEqual(int, type(r_json['responseTime']), msg='response字段类型断言失败')
        self.assertEqual(1, len(r_json), msg='返回字段 != 1个')

        get_note_url = host + '/v3/notesvr/get/notebody'
        get_note_data = {
            "noteIds": [
                self.note_id
            ]
        }
        res = requests.post(get_note_url, headers=headers, json=get_note_data)
        r_json = res.json()
        # print(r_json)
        self.assertEqual(0, r_json['noteBodies'][0]['valid'], msg='便签无效断言失败')
