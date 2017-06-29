# 用来存储字典
infor_list = []


def Name_Card():
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
            find_card()
        elif M == '5':
            show()
        elif M == '6':
            x = input("你确定要退出系统吗？ yes or no")
            if x == 'yes':
                print("退出系统中..........")
                break
        else:
            print("请输入有误,请重新输入")


def show():
    # 显示所有名片
    print('序号\t\t姓名\t\t年龄\t\tqq\t\t手机号\t\t')
    i = 0
    for temp in infor_list:
        print('%d\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t' % (i, temp['name'], temp['age'], temp['qq'], temp['tel']))
        i += 1


def find_card():
    # 查询名片
    name = input("输入你要查询的名片")
    for dir in infor_list:
        if dir['name'] == name:
            print('姓名\t 年龄\t qq\t 手机号\t')
            print('%s\t %s\t %s\t %s\t' % (dir['name'], dir['age'], dir['qq'], dir['tel']))
            break


def rename():
    # 修改名片
    print("-"*15)
    print('-'*5, '正在进行修改操作', '-'*5)
    id = int(input("输入要修改的名片:"))
    new_name = input("输入新的姓名:")
    infor_list[id]['name'] = new_name


def add_card():
    # 添加名片
    global infor_list
    print('-'*5, '正在进行添加操作', '-'*5)
    infor = {}
    new_name = input("请输入姓名:")
    new_age = input("请输入年龄:")
    new_qq = input("请输入qq:")
    new_tel = input("请输入手机号:")
    infor['name'] = new_name
    infor['age'] = new_age
    infor['qq'] = new_qq
    infor['tel'] = new_tel
    infor_list.append(infor)


def del_card():
    # 删除名片
    global infor_list
    print('-'*5, '正在进行删除操作！！！！！', '-'*5)
    print('序号\t 姓名\t 年龄\t qq\t 手机号\t')
    i = 0
    for dir in infor_list:
        print('%d\t %s\t %s\t %s\t %s\t' % (i, dir['name'], dir['age'], dir['qq'], dir['tel']))
    i += 1
    del_dir = int(input("输入要删除的名片:"))
    Q = input("你确定要删除吗？ yes or no")
    if Q == 'yes':
        del infor_list[del_dir]
        print("名片%d删除成功" % del_dir)

