import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import DAO.database as db
from DTO.taikhoanDTO import taikhoan



class taikhoanDAO:
    def __init__(self):
        self.conn = db.connect_to_database()


    def find_All(self):
        taikhoan_list=[]
        conn = self.conn
        try:
            conn.connect()
            query = "Select * from TaiKhoan"
            list = db.execute_fetch_all(conn, query)
            for item in list:
                account = taikhoan(item[0], item[1], item[2], item[3], item[4])
                taikhoan_list.append(account)
            return taikhoan_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
    
    
    def insert(self, taikhoan : taikhoan):
        conn = self.conn
        try:
            conn.connect()
            query=f"insert into taikhoan(username, password, trangthai, maloai) values ('{taikhoan.username}','{taikhoan.password}','{taikhoan.trangthai}','{taikhoan.maloai}')"
            db.execute_query(conn,query)
            return 'Thêm thành công !!!!'
        except mysql.connector.Error as error:
            return 'Thêm thất bại !!!!'
        finally:
            conn.close()

    def delete(self, id):
        conn = self.conn
        try:
            conn.connect()
            query=f"delete from taikhoan where matk = '{id}'"
            db.execute_query(conn,query)
            return 'Xoá thành công !!!!'
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            conn.close()

    def update(self, taikhoan : taikhoan):
        conn = self.conn
        try:
            conn.connect()
            query=f"update taikhoan set username = '{taikhoan.username}', password = '{taikhoan.password}', trangthai = '{taikhoan.trangthai}', maloai = '{taikhoan.maloai}' where matk = '{taikhoan.matk}'"
            db.execute_query(conn,query)
            return 'Cập nhật thành công !!!!'
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            conn.close()
        
    def checkPassword(self,username,password):
        try:
            self.conn.connect()
            query = f"Select * from TaiKhoan where username = '{username}' and password = '{password}'"
            result = db.execute_fetch_all(self.conn,query)
            if not result:
                return None
            for tk in result:
                account = taikhoan(tk[0],tk[1],tk[2],tk[3],tk[4])
            return account.maloai
        except mysql.connector.Error as error:
            return error
        finally:
            self.conn.close()

    def findById(self,id):
        account_list = []
        try:
            self.conn.connect()
            query = f"select * from taikhoan where matk = '{id}'"
            list = db.execute_fetch_all(self.conn,query)
            if list is not None:
                for account in list:
                    result = taikhoan(account[0],account[1],account[2],account[3],account[4])
                    account_list.append(result)
            return account_list
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
     
        
    def findByName(self,name):
        account_list = []
        try:
            self.conn.connect()
            query = f"select * from taikhoan where username like '%{name}%'"
            list = db.execute_fetch_all(self.conn,query)
            if list is not None:
                for account in list:
                    result = taikhoan(account[0],account[1],account[2],account[3],account[4])
                    account_list.append(result)
            return account_list
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        

    def findByStatus(self,status):
        account_list = []
        try:
            self.conn.connect()
            query = f"select * from taikhoan where trangthai = '{status}'"
            list = db.execute_fetch_all(self.conn,query)
            if list is not None:
                for account in list:
                    result = taikhoan(account[0],account[1],account[2],account[3],account[4])
                    account_list.append(result)
            return account_list
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
    
    def findByAccTypeID(self,accType):
        account_list = []
        try:
            self.conn.connect()
            query = f"select * from taikhoan where maloai = '{accType}'"
            list = db.execute_fetch_all(self.conn,query)
            if list is not None:
                for account in list:
                    result = taikhoan(account[0],account[1],account[2],account[3],account[4])
                    account_list.append(result)
            return account_list
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        
    def findByAccTypeName(self,name):
        account_list = []
        try:
            self.conn.connect()
            query = f"select tk.* from taikhoan as tk inner join loaitaikhoan as ltk where tk.maloai = ltk.maloai and ltk.tenloai like '%{name}%';"
            list = db.execute_fetch_all(self.conn,query)
            if list is not None:
                for account in list:
                    result = taikhoan(account[0],account[1],account[2],account[3],account[4])
                    account_list.append(result)
            return account_list
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'

if __name__ == "__main__":
    example = 'admin'
    passw = 'admin'
    tkDAO = taikhoanDAO()
    aa = tkDAO.checkPassword(example,passw)
    print(aa)
    
        
    