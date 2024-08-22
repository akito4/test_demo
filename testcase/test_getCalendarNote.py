import unittest
import requests
import time
from businessCommon.data_create import CreateData
from businessCommon.data_clear import ClearData
from common.checkOutput import CheckPro


class TestPro(unittest.TestCase):
    user_id = 429577729
    wps_sid = 'V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601'

    def setUp(self) -> None:
        # 前置清理所有便签数据
        ClearData.clear_notes(self.user_id, self.wps_sid)
        ClearData.clear_recycle(self.user_id, self.wps_sid)
        # 前置构建特定时间段里的便签数据
        self.startTime = int((time.time()))
        self.note_id = CreateData.create_notes(self.user_id, self.wps_sid, remindTime=int(time.time()), remindType=0, addGroupId=False)
        self.stopTime = int((time.time()))

    def testCase01_getCalendarNote_major(self):
        """
        查看日历下便签_主流程
        :return:
        """
        host = "http://note-api.wps.cn"
        path = "/v3/notesvr/web/getnotes/remind"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        data = {
            "remindStartTime": self.startTime,
            "remindEndTime": self.stopTime,
            "startIndex": "0",
            "rows": "10"
        }
        res = requests.post(url, headers=headers, json=data)
        print(res.json())
        r_json = res.json()
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")

        expected = {
            'responseTime': int,
            'webNotes':
                [
                    {
                        'noteId': str,
                        'createTime': int,
                        'star': int,
                        'remindTime': int,
                        'remindType': int,
                        'infoVersion': int,
                        'infoUpdateTime': int,
                        'groupId': str,
                        'titile': str,
                        'summary': str,
                        'thumbnail': str,
                        'contentVersion': int,
                        'contentUpdateTime': int
                    }
                ]
        }
        CheckPro().check_output(expected=expected, actual=r_json)

        # print(r_json['webNotes'][0]['noteId'])
        self.assertEqual(1, len(r_json['webNotes']), msg='noteId数 != 1')
        self.assertEqual(self.note_id, r_json['webNotes'][0]['noteId'], msg='查询到的noteId != 前置构造数据的noteId')
