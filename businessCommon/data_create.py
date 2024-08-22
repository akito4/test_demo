import requests
import time


class CreateData():
    host = 'http://note-api.wps.cn'

    @staticmethod
    def create_groups(user_id, wps_sid):
        create_group_url = CreateData.host + "/v3/notesvr/set/notegroup"
        headers = {
            'Cookie': f'wps_sid = {wps_sid}',
            'X-User-Key': f'{user_id}'
        }
        group_id = 'xixi_' + str(int((time.time() * 1000)))
        data = {
            "groupId": group_id,
            "groupName": "创建一个用来删除的分组",
            "order": 0
        }
        res = requests.post(create_group_url, headers=headers, json=data)
        # print(res.json())
        return group_id

    @staticmethod
    def create_notes(user_id, wps_sid, star=None, remindTime=None, remindType=None, addGroupId=None, num=None):
        """
        构建便签数据
        :param user_id: 用户id，也是X-User-Key
        :param wps_sid: Cookie: wps_sid
        :param star: 是否标星：枚举值1是标星，0是不标星，默认值为0
        :param remindTime: 提醒时间
        :param remindType: 提醒类型：0不提醒，1提醒一次，2已经提醒
        :param addGroupId: 是否添加进分组：True-添加进分组，False：不添加进分组
        :param num: 创建便签数量
        :return:
        """
        create_note_info_url = CreateData.host + "/v3/notesvr/set/noteinfo"
        create_note_content_url = CreateData.host + "/v3/notesvr/set/notecontent"

        if num is not None:
            for i in range(num):
                headers = {
                    'Cookie': f'wps_sid = {wps_sid}',
                    'X-User-Key': f'{user_id}'
                }
                note_id = 'haha_' + str(int((time.time() * 1000)))
                # group_id = CreateData.create_groups(user_id, wps_sid)
                info_data = {
                    "noteId": note_id,
                }
                if star is not None:
                    info_data['star'] = star
                if remindTime is not None:
                    info_data['remindTime'] = remindTime
                if remindType is not None:
                    info_data['remindType'] = remindType
                if addGroupId is True:
                    group_id = CreateData.create_groups(user_id, wps_sid)
                    info_data['groupId'] = group_id
                elif addGroupId is not False:
                    raise ValueError("addGroupId 只能是 True 或 False")
                content_data = {
                    "noteId": note_id,
                    "title": "tCIzAHOuVrb88Q5/74qwgQ==",
                    "summary": "ozxMCwC2na8/6IRTteKxVGshh/aqRz77dWlJ4EP2LKY=",
                    "body": "ozxMCwC2na8/6IRTteKxVLbIt+MdOg45sEkXG7LMzWg=",
                    "localContentVersion": "1",
                    "BodyType": "0"
                }

                res_info = requests.post(create_note_info_url, headers=headers, json=info_data)
                res_info.raise_for_status()  # 确保请求成功
                res_content = requests.post(create_note_content_url, headers=headers, json=content_data)
                # print(res_content)
                res_content.raise_for_status()  # 确保请求成功


        else:
            headers = {
                'Cookie': f'wps_sid = {wps_sid}',
                'X-User-Key': f'{user_id}'
            }
            note_id = 'haha_' + str(int((time.time())))
            # group_id = CreateData.create_groups(user_id, wps_sid)
            info_data = {
                "noteId": note_id,
            }
            if star is not None:
                info_data['star'] = star
            if remindTime is not None:
                info_data['remindTime'] = remindTime
            if remindType is not None:
                info_data['remindType'] = remindType
            if addGroupId is True:
                group_id = CreateData.create_groups(user_id, wps_sid)
                info_data['groupId'] = group_id
            elif addGroupId is not False:
                raise ValueError("addGroupId 只能是 True 或 False")
            content_data = {
                "noteId": note_id,
                "title": "tCIzAHOuVrb88Q5/74qwgQ==",
                "summary": "ozxMCwC2na8/6IRTteKxVGshh/aqRz77dWlJ4EP2LKY=",
                "body": "ozxMCwC2na8/6IRTteKxVLbIt+MdOg45sEkXG7LMzWg=",
                "localContentVersion": "1",
                "BodyType": "0"
            }
            # print('info_data', info_data)
            # print('content_data', content_data)
            # res_info = requests.post(create_note_info_url, headers=headers, json=info_data)
            # # print(res.text)
            # res_content = requests.post(create_note_content_url, headers=headers, json=content_data)
            # return group_id, note_id  # tuple

            res_info = requests.post(create_note_info_url, headers=headers, json=info_data)
            res_info.raise_for_status()  # 确保请求成功
            res_content = requests.post(create_note_content_url, headers=headers, json=content_data)
            res_content.raise_for_status()  # 确保请求成功

        if addGroupId is True:
            return group_id, note_id
        else:
            return note_id

    # ==================== 废弃这个方法，调用这个方法的py文件全部需要修改 ====================
    # @staticmethod
    # def create_notes_not_group(user_id, wps_sid):
    #     create_note_info_url = CreateData.host + "/v3/notesvr/set/noteinfo"
    #     create_note_content_url = CreateData.host + "/v3/notesvr/set/notecontent"
    #     headers = {
    #         'Cookie': f'wps_sid = {wps_sid}',
    #         'X-User-Key': f'{user_id}'
    #     }
    #     note_id = 'haha_' + str(int((time.time())))
    #     # group_id = CreateData.create_groups(user_id, wps_sid)
    #     info_data = {
    #         "noteId": note_id
    #     }
    #     content_data = {
    #         "noteId": note_id,
    #         "title": "tCIzAHOuVrb88Q5/74qwgQ==",
    #         "summary": "ozxMCwC2na8/6IRTteKxVGshh/aqRz77dWlJ4EP2LKY=",
    #         "body": "ozxMCwC2na8/6IRTteKxVLbIt+MdOg45sEkXG7LMzWg=",
    #         "localContentVersion": "1",
    #         "BodyType": "0"
    #     }
    #     res_info = requests.post(create_note_info_url, headers=headers, json=info_data)
    #     # print(res.text)
    #     res_content = requests.post(create_note_content_url, headers=headers, json=content_data)
    #     return note_id


if __name__ == '__main__':
    # CreateData.create_groups(429577729, 'V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601')
    result = CreateData.create_notes(429577729, 'V02S8mjp4VpIXQMEm4Mnh-4zfVy476400a83278700199ad601')
    print(result)
    print(result[0])
