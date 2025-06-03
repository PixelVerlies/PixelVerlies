import mariadb
import sys

class database():
    def __init__(self):
        conn = None
        cur = None

    def connection(self):
        try:
            self.conn = mariadb.connect(
                user="team09",
                password="NHHJS",
                host="10.80.0.206",
                port=3306,
                database="team09"
            )
        except mariadb.Error as e:
            print(f"Error {e}")
            sys.exit(1)

        self.cur = self.conn.cursor()

    def connClose(self):
        self.conn.close()
