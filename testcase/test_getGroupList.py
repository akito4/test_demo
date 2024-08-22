import unittest
import requests
from businessCommon.data_clear import ClearData
from businessCommon.data_create import CreateData
from common.checkOutput import CheckPro


class TestPro(unittest.TestCase):
    user_id = 429577729
    wps_sid = 'V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601'

    def setUp(self) -> None:
        # 前置清理便签和分组数据
        ClearData.clear_notes(self.user_id, self.wps_sid)
        ClearData.clear_recycle(self.user_id, self.wps_sid)
        ClearData.clear_groups(self.user_id, self.wps_sid)
        # 前置构建分组数据
        create_data = CreateData.create_groups(self.user_id, self.wps_sid)
        self.group_id = create_data

    def testCase01_getGroupList_major(self):
        """获取分组列表_主流程"""
        host = "http://note-api.wps.cn"
        path = "/v3/notesvr/get/notegroup"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        data = {
            "excludeInvalid": 'true'
        }
        res = requests.post(url, headers=headers, json=data)
        # print(res.json())
        r_json = res.json()
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")

        expected = {
            'requestTime': int,
            'noteGroups': [
                {
                    'userId': str,
                    'groupId': str,
                    'groupName': str,
                    'order': int,
                    'valid': int,
                    'updateTime': int
                }
            ]
        }
        CheckPro().check_output(expected=expected, actual=r_json)

        self.assertEqual(2, len(r_json), msg='接口返回字段数 != 2')

        groups = r_json['noteGroups']
        # 定义空列表存储查询到的所有groupId
        groupIds = []
        for group in groups:
            groupIds.append(group['groupId'])

        self.assertIn(self.group_id, groupIds, msg='构造数据产出的groupId不存在')

        for group in r_json['noteGroups']:
            if group['groupId'] == self.group_id:
                self.assertEqual(1, group['valid'], msg='分组valid为1断言失败')


