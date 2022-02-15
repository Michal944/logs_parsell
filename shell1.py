import os
import mysql.connector

class Logs:
    def __init__(self,path_file):
        self.file  = open(path_file, 'rt')
        self.sline = ''
        self.llog  = []
        self.slog  = []
    def parsell(self):
        while True:
            self.sline = self.file.readline()
            if not self.sline:
                break
            self.slog.append(self.sline.split(' ', 5))
            self.llog.append(self.slog[0])
            self.slog.clear()
        self.file.close()
    def display(self, line='', date='', unit='', pid=''):
        if not line and not date and not unit and not pid:
            for log in self.llog:
                print(f"{log[0]} {log[1]} {log[2]} {log[3]} {log[4]} {log[5]}")
    

class Databes:
    def __init__(self, host, user, passwd):
        self.host   = host
        self.user   = user
        self.passwd = passwd
        self.cmd = 0
    def connect(self, name_db=''):
        if not name_db:
            self.mydb = mysql.connector.connect(
            host     = self.host,
            user     = self.user,
            password = self.passwd )
        else:
            self.mydb = mysql.connector.connect(
            host     = self.host,
            user     = self.user,
            password = self.passwd,
            database = name_db )
      #  print(mydb) 
        self.cmd = self.mydb.cursor()

    def create_db(self, name_db):
        self.status = 'Not added. Wrong database name'
        self.sql    = f'CREATE DATABASE {name_db}'
        self.cmd.execute(self.sql)
        self.cmd.execute("SHOW DATABASES")
        
        #Check name_db has been added
        for db in self.cmd:
            if name_db == db:
                self.status = 'Added correct'
        return self.status

    def create_tb(self, name_tb, name_db, columns):
        self.connect(name_db)
        self.cmd.execute(f"CREATE TABLE {name_tb}({columns})")

    def insert_row(self, name_db, name_tb, column_nm, column_val):
        self.connect(name_db)
        self.cmd.execute(f"INSERT INTO {name_tb} ({column_nm}) VALUES ({column_val})")
        self.mydb.commit() 






        

            