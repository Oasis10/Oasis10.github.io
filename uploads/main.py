# coding:utf-8

from MySQL_3kingdoms import ThreeKingDoms


# 创建user对象
def main():
    user = ThreeKingDoms("localhost", 3306, "root", "mysql", "db_sanguo")
    while True:
        op_num = raw_input("请输入想要执行的操作：1.添加  2.删除  "
                               "3.修改  4.查询  5.显示所有英雄  6.退出")
        # 增
        if op_num == "1":
            name = raw_input("请输入英雄的姓名")
            age = raw_input("请输入英雄的年龄")
            gender = raw_input("请输入英雄的性别")
            state = raw_input("请输入英雄的国家")
            # 判断是否添加成功
            if user.insert(name, age, gender, state):
                print "[SUCCEED] 添加成功！"
            else:
                print "[FAILED] 添加失败！"
        # 删
        elif op_num == "2":
            h_id = raw_input("请输入想要删除的英雄编号：")
            if user.delete(h_id):
                print "[SUCCEED] 删除成功！"
            else:
                print "[FAILED] 删除失败！"
        # 改
        elif op_num == "3":
            h_id = raw_input("请输入想要修改的英雄编号：")
            while True:
                update_num = raw_input("请输入想要修改的信息：1.姓名 2.年龄 3.性别 4.国家")
                if update_num == "1":
                    option = "name"
                    name1 = raw_input("请输入姓名：")
                    if user.update(h_id, option, name=name1):
                        print "[SUCCEED] 修改成功！"
                    else:
                        print "[FAILED] 修改失败！"
                    break
                elif update_num == "2":
                    option = "age"
                    age1 = raw_input("请输入年龄：")
                    if user.update(h_id, option, age=age1):
                        print "[SUCCEED] 修改成功！"
                    else:
                        print "[FAILED] 修改失败！"
                    break
                elif update_num == "3":
                    option = "gender"
                    gender1 = raw_input("请输入性别：")
                    if user.update(h_id, option, gender=gender1):
                        print "[SUCCEED] 修改成功！"
                    else:
                        print "[FAILED] 修改失败！"
                    break
                elif update_num == "4":
                    option = "state"
                    state1 = raw_input("请输入姓名：")
                    if user.update(h_id, option, state=state1):
                        print "[SUCCEED] 修改成功！"
                    else:
                        print "[FAILED] 修改失败！"
                    break
                else:
                    print "输入错误，请重新选择！"
        # 查
        elif op_num == "4":
            h_id = raw_input("请选择想要查看的英雄编号"
                   "(输入0或不输入任何信息 查询全部英雄信息)：")
            result = user.select(h_id)
            if result:
                for item in result:
                    print item[0], item[1], item[2], item[3]
            else:
                print "[FAILED] 查询失败！"
        elif op_num == "5":
            for item in user.select(0):
                print item[0], item[1], item[2], item[3]
        elif op_num == "6":
            break
        else:
            print "输入有误，请重新输入！"

if __name__ == "__main__":
    main()


