# test_api.py

import unittest
from jsonschema_assert import JSONSchemaValidator

class TestAPISchemaValidation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """定义 JSON Schema"""
        cls.schema = {
            "type": "object",
            "properties": {
                "responseTime": {"type": "integer"},
                "webNotes": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
               -             "noteId": {"type": "string"},
                            "createTime": {"type": "integer"},
                            "star": {"type": "integer"},
                            "remindTime": {"type": "integer"},
                            "remindType": {"type": "string"},
                            "infoVersion": {"type": "integer"},
                            "infoUpdateTime": {"type": "integer"},
                            "groupId": {"type": "string"},
                            "title": {"type": "string"},
                            "summary": {"type": "string"},
                            "thumbnail": {"type": ["string", "null"]},
                            "contentVersion": {"type": "integer"},
                            "contentUpdateTime": {"type": "integer"}
                        },
                        "required": [
                            "noteId",
                            "createTime",
                            "star",
                            "remindTime",
                            "remindType",
                            "infoVersion",
                            "infoUpdateTime",
                            "groupId",
                            "title",
                            "summary",
                            "thumbnail",
                            "contentVersion",
                            "contentUpdateTime"
                        ]
                    }
                }
            },
            "required": ["responseTime", "webNotes"]
        }
        cls.validator = JSONSchemaValidator(cls.schema)

    def test_api_response(self):
        """测试接口返回的 JSON 数据"""
        # 假设这是从 API 获取的响应数据
        api_response = {
            "responseTime": 0,
            "webNotes": [
                {
                    "noteId": "f045dc062cbc89e9201ea575be3e8e36",
                    "createTime": 1723208358990,
                    "star": 0,
                    "remindTime": 0,
                    "remindType": 0,
                    "infoVersion": 1,
                    "infoUpdateTime": 1723208358990,
                    "groupId": "xixi_1723196063284",
                    "title": "tCIzAHOuVrb88Q5/74qwgQ==",
                    "summary": "8Cq+VmmdLlGrvzUDQgKpXg==",
                    "thumbnail": None,
                    "contentVersion": 1,
                    "contentUpdateTime": 1723208359155
                }
            ]
        }

        # 使用封装的校验方法进行 JSON 数据校验
        is_valid, error_message = self.validator.validate(api_response)
        self.assertTrue(is_valid, error_message)

if __name__ == '__main__':
    unittest.main()