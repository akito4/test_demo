import time
from unittest import TestCase
from common.caseLogs import class_case_log, info, error, step
from businessCommon.data_clear import ClearData
from common.readYaml import ReadYaml
from parameterized import parameterized


@class_case_log
class AddGroupMajor(TestCase):
    envConfig = ReadYaml().env_config()
    dataConfig = ReadYaml().data_config()['addGroup']

    user_id = envConfig['user_id']
    wps_sid = envConfig['wps_sid']
    host = envConfig['host']
    path = dataConfig['path']
    mustKeys = dataConfig['mustKeys']
    url = host + path
    headers = {
        'Cookie': f'wps_sid={wps_sid}',
        'X-User-Key': user_id
    }

    @parameterized.expand(mustKeys)
    def setUp(self, key) -> None:
        """前置清理所有分组数据"""
        step('前置清理所有分组数据')
        ClearData().clear_groups()

    def testCase01_remove_keys(self):
        """删除便签_必填项校验"""
        data = {
            'groupId': 'xixi' + str(int(time.time() * 1000)),
            'groupName': '测一下这个新增分组'
        }
        data.pop(key)
