import unittest
import requests
from businessCommon.data_create import CreateData
from businessCommon.data_clear import ClearData


# ============================ 用构造数据产出的groupId在查看分组下便签接口查询出便签数据为空 ============================

class TestPro(unittest.TestCase):
    user_id = 429577729
    wps_sid = 'V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601'

    def setUp(self) -> None:
        # 前置清理所有便签和分组数据
        ClearData.clear_notes(self.user_id, self.wps_sid)
        ClearData.clear_recycle(self.user_id, self.wps_sid)
        # 前置构建分组下的数据
        create_data = CreateData.create_notes(self.user_id, self.wps_sid, addGroupId=True)
        # print(create_data)
        self.group_id = create_data[0]
        self.note_id = create_data[1]
        # print(self.group_id)
        # print(self.note_id)

    def testCase01_getGroupNoteList_major(self):
        """
        查看分组下便签_主流程
        :return:
        """
        host = "http://note-api.wps.cn"
        path = "/v3/notesvr/web/getnotes/group"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        data = {
            "groupId": self.group_id,
            "startIndex": 0,
            "rows": 0
        }
        res = requests.post(url, headers=headers, json=data)
        # print(res.json())
        r_json = res.json()
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
        self.assertEqual(1, len(r_json['webNotes']), msg='webNotes数组长度 != 1')
        self.assertEqual(self.note_id, r_json['webNotes'][0]['noteId'], msg='noteId != 前置构造数据的noteId')
