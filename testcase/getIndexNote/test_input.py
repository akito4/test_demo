import unittest
import time
from businessCommon.data_create import CreateData
from businessCommon.data_clear import ClearData
from common.httpReMethod import BusinessRequest
from common.caseLogs import info, error, step, class_case_log
from common.checkOutput import CheckPro
from common.readYaml import ReadYaml


@class_case_log
class GetIndexNoteInput(unittest.TestCase):
    envConfig = ReadYaml().env_config()
    host = envConfig['host']
    userid = envConfig['user_id']
    old_wps_sid = envConfig['old_wps_sid']
    wps_sid = envConfig['wps_sid']

    br = BusinessRequest()

    def setUp(self) -> None:
        # 前置清理首页便签数据

        step('前置清理账号下所有首页便签数据')
        ClearData.clear_notes(self.userid, self.wps_sid)
        ClearData.clear_recycle(self.userid, self.wps_sid)

    def testCase01_getIndexNote_input_miss_userid(self):
        """获取首页便签_path缺少userId"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = 999
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 404, msg="状态码断言失败")
        expect = {
            'timestamp': str,
            'status': 404,
            'error': 'Not Found',
            'message': 'No message available',
            'path': path
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase02_getIndexNote_input_miss_startindex(self):
        """获取首页便签_path缺少startindex"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = 999
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 404, msg="状态码断言失败")
        expect = {
            'timestamp': str,
            'status': 404,
            'error': 'Not Found',
            'message': 'No message available',
            'path': path
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase03_getIndexNote_input_miss_rows(self):
        """获取首页便签_path缺少rows"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = 999
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 404, msg="状态码断言失败")
        expect = {
            'timestamp': str,
            'status': 404,
            'error': 'Not Found',
            'message': 'No message available',
            'path': path
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase04_getIndexNote_input_wps_sid_invalid(self):
        """获取首页便签_headers中wps_sid无效"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = 999
        headers = {
            'Cookie': 'wps_sid=xixi123456',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 401, msg="状态码断言失败")
        expect = {
            "errorCode": -2010,
            "errorMsg": str
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase05_getIndexNote_input_wps_sid_expire(self):
        """获取首页便签_headers中wps_sid过期"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = 999
        headers = {
            'Cookie': f'wps_sid={self.old_wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 401, msg="状态码断言失败")
        expect = {
            "errorCode": -2010,
            "errorMsg": str
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase06_getIndexNote_input_userid_overlength(self):
        """获取首页便签_path中userid过长"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = 999
        userid = 95279527952795279527952795279527952795279527
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 500, msg="状态码断言失败")
        expect = {
            "errorCode": -7,
            "errorMsg": '参数类型错误！'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase07_getIndexNote_input_userid_0(self):
        """获取首页便签_path中userid为0"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = 999
        userid = 0
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/{userid}/0/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 401, msg="状态码断言失败")
        expect = {
            "errorCode": -2010,
            "errorMsg": str
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase08_getIndexNote_input_userid_minus1(self):
        """获取首页便签_path中userid为-1"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = 999
        userid = -1
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 412, msg="状态码断言失败")
        expect = {
            "errorCode": -1011,
            "errorMsg": 'user change!'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase09_getIndexNote_input_userid_minint(self):
        """获取首页便签_path中userid为 -2147483649"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = 999
        userid = -2147483649
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 412, msg="状态码断言失败")
        expect = {
            "errorCode": -1011,
            "errorMsg": 'user change!'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase10_getIndexNote_input_userid_maxint(self):
        """获取首页便签_path中userid为 2147483648"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = 999
        userid = 2147483648
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 412, msg="状态码断言失败")
        expect = {
            "errorCode": -1011,
            "errorMsg": 'user change!'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase11_getIndexNote_input_userid_float(self):
        """获取首页便签_path中userid为小数"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = 999
        userid = 1.5
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 500, msg="状态码断言失败")
        expect = {
            "errorCode": -7,
            "errorMsg": '参数类型错误！'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase12_getIndexNote_input_userid_str(self):
        """获取首页便签_path中userid为字符串"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = 999
        userid = '九五二七'
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 500, msg="状态码断言失败")
        expect = {
            "errorCode": -7,
            "errorMsg": '参数类型错误！'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase13_getIndexNote_input_userid_strNumber(self):
        """获取首页便签_path中userid为字符串形式的数值"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = 999
        userid = str(f'{self.userid}')
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()

        self.assertTrue(res.status_code == 200, msg="状态码断言失败")

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

    def testCase14_getIndexNote_input_userid_null(self):
        """获取首页便签_path中userid为null"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = 999
        userid = None
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 500, msg="状态码断言失败")
        expect = {
            "errorCode": -7,
            "errorMsg": '参数类型错误！'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase15_getIndexNote_input_startindex_overlength(self):
        """获取首页便签_path中startindex过长"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 95279527952795279527952795279527952795279527
        rows = 999
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 500, msg="状态码断言失败")
        expect = {
            "errorCode": -7,
            "errorMsg": '参数类型错误！'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase16_getIndexNote_input_startindex_minus1(self):
        """获取首页便签_path中startindex为-1"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = -1
        rows = 999
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 500, msg="状态码断言失败")
        expect = {
            "errorCode": -7,
            "errorMsg": '参数类型错误！'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase17_getIndexNote_input_startindex_minint(self):
        """获取首页便签_path中startindex为-2147483649"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = -2147483649
        rows = 999
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 500, msg="状态码断言失败")
        expect = {
            "errorCode": -7,
            "errorMsg": '参数类型错误！'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase18_getIndexNote_input_startindex_maxint(self):
        """获取首页便签_path中startindex为2147483648"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 2147483648
        rows = 999
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 500, msg="状态码断言失败")
        expect = {
            "errorCode": -7,
            "errorMsg": '参数类型错误！'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase19_getIndexNote_input_startindex_float(self):
        """获取首页便签_path中startindex为小数"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 1.5
        rows = 999
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 500, msg="状态码断言失败")
        expect = {
            "errorCode": -7,
            "errorMsg": '参数类型错误！'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase19_getIndexNote_input_startindex_str(self):
        """获取首页便签_path中startindex为字符串"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = '九五二七'
        rows = 999
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 500, msg="状态码断言失败")
        expect = {
            "errorCode": -7,
            "errorMsg": '参数类型错误！'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase20_getIndexNote_input_startindex_strNumber(self):
        """获取首页便签_path中startindex为字符串类型的数值"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = str(0)
        rows = 999
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
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

    def testCase21_getIndexNote_input_startindex_null(self):
        """获取首页便签_path中startindex为null"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = None
        rows = 999
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 500, msg="状态码断言失败")
        expect = {
            "errorCode": -7,
            "errorMsg": '参数类型错误！'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase22_getIndexNote_input_rows_overlength(self):
        """获取首页便签_path中rows过长"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = 95279527952795279527952795279527952795279527
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 500, msg="状态码断言失败")
        expect = {
            "errorCode": -7,
            "errorMsg": '参数类型错误！'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase23_getIndexNote_input_rows_minus1(self):
        """获取首页便签_path中rows为-1"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = -1
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 500, msg="状态码断言失败")
        expect = {
            "errorCode": -7,
            "errorMsg": '参数类型错误！'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase24_getIndexNote_input_rows_minint(self):
        """获取首页便签_path中rows为-2147483649"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = -2147483649
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 500, msg="状态码断言失败")
        expect = {
            "errorCode": -7,
            "errorMsg": '参数类型错误！'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase25_getIndexNote_input_rows_maxint(self):
        """获取首页便签_path中rows为2147483648"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = 2147483648
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 500, msg="状态码断言失败")
        expect = {
            "errorCode": -7,
            "errorMsg": '参数类型错误！'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase26_getIndexNote_input_rows_float(self):
        """获取首页便签_path中rows为小数"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = 1.5
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 500, msg="状态码断言失败")
        expect = {
            "errorCode": -7,
            "errorMsg": '参数类型错误！'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase27_getIndexNote_input_rows_str(self):
        """获取首页便签_path中rows为字符串"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = '九五二七'
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 500, msg="状态码断言失败")
        expect = {
            "errorCode": -7,
            "errorMsg": '参数类型错误！'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

    def testCase28_getIndexNote_input_rows_strNumber(self):
        """获取首页便签_path中startindex为字符串类型的数值"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = str(999)
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
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

    def testCase29_getIndexNote_input_rows_null(self):
        """获取首页便签_path中rows为null"""

        step('前置构建1条便签数据')
        self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
        # print(note_id)
        startindex = 0
        rows = None
        headers = {
            'Cookie': f'wps_sid={self.wps_sid}',
            "X-User-Key": f'{self.userid}'
        }
        path = f'/v3/notesvr/user/{self.userid}/home/startindex/{startindex}/rows/{rows}/notes'
        url = self.host + path

        res = self.br.get(url, headers=headers)
        r_json = res.json()
        self.assertTrue(res.status_code == 500, msg="状态码断言失败")
        expect = {
            "errorCode": -7,
            "errorMsg": '参数类型错误！'
        }
        CheckPro().check_output(expected=expect, actual=r_json)

