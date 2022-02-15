import shell1 as a


class Build:
    def __init__(self, pathl, host, user, passwd):
        self.log_path = pathl
        self.logs = a.Logs(self.log_path)
        self.db   = a.Databes(host, user, passwd)
    
    def start(self, name_db=''):
        self.logs.parsell()
        self.db.connect(name_db)
        self.sql ='log_id INT NOT NULL AUTO_INCREMENT, date VARCHAR(20), unit VARCHAR(30) NOT NULL, pid VARCHAR(20) NOT NULL, log_desc TEXT, PRIMARY KEY ( log_id )'
        self.name_col = "date, unit, pid, log_desc"
        self.val_col  = ''
        if not name_db:
            self.db.create_db('databaselog')
            self.db.create_tb('table0222','databaselog', self.sql)
            for log in self.logs.llog:
                self.val_col = f" '{log[0]}{log[1]}{log[2]}', '{log[3]}', '{log[4]}', '{log[5]}'"
                self.db.insert_row('databaselog', 'table0222', self.name_col, self.val_col)



parsellv1 = Build('shell_script/messages','192.168.1.68', 'loguser', 'bm310594')
parsellv1.start()
