import random
from urllib.parse import uses_netloc
from Connection import sqlexecution
x=sqlexecution()
cur = x.cur
def add_beneficiary(username):
    '''
    This function is used to ....
    :params: username: what is it?
    '''
    Name=input("Please enter the name of beneficiary: ")
    temp= Name.isalpha()
    while temp==False:
        print("..The entered name is not valid, please try again....")
        Name=str(input("Please enter the name of beneficiary : "))
        temp= Name.isalpha()
    cmd='select Name from Registration'
    var=()
    x.execute(cmd,var)
    result=cur.fetchall()
    l=[]
    for i in result:
        l.append(i[0])
    temp =  Name in l
    while temp==False:    
      print("This Name has not been registered.......")
      Name=str(input("Please enter the name of beneficiary:  "))
      temp =  Name in l
    print("Thank you for confirming the user name....")
    cmd1='insert into Beneficiary(Name, beneficiary_to) values(%s,%s)'
    var1=(Name,username)
    x.execute(cmd1,var1)
    cmd2='update Beneficiary set account_no=(select account_no from Registration where Name=%s) where Name=%s'
    var2=(Name,Name)
    x.execute(cmd2,var2)
