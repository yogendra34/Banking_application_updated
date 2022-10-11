
import mysql.connector
connection = mysql.connector.connect(host='localhost', database='bank', user='root', password='Yogendra@3156')


class sqlexecution:
    con = connection
    cur=con.cursor(buffered=True)
    def execute(self,cmd,var):
        self.cmd = cmd
        self.var = var
        self.cur.execute(self.cmd,self.var)
        self.con.commit()



