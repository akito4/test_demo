import time
import unittest
import requests
from businessCommon.data_clear import ClearData
from common.checkOutput import CheckPro
from common.caseLogs import info, error, step
from common.httpReMethod import BusinessRequest


class TestPro(unittest.TestCase):
    user_id = 429577729
    wps_sid = 'V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601'
    br = BusinessRequest()

    def setUp(self) -> None:
        # 前置删除所有分组数据
        ClearData.clear_groups(self.user_id, self.wps_sid)

    def testCase01_addNoteGroup_major(self):
        """
        新增分组_主流程
        :return:
        """

        host = "http://note-api.wps.cn"
        path = "/v3/notesvr/set/notegroup"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        group_id = 'xixi_' + str(int((time.time()) * 1000))
        # print(group_id)
        data = {
            "groupId": group_id,
            "groupName": "测一下这个新增分组",
            "order": 0
        }
        # res = requests.post(url, headers=headers, json=data)

        step('【step】新增分组开始')


        res = self.br.post(url, headers=headers, json=data)



        r_json = res.json()
        # print(r_json)
        self.assertTrue(res.status_code == 200, msg='状态码断言失败')

        expected = {
            'responseTime': int,
            'updateTime': int
        }
        CheckPro().check_output(expected=expected, actual=r_json)

        self.assertEqual(int, type(r_json['responseTime']), msg='repsonseTime非int类型')
        self.assertEqual(int, type(r_json['updateTime']), msg='updateTime非int类型')
        self.assertEqual(2, len(r_json.keys()), msg='返回字段 != 2个')

        # 查询用户名下分组，校验新增分组是否存在
        get_group_url = host + "/v3/notesvr/get/notegroup"
        get_group_data = {
            "excludeInValid": True
        }
        res = requests.post(get_group_url, headers=headers, json=get_group_data)
        self.assertEqual(1, len(res.json()['noteGroups']), msg='查询出分组数量 != 1个')
        # print(r_json.keys())
        self.assertEqual(group_id, res.json()['noteGroups'][0]['groupId'], msg='查询出的分组id != 新增时自定义的分组id')
