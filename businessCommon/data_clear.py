import requests


class ClearData():
    host = 'http://note-api.wps.cn'

    @staticmethod
    def clear_groups(user_id, wps_sid):
        """
        清理用户名下的分组
        :param user_id: 用户id
        :param wps_sid: 用户身份标识
        :return:
        """
        get_group_url = ClearData.host + "/v3/notesvr/get/notegroup"
        delete_group_url = ClearData.host + "/notesvr/delete/notegroup"
        headers = {
            'Cookie': f'wps_sid = {wps_sid}',
            'X-User-Key': f'{user_id}'
        }

        # 查询当前用户名下所有分组信息
        data = {
            "excludeInValid": True
        }
        res = requests.post(get_group_url, headers=headers, json=data)
        # print(res.text)
        d_groups = []  # 定义空列表存储groupId
        for group in res.json()['noteGroups']:
            if group['valid'] == 1:
                d_groups.append(group['groupId'])

        # 遍历所有groupId去请求删除分组接口
        for group_id in d_groups:
            requests.post(delete_group_url, headers=headers, json={'groupId': group_id})

        return 'msg：groups clear successfully!'

    @staticmethod
    def clear_notes(user_id, wps_sid):
        """
        清理用户名下的便签
        :param user_id: 用户id
        :param wps_sid: 用户身份标识
        :return:
        """
        userid = user_id
        startindex = 0
        rows = 999
        delete_note_url = ClearData.host + '/v3/notesvr/delete'
        get_note_url = ClearData.host + f'/v3/notesvr/user/{userid}/home/startindex/{startindex}/rows/{rows}/notes'
        headers = {
            'Cookie': f'wps_sid = {wps_sid}',
            'X-User-Key': f'{user_id}'
        }
        g_res = requests.get(get_note_url, headers=headers)
        # return g_res.json()
        # d_note_ids = []
        for noteId in g_res.json()['webNotes']:
            # d_note_ids.append(noteId['noteId'])
            d_res = requests.post(delete_note_url, headers=headers, json={'noteId': noteId['noteId']})
            # print(d_res.json())


    @staticmethod
    def clear_recycle(user_id, wps_sid):
        userid = user_id
        startindex = 0
        rows = 999
        get_recycle_url = ClearData.host + f'/v3/notesvr/user/{userid}/invalid/startindex/{startindex}/rows/{rows}/notes'
        delete_recycle_url = ClearData.host + '/v3/notesvr/cleanrecyclebin'
        headers = {
            'Cookie': f'wps_sid = {wps_sid}',
            'X-User-Key': f'{user_id}'
        }
        res = requests.get(get_recycle_url, headers=headers)
        # print(res.json())
        noteIds = []
        for noteInfo in res.json()['webNotes']:
            noteIds.append(noteInfo['noteId'])
        # print(noteIds)
        data = {
            'noteIds': noteIds
        }
        if noteIds == []:
            return '回收站里没有数据'
        else:
            res = requests.post(delete_recycle_url, headers=headers, json=data)
            return res.json()
        # return res.json()


if __name__ == '__main__':
    # result1 = ClearData.clear_groups(429577729, 'V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601')
    result2 = ClearData.clear_notes(429577729, 'V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601')
    # result3 = ClearData.clear_recycle(429577729, 'V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601')
    # print(result1)
    print(result2)
    # print(result3)
