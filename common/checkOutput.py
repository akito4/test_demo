import unittest


class CheckPro(unittest.TestCase):
    def check_output(self, expected, actual):
        # 判断返回字段数量是否与期望一致
        self.assertEqual(len(expected.keys()), len(actual.keys()), msg=f'{actual.keys()} key长度与期望长度不一致！')
        # 遍历期望值（dict）获取每个字段和值
        for key, value in expected.items():
            # print(value)
            # 遍历所有返回字段，判断是否存在期望值中
            self.assertIn(key, actual.keys(), msg=f'缺少{key}字段！')
            # 校验所传期望字段的值是否为type
            if isinstance(value, type):
                # 校验所传字段的值的类型是否为期望的类型
                self.assertEqual(value, type(actual[key]), msg=f'{key}字段的类型与期望类型不一致！')
            # 校验所传期望字段的值是否为dict（json）
            elif isinstance(value, dict):
                # 递归调用check_output()
                self.check_output(value, actual[key])
            # 校验所传期望字段的值是否为list（array）
            elif isinstance(value, list):
                # print('?',value, actual[key])
                # print('=======================')
                # 校验数组中的字段数是否与期望数一致
                # ======================== 这里有bug ========================
                self.assertEqual(len(value), len(actual[key]), msg=f'{actual.keys()} 这个数组下的字段数与期望数不一致！')

                # 对数组中每个元素进行类型校验或进一步的字典校验
                for list_index in range(len(value)):
                    # 遍历所传期望字段中数组下的子字段的值是否为type
                    if isinstance(value[list_index], type):
                        self.assertEqual(value[list_index], type(actual[key][list_index]), msg=f'{value[list_index]}字段的值不是数据类型！')
                    # 校验数组中字段的类型是否为dict（json）
                    elif isinstance(value[list_index], dict):
                        # 递归调用check_output()
                        self.check_output(value[list_index], actual[key][list_index])
                    else:
                        # 校验数组中的元素是否与期望的元素一致
                        self.assertEqual(value[list_index], actual[key][list_index], msg=f'{value[list_index]}字段的值与期望值不一致！')
            else:
                self.assertEqual(value, actual[key], msg=f'{key} 字段的值与期望值不一致！')



# # 测试用例部分
# class TestCheckPro(unittest.TestCase):
#     def setUp(self):
#         self.checker = CheckPro()
#
#     # def testCase01_exact_match(self):
#     #     expected = {
#     #         'order_id': str,
#     #         'status': str,
#     #         'items': list
#     #     }
#     #     actual = {
#     #         'order_id': '123',
#     #         'status': 'completed',
#     #         'items': [
#     #             {'item_id': '001', 'quantity': 1},
#     #             {'item_id': '002', 'quantity': 2}
#     #         ]
#     #     }
#     #     self.checker.check_output(expected, actual)
#
#     def testCase02_type_match(self):
#         expected = {
#             'order_id': str,
#             'status': str,
#             'items': [
#                 {'item_id': str, 'quantity': int},
#                 {'item_id': str, 'quantity': int}
#             ]
#         }
#         actual = {
#             'order_id': '123',
#             'status': 'completed',
#             'items': [
#                 {'item_id': '001', 'quantity': 1},
#                 {'item_id': '002', 'quantity': 2}
#             ]
#         }
#         self.checker.check_output(expected, actual)
#     #
#     # def testCase03_inconsistent_keys(self):
#     #     expected = {
#     #         'order_id': '123',
#     #         'status': 'completed'
#     #     }
#     #     actual = {
#     #         'order_id': '123'
#     #     }
#     #     with self.assertRaises(AssertionError):
#     #         self.checker.check_output(expected, actual)
#     #
#     # def testCase04_inconsistent_values(self):
#     #     expected = {
#     #         'order_id': int,
#     #         'status': 'completed'
#     #     }
#     #     actual = {
#     #         'order_id': '123',
#     #         'status': 'pending'
#     #     }
#     #     with self.assertRaises(AssertionError):
#     #         self.checker.check_output(expected, actual)
#     #
#     # def testCase05_nested_structure(self):
#     #     expected = {
#     #         'order_id': '123',
#     #         'details': {
#     #             'shipping': {'address': '123 Street', 'city': 'CityName'},
#     #             'items': [{'item_id': '001', 'quantity': 1}]
#     #         }
#     #     }
#     #     actual = {
#     #         'order_id': '123',
#     #         'details': {
#     #             'shipping': {'address': '123 Street', 'city': 'CityName'},
#     #             'items': [{'item_id': '001', 'quantity': 1}]
#     #         }
#     #     }
#     #     self.checker.check_output(expected, actual)
#
# if __name__ == '__main__':
#     unittest.main()
