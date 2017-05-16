# coding:utf-8

import MySQLdb


class ThreeKingDoms():
    """创建三国数据库类"""

    def __init__(self, host, port, user, passwd, db, charset="utf8"):
        """初始化"""
        self.__host = host
        self.__port = port
        self.__user = user
        self.__passwd = passwd
        self.__db = db
        self.__charset = charset

    def __open(self):
        """建立python和MySQL的连接"""
        self.__conn = MySQLdb.connect(
            host = self.__host,
            port = self.__port,
            user = self.__user,
            passwd = self.__passwd,
            db = self.__db,
            charset = self.__charset
        )
        self.__cursor = self.__conn.cursor()

    def __close(self):
        """关闭连接"""
        self.__cursor.close()
        self.__conn.close()

    def insert(self, name, age, gender, state):
        """增加数据"""
        self.__open()
        # 构造sql语句
        try:
            sql = "INSERT INTO t_hero(name, age, gender, state)  \
                   VALUES (%s, %s, %s, %s)"
            # 执行sql语句
            result = self.__cursor.execute(sql, [name, age, gender, state])
            # 判断是否执行成功
            if result == 1:
                self.__conn.commit()
                return True
            else:
                return False
        except Exception, e:
            print "添加失败，错误代码为：", e
            return False
        finally:
            self.__close()

    def delete(self, h_id):
        """删除某条数据"""
        self.__open()
        try:
            # 构造sql语句
            sql = "DELETE FROM t_hero WHERE id = %s"
            # 执行sql语句
            result = self.__cursor.execute(sql, [h_id])
            # 判断是否执行成功
            if result == 1:
                self.__conn.commit()
                return True
            else:
                return False
        except Exception, e:
            print "删除出错！错误代码为：", e
            return False
        finally:
            self.__close()

    def update(self, h_id, option, name=0, age=0, gender=0, state=0):
        """修改某条数据"""
        self.__open()
        try:
            # 构造sql语句
            sql = "UPDATE t_hero SET " + option + " = %s WHERE id = %s"
            print sql
            # 执行sql语句
            # 修改姓名
            if option == "name":
                result = self.__cursor.execute(sql, [name, h_id])
            # 修改年龄
            elif option == "age":
                result = self.__cursor.execute(sql, [age, h_id])
            # 修改性别
            elif option == "gender":
                result = self.__cursor.execute(sql, [gender, h_id])
            # 修改国家
            else:
                result = self.__cursor.execute(sql, [state, h_id])
            if result == 1:
                self.__conn.commit()
                return True
            else:
                return False
        except Exception, e:
            print "修改出错，错误代码为：", e
            return False
        finally:
            self.__close()

    def select(self, h_id = 0):
        """查询"""
        self.__open()
        try:
            # 判断查询的内容
            if h_id:
                sql = "SELECT * FROM t_hero WHERE id = %s"
                self.__cursor.execute(sql, [h_id])
                result = self.__cursor.fetchall()
            else:
                sql = "SELECT * FROM t_hero"
                self.__cursor.execute(sql)
                result = self.__cursor.fetchall()
            # 判断是否查询到
            if len(result) > 0:
                return result
            else:
                return False
        except Exception, e:
            print e
            return False
        finally:
            self.__close()









