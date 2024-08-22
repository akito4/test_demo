# import unittest
#
#
# value = 123
# a = 123
#
# if isinstance(value, type):
#     print('嗯嗯')
# else:
#     print('八嘎')
#
# print(type)
#
# # b = [
# #       {
# #         "type": "home",
# #         "number": "123-456-7890"
# #       },
# #       {
# #         "type": "mobile",
# #         "number": "987-654-3210"
# #       }
# #     ]
# #
# # for index_list in range(len(b)):
# #     print(b[index_list])
# #     print(type(b[index_list]))
#
#
# class xixiTest(unittest.TestCase):
#
#
#     def check_output(self, expected, actual):
#         # 判断返回字段数量是否与期望一致
#         self.assertEqual(len(expected.keys()), len(actual.keys()), msg=f'{actual.keys()} key长度与期望长度不一致！')
#         # 遍历期望值（dict）获取每个字段和值
#         for key, value in expected.items():
#             # print(value)
#             # 遍历所有返回字段，判断是否存在期望值中
#             self.assertIn(key, actual.keys(), msg=f'缺少{key}字段！')
#             # 校验所传期望字段的值是否为type
#             if isinstance(value, type):
#                 self.assertEqual(value, type(actual[key]), msg=f'{key}字段类型与期望类型不一致！')
#             # 校验所传期望字段的值是否为dict（json）
#             elif isinstance(value, dict):
#                 # 递归调用check_output()
#                 self.check_output(value, actual[key])
#             # 校验所传期望字段的值是否为list（array）
#             elif isinstance(value, list):
#                 self.assertEqual(len(value), len(actual[key]), msg=f'{actual.keys()} 这个数组下的字段数与期望数不一致！')
#
#                 for list_index in range(len(value)):
#                     # 遍历所传期望字段中数组下的子字段的值是否为type
#                     if isinstance(value[list_index], type):
#                         # 校验数组下的子字段的值是否与期望一致
#                         self.assertEqual(value[list_index], type(actual[key][list_index]), msg=f'{value[list_index]}')
#
# class TestCheckPro(unittest.TestCase):
#     def setUp(self):
#         self.checker = xixiTest()
#
#     def testCase01_exact_match(self):
#         expected = {
#             'order_id': str,
#             'status': str,
#             'items': [
#                 {'item_id': int, 'quantity': 1},
#                 {'item_id': '002', 'quantity': 2}
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
#
#     def testCase03_inconsistent_keys(self):
#         expected = {
#             'order_id': '123',
#             'status': 'completed'
#         }
#         actual = {
#             'order_id': '123'
#         }
#         with self.assertRaises(AssertionError):
#             self.checker.check_output(expected, actual)
#
#     def testCase04_inconsistent_values(self):
#         expected = {
#             'order_id': int,
#             'status': 'completed'
#         }
#         actual = {
#             'order_id': '123',
#             'status': 'pending'
#         }
#         with self.assertRaises(AssertionError):
#             self.checker.check_output(expected, actual)
#
#     def testCase05_nested_structure(self):
#         expected = {
#             'order_id': '123',
#             'details': {
#                 'shipping': {'address': '123 Street', 'city': 'CityName'},
#                 'items': [{'item_id': '001', 'quantity': 1}]
#             }
#         }
#         actual = {
#             'order_id': '123',
#             'details': {
#                 'shipping': {'address': '123 Street', 'city': 'CityName'},
#                 'items': [{'item_id': '001', 'quantity': 1}]
#             }
#         }
#         self.checker.check_output(expected, actual)
#
# if __name__ == '__main__':
#     unittest.main()
