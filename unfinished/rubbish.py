import unittest
import requests
import time


class TestPro(unittest.TestCase):
    # def setUp(self):
    # print("========== 开始测试 ==========")

    def testCase01_getIndexNoteList_major(self):
        """获取首页便签列表_主流程"""
        host = "http://note-api.wps.cn"
        userid = 429577729
        startindex = 0
        rows = 10
        path = f"/v3/notesvr/user/{userid}/home/startindex/{startindex}/rows/{rows}/notes"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601"
        }
        res = requests.get(url, headers=headers)
        # print(res.json())
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
        self.assertTrue(type(res.json()["responseTime"]) == int, msg="时间戳类型断言失败")
        # print(res.json()["webNotes"])
        self.assertIn('noteId', str(res.json()["webNotes"]), msg="noteId字段断言失败")

    def testCase02_updateNoteSubject_major(self):
        """上传/更新便签信息主体_主流程"""
        host = "http://note-api.wps.cn"
        path = "/v3/notesvr/set/noteinfo"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        data = {
            "noteId": "ab24da4d69de56b219efeb08af8949ed",
            "star": "9527",
            "remindTime": "1722309544",
            "remindType": "0",
            "groupId": "14ac6a40b8270bd0d9cc46e6a4db9472"
        }
        res = requests.post(url, headers=headers, json=data)
        # print(res.json())
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
        self.assertIn('infoVersion', str(res.json()), msg="infoVersion字段断言失败")

    def testCase03_updateNoteContent_major(self):
        """上传/更新便签内容_主流程"""
        host = "http://note-api.wps.cn"
        path = "/v3/notesvr/set/notecontent"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        data = {
            "noteId": "81699a386cf05f1c94f09032bd54301e",
            "title": "tCIzAHOuVrb88Q5/74qwgQ==",
            "summary": "ozxMCwC2na8/6IRTteKxVGshh/aqRz77dWlJ4EP2LKY=",
            "body": "ozxMCwC2na8/6IRTteKxVLbIt+MdOg45sEkXG7LMzWg=",
            "localContentVersion": "21",
            "BodyType": "0"
        }
        res = requests.post(url, headers=headers, json=data)
        # print(res.json())
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
        self.assertIn('contentVersion', str(res.json()), msg="contentVersion字段断言失败")

    def testCase04_getNoteContent_major(self):
        """获取便签内容_主流程"""
        host = "http://note-api.wps.cn"
        path = "/v3/notesvr/get/notebody"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        data = {
            "noteIds": [
                "81699a386cf05f1c94f09032bd54301e"
            ]
        }
        res = requests.post(url, headers=headers, json=data)
        # print(res.json())
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
        self.assertIn('noteBodies', str(res.json()), msg="noteBodies字段断言失败")
        self.assertFalse(res.json()['noteBodies'] == [], msg="noteBodies不为空断言失败")

    def testCase05_deleteNote_major(self):
        """删除便签_主流程"""
        host = "http://note-api.wps.cn"
        path = "/v3/notesvr/delete"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        data = {
            "noteId": "5c59202c72530bf3631337d7bf8a2f72"
        }
        res = requests.post(url, headers=headers, json=data)
        # print(res.json())
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
        self.assertIn('responseTime', str(res.json()), msg="responseTime字段断言失败")

    def testCase06_getNoteGroupList_major(self):
        """获取分组列表_主流程"""
        host = "http://note-api.wps.cn"
        path = "/v3/notesvr/get/notegroup"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        data = {
            "excludeInvalid": "false"
        }
        res = requests.post(url, headers=headers, json=data)
        # print(res.json())
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
        self.assertFalse(res.json()['noteGroups'] == [], msg="noteGroups不为空断言失败")

    def testCase07_addNoteGroup_major(self):
        """新增分组_主流程"""
        host = "http://note-api.wps.cn"
        path = "/v3/notesvr/set/notegroup"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        data = {
            "groupId": "groupId_123",
            "groupName": "新增接口新增的分组123",
            "order": 9527
        }
        res = requests.post(url, headers=headers, json=data)
        # print(res.json())
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
        self.assertIn('responseTime' and 'updateTime', str(res.json()), msg="responseTime和updateTime字段断言失败")

    def testCase08_getGroupNoteList_major(self):
        """查看分组下便签_主流程"""
        host = "http://note-api.wps.cn"
        path = "/v3/notesvr/web/getnotes/group"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        data = {
            "groupId": "14ac6a40b8270bd0d9cc46e6a4db9472",
            "startIndex": 0,
            "rows": 0
        }
        res = requests.post(url, headers=headers, json=data)
        # print(res.json())
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
        self.assertFalse(res.json()['webNotes'] == [], msg="webNotes不为空断言失败")
        self.assertIn('noteId', str(res.json()), msg="noteId字段断言失败")

    def testCase09_deleteGroup_major(self):
        """删除分组_主流程"""
        host = "http://note-api.wps.cn"
        path = "/notesvr/delete/notegroup"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        data = {
            "groupId": "groupId_123"
        }
        res = requests.post(url, headers=headers, json=data)
        # print(res.json())
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
        self.assertIn('responseTime', str(res.json()), msg="responseTime字段断言失败")

    def testCase10_getCalendarNote_major(self):
        """查看日历下便签_主流程"""
        host = "http://note-api.wps.cn"
        path = "/v3/notesvr/web/getnotes/remind"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        data = {
            "remindStartTime": "1719815194",
            "remindEndTime": "1722493594",
            "startIndex": "0",
            "rows": "10"
        }
        res = requests.post(url, headers=headers, json=data)
        # print(res.json())
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
        self.assertFalse(res.json()['webNotes'] == [], msg="webNotes不为空断言失败")
        self.assertIn('noteId', str(res.json()), msg="noteId字段断言失败")

    def testCase11_getRecycleNoteList_major(self):
        """查看回收站下便签列表_主流程"""
        userid = "429577729"
        startindex = "0"
        rows = "10"
        host = "http://note-api.wps.cn"
        path = f"/v3/notesvr/user/{userid}/invalid/startindex/{startindex}/rows/{rows}/notes"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        res = requests.get(url, headers=headers)
        # print(res.json())
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
        self.assertFalse(res.json()['webNotes'] == [], msg="webNotes不为空断言失败")
        self.assertIn('noteId', str(res.json()), msg="noteId字段断言失败")

    def testCase12_restoreRecycleNote_major(self):
        """恢复回收站的便签_主流程"""
        host = "http://note-api.wps.cn"
        userid = "429577729"
        path = f"/v3/notesvr/user/{userid}/notes"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        data = {
            "userId": 429577729,
            "noteIds": [
                "cffdc863523836b2a3a0daa5eb425d3a"
            ]
        }
        res = requests.patch(url, headers=headers, json=data)
        # print(res.json())
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")

    def testCase13_deleteRecycleNote_major(self):
        """删除/清空回收站便签_主流程"""
        host = "http://note-api.wps.cn"
        path = "/v3/notesvr/cleanrecyclebin"
        url = host + path
        headers = {
            "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601",
            "X-User-Key": "429577729"
        }
        data = {
            "noteIds": [
                "5c59202c72530bf3631337d7bf8a2f72"
            ]
        }
        res = requests.post(url, headers=headers, json=data)
        # print(res.json())
        self.assertTrue(res.status_code == 200, msg="状态码断言失败")
        self.assertIn('responseTime', str(res.json()), msg="responseTime字段断言失败")

