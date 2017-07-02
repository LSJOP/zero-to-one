
"""
数据保存模块
"""

def passwd_data():
    # 密码文件
    f = open('passwd_data.data', 'w+')
    f.write(str(user_password))
    f.close()


def read_passwd_data():
    global  user_password
    r = open('passwd_data.data', 'w+')
    user_password = eval(r.read())
    r.close()


def card_data():
    # 名片文件
    f = open('card_data.data', 'w+')
    f.write(str(info_list))
    f.close()


def read_card_data():
    global info_list
    r = open('card_data.data', 'w+')
    info_list = eval(r.read())
    r.close()
