import unittest
import requests
from businessCommon.data_create import CreateData
from businessCommon.data_clear import ClearData


class TestPro(unittest.TestCase):
    userid = "429577729"
    wps_sid = "V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601"
    def setUp(self) -> None:
        # 前置清空回收站
        ClearData.clear_recycle(self.userid, self.wps_sid)
        # 前置构建便签数据并移至回收站
        self.note_id = CreateData.create_notes_not_group(self.userid, self.wps_sid)
        ClearData.clear_notes(self.userid, self.wps_sid)
        print(self.note_id)

    def testCase09_restoreRecycleNote_major(self):
        """
        恢复回收站的便签_主流程
        :return:
        """
        host = "http://gonote.wps.cn"
        userid = 429577729
        path = "/gonote/api/v5/notesvr/recover/notes"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        data = {
            "userId": 429577729,
            "noteIds": [
                self.note_id
            ]
        }
        res = requests.post(url, headers=headers, json=data)
        print(res.json())
        r_json = res.json()
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
        self.assertTrue(r_json['code'] == 0, msg='code != 0')
        self.assertTrue(r_json['msg'] == 'success', msg='msg != "success"')
        self.assertEqual(3, len(r_json), msg='返回字段数 != 3')

        # 查询恢复的便签信息
        r_url = host + '/v3/notesvr/get/notebody'
        r_data = {
            'noteIds':[
                self.note_id
            ]
        }
        print(r_data)
        r_res = requests.post(r_url, headers=headers, json=r_data)
        print(r_res.json())

