# Flask 用到的配置对象
import os

from fishbase import conf_as_dict, check_sub_path_create, re
from fishbase.fish_logger import logger as log, set_log_stdout
import fishbase.fish_file as fff
from fishbase.fish_logger import logger, set_log_file


class Config:
    """
    flask 的 Config class， 完成基础的 flask 各类配置
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'welcome to my config'
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """
    开发配置
    """
    DEBUG = True


# 测试配置
class TestingConfig(Config):
    """
    开发配置
    """
    DEBUG = True


class ProductConfig(Config):
    """
    生产配置
    """
    pass


class PressureTesting:
    """
    压测配置
    """
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'product': ProductConfig,
    'default': TestingConfig,
    'pressuretesting': PressureTesting
}
log.info('flask server conf setup ok')


class SingleTon(object):
    """
    单例
    """
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(SingleTon, cls).__new__(cls)
        ob.__dict__ = cls._state  # 类维护所有实例的共享属性
        return ob


class ServerConfig(SingleTon):
    """
    ServerConfig
    """
    server_conf_abs_filename = ''
    log_abs_filename = ''
    dt = {}

    def __init__(self):
        ServerConfig.create_need_abs_filename()  # 生成需要的各类绝对路径名称

        flag, ServerConfig.dt, count = conf_as_dict(
            # 读取 server conf 文件中的测试信息, 写入到 bankcard_man 的 dt 字典变量
            ServerConfig.server_conf_abs_filename)

        # 日志格式设置
        local_log_mode = ServerConfig.dt.get('server').get('log_mode')
        # 'logcat'为只在控制台输出日志
        if local_log_mode == 'logcat':
            set_log_stdout()
            logger.info('日志初始化完成，目前的日志模式为：%s，日志将只在控制台输出' % local_log_mode)
        # 'file'为日志文件输出
        elif local_log_mode == 'file':
            set_log_file(ServerConfig.log_abs_filename)
            logger.info('日志初始化完成，目前的日志模式为：%s，日志将只在日志文件输出' % local_log_mode)
        # 其他的统一输出为日志文件+logcat
        else:
            set_log_stdout()
            set_log_file(ServerConfig.log_abs_filename)
            logger.info('日志初始化完成，目前的日志模式为：%s，日志将在控制台及日志文件同时输出' % local_log_mode)

    @staticmethod
    def create_need_path():  # 创建应用程序所需要的基本路径
        check_sub_path_create('log')

    @staticmethod
    def create_need_abs_filename():  # 创建app使用的各个长文件名
        basedir = os.path.abspath(os.path.dirname(__file__))
        basedir = os.path.split(basedir)[0]
        ServerConfig.log_abs_filename = os.path.join(basedir, 'log', 'server.log')
        ServerConfig.server_conf_abs_filename = os.path.join(basedir, 'conf', 'config.conf')






