"""数据库版名片"""
import time
from pymysql import *
import hashlib


class start(object):
    def __init__(self):
        self.database = Database()
        self.user_name = None
        self.user_password = None

    def main(self):
        print("-"*5, 'Hello,World', '-'*5)
        print('用户注册:1\n用户登陆:2\n')
        N = int(input("输入要选择的操作:"))
        if N == 1:
            self.New_User()
        elif N == 2:
            self.landing()
        else:
            print("输入有误，请重新输入")

    def New_User(self):
        """用户注册系统"""
        temp = []
        print("欢迎注册成为Hello,World世界的一员")
        new_name = input('用户名:')
        password = input('密码:')
        hash_password = hashlib.md5(password.encode('utf-8'))
        temp.append(new_name, hash_password)
        # 将数据写入数据库
        self.database.insert_data(True, temp)

    def landing(self):
        """用户登陆
            查找数据库中是否存在此用户
        """
        user_name = input("请输入用户名:")
        user_password = input("请输入密码:")
        # 将密码转换为哈希加密
        hash_password = hashlib.md5(user_password.encode('utf-8'))
        temp = []
        temp.append(user_name, hash_password)
        result = Database.select_data(True, temp)
        if result:
            self.user_name = user_name
            self.user_password = hash_password
            self.success()
        else:
            print('用户名或密码有误,请重新输入')

    def success(self):
        # 登陆成功后跳转到此
        print("-"*5, '%s登陆中' % self.user_name, '-'*5)
        print("用户管理:1\t名片管理系统:2\t")
        select = int(input("请选择你的操作:"))
        if select == 1:
            admin = Admin(self.user_name, self.user_password)
        elif select == 2:
            name_card = Name_Card()
            name_card()
        else:
            print("输入有误")


class Admin(object):

    def __init__(self, user_name, user_password):
        self.database = Database()
        self.user_name = user_name
        self.user_password = user_password

    def admin(self):
        # 用户管理操作
        # 修改密码，修改用户名
        print("修改用户名:1\t修改密码:2\t删除用户:3\t返回:4\t")
        select = int(input('请输入你的操作:'))
        if select == 1:
            new_name = input("请输入新的用户名:")
            temp = []
            temp.append(self.user_name, new_name)
            self.database.update_data(False, temp)
        elif select == 2:
            old_password = input('请输入确认密码:')
            hash_password = hashlib.md5(old_password.encode('utf-8'))
            if hash_password == self.user_password:
                new_password = input('输入新的密码:')
                temp = []
                temp.append(self.user_password, new_password)
                self.database.update_data(False, temp)
            else:
                print('密码错误')
        elif select == 3:
            pass
        elif select == 4:
            pass
        else:
            print("输入有误")

    def del_user(self):
        """删除用户"""
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


class Name_Card(object):
    # 加载数据
    read_card_data()
    # 名片系统
    while True:
        print("-"*15)
        print("添加名片:1\n删除名片:2\n修改名片:3\n查询名片:4\n显示所有的名片:5\n退出系统:6\n")
        M = input("输入要选择的操作：")
        if M == '1':
            add_card()
        elif M == '2':
            del_card()
        elif M == '3':
            rename()
        elif M == '4':
            read_card_data()
            find_card()
        elif M == '5':
            read_card_data()
            show()
        elif M == '6':
            x = input("你确定要退出系统吗？ yes or no")
            if x == 'yes':
                card_data()
                print("退出系统中..........")
                break
        else:
            print("请输入有误,请重新输入")

    def show(self):
        # 显示所有名片
        print('序号\t\t姓名\t\t年龄\t\tqq\t\t手机号\t\t')
        i = 0
        for temp in info_list:
            print('%d\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t' % (i, temp['name'], temp['age'], temp['qq'], temp['tel']))
            i += 1

    def find_card(self):
        # 查询名片
        name = input("输入你要查询的名片")
        for dir in info_list:
            if dir['name'] == name:
                print('姓名\t年龄\tqq\t手机号\t')
                print('%s\t\t%s\t\t%s\t\t%s\t\t' % (dir['name'], dir['age'], dir['qq'], dir['tel']))
                break

    def rename(self):
        # 修改名片
        print("-"*15)
        print('-'*5, '正在进行修改操作', '-'*5)
        old_name = input("输入要修改的名片:")
        new_name = input("输入新的姓名:")
        for dir in info_list:
            if dir['name'] == old_name:
                dir['name'] = new_name
                card_data()

    def add_card(self):
        # 添加名片
        global info_list
        print('-'*5, '正在进行添加操作', '-'*5)
        info = {}
        new_name = input("请输入姓名:")
        new_age = input("请输入年龄:")
        new_qq = input("请输入qq:")
        new_tel = input("请输入手机号:")
        info['name'] = new_name
        info['age'] = new_age
        info['qq'] = new_qq
        info['tel'] = new_tel
        info_list.append(info)
        card_data()

    def del_card(self):
        # 删除名片
        global info_list
        print('-'*5, '正在进行删除操作！！！！！', '-'*5)
        print('序号\t 姓名\t 年龄\t qq\t 手机号\t')
        i = 0
        for dir in info_list:
            print('%d\t %s\t %s\t %s\t %s\t' % (i, dir['name'], dir['age'], dir['qq'], dir['tel']))
            i += 1
        del_dir = input("输入要删除的名片:")
        Q = input("你确定要删除吗？ yes or no")
        if Q == 'yes':
            i = -1
            for dir in info_list:
                i += 1
                if dir['name'] == del_dir:
                    del info_list[i]
                    card_data()
                    print("名片%s删除成功" % del_dir)

    def card_data(self):
        # 名片文件
        f = open('card_data.txt', 'w')
        f.write(str(info_list))
        f.close()

    def read_card_data(self):
        global info_list
        r = open('card_data.txt')
        info_list = eval(r.read())
        r.close()


class Database(object):
    """数据库操作
        1.一个存储名片
        2.一个存储用户信息
    """
    conn = connect(host='127.0.0.1', port=3306, user='root', password='809588434', database='lsjop', charset='utf8')
    cur = conn.cursor()

    def insert_data(self, bool, temp):
        """插入数据
            1.True 为user操作
            2.False 为card
        """
        try:
            if bool:
                sql = 'insert into user (name,password) values (%s,%s)'
                self.cur.execute(sql, temp)
                self.cur.close()
            else:
                pass
        except Exception as e:
            print(e)

    def delete_data(self, bool):
        """删除数据（逻辑删除）"""
        pass

    def update_data(self, bool):
        """更改数据"""
        try:
            if bool:
                pass
            else:
                pass
        except Exception as e:
            print(e)


    def select_data(self, bool, temp):
        """查询数据"""
        try:
            if bool:
                sql = 'select name,password from user where name = % , password = %'
                count = self.cur.execute(sql, temp)
                result = self.cur.fetchone()
                if result[0] == temp[0] and result[1] == temp[1]:
                    return True
                else:
                    return False
            else:
                pass
        except Exception as e:
            print(e)

if __name__ == '__main__':
    pass
