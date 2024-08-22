import unittest
import os
from BeautifulReport import BeautifulReport

DIR = os.path.dirname(os.path.abspath(__file__))
ENVIRON = 'prd'     # dev-开发环境  test-测试环境   prd-生产环境


if __name__ == '__main__':
    run_pattern = 'all'
    if run_pattern == 'all':    # all-全量用例执行  /  smoking-冒烟用例执行   /   指定执行文件
        pattern = 'test*.py'
    elif run_pattern == 'smoking':
        pattern = 'test_major*.py'
    else:
        pattern = run_pattern + '.py'

    suite = unittest.TestLoader().discover('./testcase', 'test*.py')

    result = BeautifulReport(suite)
    result.report(filename='reports.html', description='测试报告', report_dir='./')
    # runner = unittest.TextTestRunner()
    # runner.run(suite)