import random
from urllib.parse import uses_netloc
from Connection import sqlexecution
x=sqlexecution()
cur = x.cur
def beneficiary():
#    Name=input("Enter the name of beneficiary: ")
#    account_no=input("Enter the account_no of beneficiary: ") 
#    cmd1='insert into Beneficiary values(%s,%s)'
#    var1=(Name,account_no)
#    x.execute(cmd1,var1)
   username=input("Enter the username: ")
   cmd2='select * from Beneficiary where beneficiary_to=%s'
   var2=(username,)
   x.execute(cmd2,var2)
   result=cur.fetchall()
   print("-------Your beneficiaries--------")
   print(result)







    