import sqlite3
from sqlite3 import Error
from datetime import datetime

class CompostDB:
    database = "./compost_temp.db"
    connection = None
    def get_connection(self):
        if self.connection is None:
            try:
                self.connection = sqlite3.connect(self.database)
            except Error as e:
                print(e)
        return self.connection

    def insert_data(self, temperature, battery):
        connection = self.get_connection()
        sql = ''' INSERT INTO Compost(temperature, battery) VALUES(?,?) '''
        cur = connection.cursor()
        cur.execute(sql, (temperature, battery))
        connection.commit()
        return cur.lastrowid

    def select_all_temp_data(self):
        connection = self.get_connection()
        cur = connection.cursor()
        cur.execute("SELECT temperature, DATETIME(date_created, 'localtime') FROM Compost ORDER BY date_created")
        rows =  cur.fetchall()
        dates = []
        temps = []
        for row in rows:
            temps.append(row[0])
            dates.append(datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S"))
        return dates,temps

    def select_latest_temp_data(self):
        connection = self.get_connection()
        cur = connection.cursor()
        cur.execute("SELECT temperature, battery, DATETIME(date_created, 'localtime') FROM Compost ORDER BY date_created DESC LIMIT 1")
        row = cur.fetchone()
        return row[0], row[1], row[2]




def main():
    compostDB = CompostDB()
    compostDB.insert_data(88.55,4321)
    date, battery, temp = compostDB.select_latest_temp_data()
    print("date={} battery={} temp={}".format(date,battery,temp))


if __name__ == '__main__':
    main()