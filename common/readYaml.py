from main import DIR, ENVIRON
import yaml

class ReadYaml:
    @staticmethod
    def env_config():
        """
        读取环境变量yml方法
        :return:
        """
        with open(file=f'{DIR}/config/env/{ENVIRON}/config.yml', mode='r', encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    @staticmethod
    def data_config():
        """
        读取请求参数yml方法
        :return:
        """
        with open(file=f'{DIR}/config/data/config.yml', mode='r', encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)