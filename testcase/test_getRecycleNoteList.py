import unittest
import requests
from businessCommon.data_clear import ClearData
from businessCommon.data_create import CreateData


class TestPro(unittest.TestCase):
    user_id = 429577729
    wps_sid = 'V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601'

    def setUp(self) -> None:
        # 前置所有便签和分组以及回收站数据
        ClearData.clear_notes(self.user_id, self.wps_sid)
        ClearData.clear_recycle(self.user_id, self.wps_sid)
        # 前置构建便签数据用于删除
        self.note_id = CreateData.create_notes(self.user_id, self.wps_sid, addGroupId=False)
        # 将前置构建的便签数据移至回收站
        ClearData.clear_notes(self.user_id, self.wps_sid)
        # print(self.note_id)

    def testCase01_getRecycleNoteList_major(self):
        """
        查看回收站下便签列表_主流程
        :return:
        """
        userid = "429577729"
        startindex = "0"
        rows = "10"
        host = "http://note-api.wps.cn"
        path = f"/v3/notesvr/user/{userid}/invalid/startindex/{startindex}/rows/{rows}/notes"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        res = requests.get(url, headers=headers)
        # print(res.json())
        r_json = res.json()
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
        self.assertFalse(r_json['webNotes'] == [], msg='webNotes不为空断言失败')
        self.assertEqual(2, len(r_json),msg='接口返回字段数 != 2')
        # for note in r_json['webNotes']:
        #     if note['noteId'] == self.note_id:
        #         self.assertEqual()
        self.assertEqual(self.note_id, r_json['webNotes'][0]['noteId'], msg='返回的noteId != 构造数据产出的noteId')

