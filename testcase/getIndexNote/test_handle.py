import unittest
import time
from businessCommon.data_create import CreateData
from businessCommon.data_clear import ClearData
from common.httpReMethod import BusinessRequest
from common.caseLogs import info, error, step, class_case_log
from common.checkOutput import CheckPro
from common.readYaml import ReadYaml


@class_case_log
class GetIndexNoteHandle(unittest.TestCase):
    envConfig = ReadYaml().env_config()
    host = envConfig['host']
    userid = envConfig['user_id']
    wps_sid = envConfig['wps_sid']

    br = BusinessRequest()

    def setUp(self) -> None:
        # 前置清理首页便签数据
        ClearData.clear_notes(self.userid, self.wps_sid)
        ClearData.clear_recycle(self.userid, self.wps_sid)

    def testCase01_getIndexNote_handle_(self):
        """获取首页便签_查询用户第2条数据"""

        step('前置构建2条便签数据')
        self.note_id1 = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False, num=1)
        self.note_id2 = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False, num=1)
        # print(note_id)
        startindex = 1
        rows = 1
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)

        r_json = res.json()
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
        # self.assertEqual(2, len(r_json['webNotes']), msg='便签数据数 != 2')

        expect = {
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
                        'groupId': None,
                        'title': str,
                        'summary': str,
                        'thumbnail': None,
                        'contentVersion': int,
                        'contentUpdateTime': int
                    }
                ]
        }
        CheckPro().check_output(expected=expect, actual=r_json)
        self.assertEqual(self.note_id1, r_json['webNotes'][0]['noteId'])
