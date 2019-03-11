# -*- coding: utf-8 -*-

# @Time    : 2018/12/4 10:48
# @Author  : songq001
# @Comment : 全局配置文件，配置全局变量

import os
import hashlib

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True                    # 自动提交
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'                 # #这个类似于主题概要的意思，但不是主题，只是在主题前面加个修饰前缀
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'    # 这个是发件人，而<>前面的内容，实际上就相当于昵称的作用
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')           # 这里意思是指管理员是谁，其实这个FLASKY_ADMIN随便改成什么都可以

    # oracle配置
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    SQLALCHEMY_POOL_SIZE = 20       # 数据库连接池的大小。默认是引擎默认值（通常 是 5 ），此处最重要。
    SQLALCHEMY_POOL_TIMEOUT = 10     # 指定数据库连接池的超时时间。默认是10s。
    SQLALCHEMY_POOL_RECYCLE = 3000  # 配置连接池的 recyle 时间。默认是7200s。
    SECRET_KEY = os.environ.get('SECRET_KEY') or hashlib.new(name='md5', string='ousi keji hawk@#').hexdigest()
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    OUSI_POSTS_PER_PAGE = 100

    # msp相关配置
    mps_baseUrl = "https://msp-di1.dev.cmrh.com"
    mps_uri = "RH_MSPSERVER"
    pingAn = "https://pabo2o.pingan.com.cn/m/api"
    jinKong = "http://jzhongb.jzbncp.com/jinzhongbao/jzb_wx"

    @staticmethod
    # 此注释可表明使用类名可以直接调用该方法
    def init_app(app):  # 执行当前需要的环境的初始化
        pass


class DevelopmentConfig(Config):  # 开发环境
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'oracle+cx_oracle://' + os.path.join(basedir, 'data-dev.oracle')      # oracle://scott:redhat@192.168.0.107:1521/xe
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):     # 测试环境
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'oracle://' + os.path.join(basedir, 'data-test.oracle')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'oracle+cx_oracle://testmgr:%s@FTSZ-NB0045.cmrh.com:1521/testmgr' % 'test2018'


class ProductionConfig(Config):  # 生产环境
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'oracle+cx_oracle://' + os.path.join(basedir, 'data.oracle')


config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
        }

