import inspect
import os.path
import functools
from datetime import datetime
from colorama import Fore
from main import DIR


def info(text):
    """
    info级别日志输出方法
    :param text:
    :return:
    """
    stack = inspect.stack()
    formatted_time = datetime.now().strftime('%H:%M:%S:%f')[:-3]  # 定义日志输出时间
    code_path = f'{os.path.basename(stack[1].filename)}:{stack[1].lineno}'  # 当前执行文件的绝对路径和执行代码行号
    content = f'[INFO]{formatted_time}-{code_path} >> {text}'
    print(Fore.LIGHTGREEN_EX + content)
    str_time = datetime.now().strftime('%Y%m%d')
    with open(file=DIR + '\\logs\\' + f'{str_time}_info.log', mode='a', encoding='utf-8') as f:
        f.write(content + '\n')


def error(text):
    """
    error级别日志输出方法
    :param text:
    :return:
    """
    stack = inspect.stack()
    formatted_time = datetime.now().strftime('%H:%M:%S:%f')[:-3]  # 定义日志输出时间
    code_path = f"{os.path.basename(stack[1].filename)}:{stack[1].lineno}"  # 当前执行文件的绝对路径和执行代码行号
    content = f"[ERROR]{formatted_time}-{code_path} >> {text}"
    print(Fore.LIGHTRED_EX + content)
    str_time = datetime.now().strftime("%Y%m%d")
    with open(file=DIR + '\\logs\\' + f'{str_time}_info.log', mode='a', encoding='utf-8') as f:
        f.write(content + '\n')
    with open(file=DIR + '\\logs\\' + f'{str_time}_error.log', mode='a', encoding='utf-8') as f:
        f.write(content + '\n')


def step(text):
    """
    自定义step级别日志输出方法
    :param msg:
    :return:
    """
    stack = inspect.stack()
    formatted_time = datetime.now().strftime('%H:%M:%S:%f')[:-3]  # 定义日志输出时间
    code_path = f"{os.path.basename(stack[1].filename)}:{stack[1].lineno}"  # 当前执行文件的绝对路径和执行代码行号
    content = f"[STEP]{formatted_time}-{code_path} >> {text}"
    print(Fore.LIGHTCYAN_EX + content)
    str_time = datetime.now().strftime("%Y%m%d")
    with open(file=DIR + '\\logs\\' + f'{str_time}_info.log', mode='a', encoding='utf-8') as f:
        f.write(content + '\n')


def case_log_init(func):
    @functools.wraps(func)  # 解决参数冲突问题
    def inner(*args, **kwargs):
        class_name = args[0].__class__.__name__  # 获取类名
        method_name = func.__name__  # 获取方法名
        docstring = inspect.getdoc(func)  # 获取方法注释
        print(Fore.LIGHTRED_EX + '----------------------------------------------------------------------')
        # step(f"Method Name:{method_name}, Class Name:{class_name}")
        step(f'[测试类]：{class_name}')
        step(f'[测试用例]：{method_name}')
        step(f"[用例描述]:{docstring}")
        func(*args, **kwargs)

    return inner

def class_case_log(cls):
    """
    用例的日志装饰器级别
    :param cls:
    :return:
    """
    for name, method in inspect.getmembers(cls, inspect.isfunction):
        if name.startswith('testCase'):
            setattr(cls, name, case_log_init(method))
    return cls




if __name__ == '__main__':
    info('哈哈哈叼毛')
    step('嘻嘻嘻叼毛')
    error('嘻嘻哈哈叼毛')
