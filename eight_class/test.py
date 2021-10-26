import mysql.connector as con


class MySQLdb:
    def connect_mysql(self, host="localhost", user='root', password='', database=''):

        try:
            if database != '':

                mydb = con.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=database
                )
            else:
                mydb = con.connect(
                    host=host,  
                    user=user,
                    password=password,
                )

            print(mydb)
            return mydb
        except Exception as e:
            print(e)

    def create_database(self, dbname):
        try:
            connection = self.connect_mysql()
            cursor = connection.cursor()
            sql = "CREATE DATABASE " + dbname
            cursor.execute(sql)
            cursor.close()
            connection.close()
        except Exception as e:
            print(e)

    def create_table(self, table_name):
        try:
            connection = self.connect_mysql(database='super_shop')
            cursor = connection.cursor()
            sql = "CREATE TABLE " + table_name + " (id INT AUTO_INCREMENT PRIMARY KEY, name varchar(255), post varchar(255))"
            cursor.execute(sql)
            cursor.close()
            connection.close()
        except Exception as e:
            print(e)

    def insert_data(self, table_name):
        try:
            connection = self.connect_mysql(database='super_shop')
            cursor = connection.cursor()
            sql = "INSERT INTO " + table_name + "(name, post) VALUES(%s, %s)"
            val = [
                ('Peter', 'Aria Manager'),
                ('Amy', 'General Manager'),
                ('Hannah', 'Team Head'),
                ('Michael', 'Accountent'),
                ('Sandy', 'Sales Man')]
            cursor.executemany(sql,val)
            connection.commit()
            cursor.close()
            connection.close()
        except Exception as e:
            print(e)

    def show_data(self, table_name):
        try:
            connection = self.connect_mysql(database='super_shop')
            cursor = connection.cursor()
            sql = "SELECT * FROM " + table_name
            cursor.execute(sql)
            resutl = cursor.fetchall()
            for i in resutl:
                print(i)
            cursor.close()
            connection.close()
        except Exception as e:
            print(e)


mysql_handl = MySQLdb()
mysql_handl.create_database('super_shop')
mysql_handl.create_table('employee')
mysql_handl.insert_data('employee')
mysql_handl.show_data('employee')
