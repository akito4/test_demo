import unittest
import requests
from businessCommon.data_create import CreateData
from businessCommon.data_clear import ClearData
from common.checkOutput import CheckPro


class TestPro(unittest.TestCase):
    userid = 429577729
    wps_sid = "V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601"

    def setUp(self) -> None:
        # 前置构建便签数据并移至回收站""
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        ClearData.clear_notes(self.userid, self.wps_sid)
        ClearData.clear_recycle(self.userid, self.wps_sid)

    def testCase01_deleteRecycleNote_major(self):
        """
        删除/清空回收站便签_主流程
        :return:
        """
        host = "http://note-api.wps.cn"
        path = "/v3/notesvr/cleanrecyclebin"
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
        # print(data)
        res = requests.post(url, headers=headers, json=data)
        # print(res.json())
        r_json = res.json()
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")

        expected = {
            'responseTime': int
        }
        CheckPro().check_output(expected=expected, actual=r_json)

        self.assertEqual(1, len(r_json), msg="返回字段数 != 1")

        # 查看回收站下标签数据
        startindex = 0
        rows = 999
        get_recycle_url = host + f'/v3/notesvr/user/{self.userid}/invalid/startindex/{startindex}/rows/{rows}/notes'
        res = requests.get(get_recycle_url, headers=headers)
        # recycle_json = res.json()
        #
        # noteIds = []
        # for noteInfo in recycle_json['webNotes']:
        #     noteIds.append(noteInfo['noteId'])

        self.assertEqual([], res.json()['webNotes'], msg='回收站下不存在便签数据断言失败')
