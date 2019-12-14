import acm

from config.config import ServerConfig
from config.config_model import ConfigOperator
from fishbase.fish_logger import logger as log

from config.config_model import ConfigOperator


class ACMConfigManager(ConfigOperator):
    # ACM的配置
    acm_sdk_config = dict()
    server_config = dict()

    @staticmethod
    def load(config_name=None):
        server_config = ServerConfig()

        server_status = server_config.dt['server']['status']
        ACMConfigManager.acm_sdk_config = server_config.d[server_status]
        pass

    @staticmethod
    def save(config_model):
        raise SyntaxError('ACMConfigManager: ACM not support write config')

    @staticmethod
    def load_config_from_acm():
        if ACMConfigManager.acm_sdk_config is not None:
            _acm = acm.ACMClient(ACMConfigManager.acm_sdk_config['endpoint'],
                                 ACMConfigManager.acm_sdk_config['namespace'],
                                 ACMConfigManager.acm_sdk_config['ak'],
                                 ACMConfigManager.acm_sdk_config['sk'])
        else:
            print('error')
            log.warning('ACM configuration not found in config file')
            return None

        config_str = _acm.get(ACMConfigManager.acm_sdk_config['data_id'],
                              ACMConfigManager.acm_sdk_config['group'])
        print(config_str)


if __name__ == '__main__':
    print("aaaaa")
    ACMConfigManager.load()
    ACMConfigManager.load_config_from_acm()
