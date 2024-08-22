import unittest
import requests
# from businessCommon.data_create import create_groups
from businessCommon.data_create import CreateData
from common.checkOutput import CheckPro


class TestPro(unittest.TestCase):
    user_id = 429577729
    wps_sid = 'V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601'

    def setUp(self) -> None:
        # 前置构建分组数据
        self.group_id = CreateData.create_groups(self.user_id, self.wps_sid)

    def testCase01_deleteGroup_major(self):
        """
        删除分组_主流程
        :return:
        """
        host = "http://note-api.wps.cn"
        path = "/notesvr/delete/notegroup"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        data = {
            "groupId": self.group_id
        }
        res = requests.post(url, headers=headers, json=data)
        r_json = res.json()
        # print(res.json())
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")

        expected = {
            'responseTime': int
        }
        CheckPro().check_output(expected=expected, actual=r_json)

        self.assertEqual(int, type(r_json['responseTime']), msg='responseTime字段类型断言失败')
        self.assertEqual(1, len(r_json), msg='返回字段 != 1个')

        # 查询用户名下分组，校验删除的分组状态是否为无效（valid==0）
        get_group_url = host + "/v3/notesvr/get/notegroup"
        get_group_data = {
            "excludeInValid": False
        }
        res = requests.post(get_group_url, headers=headers, json=get_group_data)
        # 定义变量d_valid，表示删除的分组状态
        d_valid = None
        for group in res.json()['noteGroups']:
            if group['groupId'] == self.group_id:
                d_valid = group['valid']
        self.assertEqual(d_valid, 0, msg='分组无效状态断言失败')
