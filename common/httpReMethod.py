import requests
from common.caseLogs import info, error, step


class BusinessRequest(object):
    @staticmethod
    def post(url, json=None, headers=None, sid=None, user_id=None, **kwargs):
        if headers:
            pass
        else:
            headers = {
                'Cookie': f'wps_sid={sid}',
                'X-User_key': f'{user_id}'
            }
        info(f'post url: {url}')
        info(f'post headers:{headers}')
        info(f'post body: {json}')
        try:
            res = requests.post(url, headers=headers, json=json, timeout=10, **kwargs)
        except TimeoutError:
            error('http request Timeout!')
            raise TimeoutError
        info(f'接口返回状态码：{res.status_code}')
        info(f'接口返回body：{res.text}')
        return res

    @staticmethod
    def get(url, headers=None, sid=None, user_id=None, **kwargs):
        if headers:
            pass
        else:
            headers = {
                'Cookie': f'wps_sid={sid}',
                'X-user-key': f'{user_id}'
            }
        info(f'get url: {url}')
        info(f'get headers:{headers}')
        try:
            res = requests.get(url,headers=headers,timeout=10, **kwargs)
        except TimeoutError:
            error('http request Timeout!')
            raise TimeoutError
        info(f'接口返回状态码：{res.status_code}')
        info(f'接口返回body：{res.text}')
        return res