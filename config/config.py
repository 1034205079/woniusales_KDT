import logging
import os


class Config:
    project_path = os.path.split(os.path.split(__file__)[0])[0]
    keword_path = "woniusales_KDT.keyword"
    base_url = "http://192.168.12.51:8080"
    db_info = {"host": "localhost", "port": 7896, "user": "root", "password": "root", "db": "kdt_test"}
    logger_name = "woniusales"
    logger_level = logging.DEBUG
    mail_account = "2322537658@qq.com"
    mail_token = "11111"
    mail_smtp = "smtp.qq.com"
    mail_port = 465
    receive_mail = '1034205079@qq.com'
    receive_mail1 = '273950267@qq.com'



if __name__ == '__main__':
    print(Config.project_path)
