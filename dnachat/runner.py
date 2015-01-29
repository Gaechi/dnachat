from bynamodb import init_bynamodb
from twisted.internet import reactor

from .settings import conf
from .logger import init_logger


def run_dnachat(config_file='localconfig.py'):
    conf.load_from_file(config_file)
    init_bynamodb(conf)
    init_logger(conf['CHAT_LOG_FILE_NAME'], conf['LOG_LEVEL'])
    from dnachat.server import ChatFactory
    reactor.listenTCP(conf.get('PORT', 9339), ChatFactory(conf['REDIS_HOST']))
    reactor.run()


def run_logger(config_file='localconfig.py'):
    conf.load_from_file(config_file)
    init_bynamodb(conf)
    init_logger(conf['LOGGER_LOG_FILE_NAME'], conf['LOG_LEVEL'])
    from dnachat.logserver import ChatLogger
    ChatLogger(conf['REDIS_HOST']).start()


def run_notisender(config_file='localconfig.py'):
    conf.load_from_file(config_file)
    init_bynamodb(conf)
    init_logger(conf['NOTISENDER_LOG_FILE_NAME'], conf['LOG_LEVEL'])
    from dnachat.notiserver import NotificationSender
    NotificationSender().start()
