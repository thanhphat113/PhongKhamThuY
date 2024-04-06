import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import DAO.database as db
from DTO.petDTO import pet
import mysql.connector

class petDAO:
    def __init__(self):
        self.conn = db.connect_to_database()
    
    def ReadFromDatabase(self):
        thunuoi_list = []
        conn = self.conn
        try:
            conn.connect()
            query = "Select * from ThuNuoi"
            list = db.execute_fetch_all(conn, query)
            for tn in list:
                subPet = pet(tn[0], tn[1], tn[2], tn[3], tn[4])
                thunuoi_list.append(subPet)
            return thunuoi_list
        except mysql.connector.Error as error:
            print(f'Error: {error}')
            return None
        finally:
            conn.close()
        

    def insert(self, pet : pet):
        conn = self.conn
        try:
            conn.connect()
            query=f"insert into thunuoi(tentn, mau, cannang) values ('{pet.get_tentn()}','{pet.get_maulong()}','{pet.get_cannang()}')"
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
            query=f"delete from thunuoi where matn = '{id}'"
            db.execute_query(conn,query)
            return 'Xoá thành công !!!!'
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            conn.close()

    def update(self, pet : pet):
        conn = self.conn
        try:
            conn.connect()
            query=f"update thunuoi set tentn = '{pet.get_tentn()}', mau = '{pet.get_maulong()}', cannang = '{pet.get_cannang()}' where matn = '{pet.get_matn()}'"
            db.execute_query(conn,query)
            return 'Cập nhật thành công !!!!'
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            conn.close()


    def findById(self, id):
        result = None
        conn = self.conn
        try:
            conn.connect()
            query = f"select * from thunuoi where matn = '{id}'"
            list = db.execute_fetch_all(conn, query)
            for subPet in list:
                result = pet(subPet[0], subPet[1], subPet[2], subPet[3], subPet[4])
            return result
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            conn.close()
        
#if __name__ == "__main__":
#    pets = petDAO()
#    result = pets.findById(1)
#    print(f"{result.get_tentn()}")

