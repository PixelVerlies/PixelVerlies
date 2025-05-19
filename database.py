import mariadb
import sys

class database():
    def __init__(self):
        conn = None
        cur = None

    def connection(self):
        try:
            self.conn = mariadb.connect(
                user="Geister_Eule",
                password="Jd787811?",
                host="localhost",
                port=3306,
                database="pixelverlies"
            )
        except mariadb.Error as e:
            print(f"Error {e}")
            sys.exit(1)

        self.cur = self.conn.cursor()

    def connClose(self):
        self.conn.close()



