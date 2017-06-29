# -*- coding:utf-8 -*-
import time
from card import Name_Card
"""
编写程序，完成“名片管理器”项目
需要完成的基本功能：
添加名片
删除名片
修改名片
查询名片
退出系统
程序运行后，除非选择退出系统，否则重复执行功能
增强的功能:
用户登陆
新注册用户
用户管理(密码修改和修改用户名)
"""

# 用户名和密码
user_password = []

def start():
    # 管理
    print("-"*5, 'Hello,World', '-'*5)
    print('用户注册:1\n用户登陆:2\n')
    N = int(input("输入要选择的操作:"))
    if N == 1:
        New_User()
    elif N == 2:
        landing()
    else:
        print("输入有误，请重新输入")


def New_User():
    # 用户注册系统
    temp = {}
    print("欢迎注册成为Hello,World世界的一员")
    New_Name = input('用户名:')
    Passwd = input('密码:')
    temp[New_Name] = Passwd
    user_password.append(temp)
    print("%s 注册成功" % New_Name)
    print(user_password)
    return start()

def admin():
    # 用户管理操作
    # 修改密码，修改用户名
    # 修改完毕将列表中的老用户和密码删除，使用列表遍历然后if进行判断，最后通过下标删除
    global user_name, user_password
    print("修改用户名:1\t修改密码:2\t删除用户:3\t返回:4\t")
    select = int(input('请输入你的操作:'))
    i = -1
    for temp in user_password:
        i += 1
        for key, value in temp.items():
            user = key
            passwd = value
            if user == user_name:
                old_passwd = value
            if select == 1:
                temp_dir ={}
                print("当前用户%s" % user_name)
                new_user = input("输入新的用户名")
                temp_dir[new_user] = old_passwd
                del user_password[i]
                user_password.append(temp_dir)
            elif select == 2:
                temp = {}
                print('当前用户名%s' % user_name)
                new_passwd = input("请输入新的密码:")
                temp[user_name] = new_passwd
                del user_password[i]
                user_password.append(temp)
            elif select == 3:
                return del_user()
            elif select == 4:
                return start()
            else:
                print('输入错误')
            return start()

def success():
    # 登陆成功后跳转到此
    print("-"*5, '%s登陆中' % user_name, '-'*5)
    print("用户管理:1\t名片管理系统:2\t")
    select = int(input("请选择你的操作:"))
    if select == 1:
        admin()
    elif select == 2:
        Name_Card()
    else:
        print("输入有误")


def landing():
    # 用户登陆系统
    # 用来存储登陆信息
    # 验证密码
    # 将dir提取出来然后进行if判断,先判断用户名存不存在，如果存在进行密码判断
    global user_name
    user_name = input("请输入用户名:")
    user_passwd = input("请输入密码:")
    for temp in user_password:
        for key, value in temp.items():
            user = key
            passwd = value
            if user == user_name:
                if user_passwd == passwd:
                    print("登陆成功跳转中")
                    i = 0
                    while True:
                        time.sleep(0.1)
                        # print('>', end='')
                        i += 1
                        if i == 10:
                            success()
                else:
                    print("密码错误")
            else:
                print("用户不存在")

def del_user():
    # 删除用户
    print("!"*5, '请小心操作', '!'*5)
    passwd = input("请输入密码确认:")
    i = -1
    for temp in user_password:
        i += 1
        for key, value in temp.items():
            user = key
            old_passwd = value
            if user == user_name and old_passwd == passwd:
                del user_password[i]
                time.sleep(1)
                print('删除成功')
                print('即将跳转至主界面')
                time.sleep(2)
                start()
            else:
                print('密码错误')


if __name__ == '__main__':
    start()
