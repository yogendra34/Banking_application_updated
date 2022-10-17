import random
from urllib.parse import uses_netloc
from Connection import sqlexecution
x=sqlexecution()
cur = x.cur
def beneficiary(username):
   cmd2='select * from Beneficiary where beneficiary_to=%s'
   var2=(username,)
   x.execute(cmd2,var2)
   result=cur.fetchall()
   print("-------Your beneficiaries--------")
   print(result)







    