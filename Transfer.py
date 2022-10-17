from unittest import result
from Connection import sqlexecution
x=sqlexecution()
cur = x.cur
#Credited the amount2
def Trans(username):
    account_no=input("Enter the account no for which you want to transfer the money: ")
    temp= account_no.isnumeric() and len(str( account_no))==10
    while temp == False:
            print("invalid account_no, please enter again....")
            account_no=input("Enter the account_no : ")
            temp= account_no.isnumeric() and len(str( account_no))==10
    print(".....Thank you for conforming the account_no....")
    amount=input("Enter the amount you want to transfer: ")
    cmd2='select amount from Registration where Name=%s'
    var2=(username,)
    x.execute(cmd2,var2)

    result=cur.fetchone()[0]
    amount=input("Enter the amount you want to transfer: ")
    temp=int(result)<int(amount)
    while temp==True:
        print("......Insufficient balancd ....try again")
        amount=input("Enter the amount you want to transfer: ")
        temp=int(result)<int(amount)
    print(".....Thank you for conforming the balance....")
    # while True:
    #     if result<amount:
    #         print("Insufficient balance...try again.....")
    #         amount=input("Enter the amount you want to transfer: ")
            
    #     else:
    #          print(".....Thank you for conforming the balance....")
    cmd='update Registration set amount=amount + %s where account_no=%s'
    var=(amount,account_no)
    x.execute(cmd,var)
    cmd1='update Registration set amount=amount - %s where Name=%s'
    var1=(amount,username)
    x.execute(cmd1,var1)
    print("...Amount is transfered successfully...")
    sav={1:'Name',2: 'address',3:'Aadhar',4:'mobile_no',5:'amount',6:'confirm_password',7:'account_no' }
    
    cmd3='select * from Registration where account_no=%s'
    var3=(account_no,)
    x.execute(cmd3,var3)
    result2=cur.fetchone()
    acc = list(sav.values())
    print('-'*54)
    for i in zip(acc,result2[0:]):
        print('|  {:^16}  |      {:<20}     |'.format(i[0],i[1]))
        print('-'*54)
    




     