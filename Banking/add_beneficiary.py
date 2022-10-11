import random
from urllib.parse import uses_netloc
from Connection import sqlexecution
x=sqlexecution()
cur = x.cur
def add_beneficiary():
   username=input("Enter the username: ")
   Name=input("Enter the name of beneficiary: ")
   account_no=input("Enter the account_no of beneficiary: ") 
   temp=account_no.isnumeric() and len(str(account_no))==10
   while temp == False:
            print("invalid account_no, please enter again....")
            account_no=input("Enter the account_no of beneficiary: ")
            temp=account_no.isnumeric() and len(str(account_no))==10
            print("Valid Account_no")
   cmd1='insert into Beneficiary values(%s,%s,%s)'
   var1=(Name,account_no,username)
   x.execute(cmd1,var1)