import mysql.connector

# db連線架構
# https://github.com/nestordeharo/mysql-python-class/blob/master/mysql_python.py

class Website(object):
    # db_info = ("localhost", "root", "root")
    def __init__(self, host = 'localhost', user = 'root', password = 'root'):
        self.__host = 'localhost'
        self.__user = 'root'
        self.__password = 'root' 

    def __open__(self):
        try:
            self.__connect = mysql.connector.connect(host = self.__host, user= self.__user, password= self.__password)
            self.__cursor = self.__connect.cursor()
        except mysql.connector.errors as e:
            # Todo 測試
            for error_msg in e:
                print("Error %s" % (e))

    def __close__(self):
        self.__connect.close()

    def queryMemberByUserName(self, username):
        sql = "select * from website.member where username = %s"

        self.__open__()
        self.__cursor.execute(sql, (username, ))
        
        result = self.__cursor.fetchone()
        self.__close__()
        if result and len(result) > 0:
            return dict(zip(self.__cursor.column_names, result))
        
        return None

    def insertNewMember(self, name, username, password):
        sql = "INSERT INTO WEBSITE.MEMBER (name, username, password)"
        sql += " values (%s, %s, %s)"

        self.__open__()
        self.__cursor.execute(sql, (name, username, password))
        self.__connect.commit()
        self.__close__()
        
    def queryAllMessage(self):
        sql = 'select b.name, b.username , a.* from website.message a'
        sql += ' left join website.member b'
        sql += ' on a.member_id = b.id'
        sql += ' order by time'

        self.__open__()
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        self.__close__()
        if result and len(result) > 0:
            return [dict(zip(self.__cursor.column_names, row)) for row in result]
        
        return None
    
    def insertNewMessage(self, member_id, message):
        
        if not member_id or not message:
            return None

        sql = "INSERT INTO WEBSITE.MESSAGE (MEMBER_ID, CONTENT)"
        sql += " values (%s, %s)"

        self.__open__()
        self.__cursor.execute(sql, (member_id, message))
        self.__connect.commit()
        self.__close__()

    def deleteMsesageById(self, message_id):
        sql = "DELETE FROM WEBSITE.MESSAGE"
        sql += " WHERE ID = %s"
        self.__open__()
        self.__cursor.execute(sql, (message_id, ))
        self.__connect.commit()
        self.__close__()

    def updateMemberUserName(self, orig_username, new_name):
        sql = "update WEBSITE.member"
        sql += " set name = %s"
        sql += " where username = %s"

        self.__open__()
        self.__cursor.execute(sql, (new_name, orig_username, ))
        self.__connect.commit()
        self.__close__()