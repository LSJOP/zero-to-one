import os
"""
文件操作模块
"""
def file_data():
    # 获取要修改的文件名
    folder_name = input("输入文件夹名称:")
    while True:
            select = int(input("批量增加文件名:1\n批量删除文件名:2\n删除文件:3\n删除目录:4\n创建文件夹:5\n退出:6\n>"))
            # 将文件名导入
            file_name = os.listdir(folder_name)
            # 修改默认目录
            os.chdir(folder_name)
            if select == 1:
                new_file = input("输入要增加的名字:")
                # 增加
                for name in file_name:
                    os.rename(name, new_file + name)
            elif select == 2:
                del_file = input("输入要删除的名字:")
                length = len(del_file)
                for name in file_name:
                    os.rename(name,name[length:])
                # 删除
            elif select == 3:
                # 删除文件
                del_file_name = input("输入要删除的文件名:")
                os.remove(del_file_name)
                print("文件%s已删除" % del_file_name)
            elif select == 4:
                # 删除文件夹
                del_folder_name = input("输入要删除的文件夹:")
                os.rmdir(del_folder_name)
                print("文件夹%s已删除" % del_folder_name)
            elif select ==5:
                # 创建文件夹
                new_folder_name = input("输入你要创建的文件夹名称:")
                os.mkdir(new_folder_name)
                print("文件夹%s已成功创建" % new_folder_name)
            elif select == 6:
                break
            else:
                print("输入有误")

file_data()
