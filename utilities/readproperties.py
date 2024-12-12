import configparser
import os
import time

config = configparser.ConfigParser()
filepath="C:\\Users\\usha5\\pycharmprojects\\PracticeProject2\\configurations\\config.ini"
config.read(filepath)

class readconfig:

    @staticmethod
    def get_url() :
        url = config.get('commonInfo','baseURL')
        return url

    @staticmethod
    def get_password():
        pword = config.get('commonInfo','password')
        return pword
