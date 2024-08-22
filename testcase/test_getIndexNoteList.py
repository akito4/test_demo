# import unittest
# import requests
# import time
# from businessCommon.data_create import CreateData
# from businessCommon.data_clear import ClearData
#
#
# class TestPro(unittest.TestCase):
#     userid = 429577729
#     wps_sid = "V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601"
#
#     def setUp(self) -> None:
#         # 前置清理首页便签数据并构造新便签数据获取note_id
#         ClearData.clear_notes(self.userid, self.wps_sid)
#         ClearData.clear_recycle(self.userid, self.wps_sid)
#         self.note_id = CreateData.create_notes(self.userid, self.wps_sid, addGroupId=False)
#         # print(note_id)
#
#     def testCase01_getIndexNoteList_major(self):
#         """
#         获取首页便签列表_主流程
#         :return:
#         """
#         host = "http://note-api.wps.cn"
#         userid = 429577729
#         startindex = 0
#         rows = 999
#         path = f"/v3/notesvr/user/{userid}/home/startindex/{startindex}/rows/{rows}/notes"
#         url = host + path
#         headers = {
#             "Cookie": "wps_sid=V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601"
#         }
#         res = requests.get(url, headers=headers)
#         # print(res.json())
#         r_json = res.json()
#         self.assertTrue(res.status_code == 200, msg="状态码断言失败")
#         self.assertEqual(self.note_id, r_json['webNotes'][0]['noteId'], msg='noteId断言失败')
#         self.assertEqual(1, r_json['webNotes'][0]['infoVersion'], msg='infoVersion断言失败')
#         self.assertEqual(2, len(r_json), msg='返回字段数 != 2')
#         self.assertEqual(13, len(r_json['webNotes'][0]), msg='webNotes数组返回字段数 != 13')
