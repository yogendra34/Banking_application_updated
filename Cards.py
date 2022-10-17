import random
from Connection import sqlexecution
x=sqlexecution()
cur = x.cur
def Cards(username):
    print("---------Please enter the following information for Credit/Debit card allotment----------")
    type_of_card=input("Enter the type of  Card : ")
    temp=type_of_card in ('credit','Credit','Debit','debit')
    while temp==False:
        print("........Invalid type of Cards.....")
        type_of_card=input("Enter the type of Card : ")
        temp=type_of_card in ('credit','Credit','Debit','debit')
    print(".......Thank you for confirming the type of card.....")
    Card_number=random.randint(111111111111,999999999999)
    CVV_no=random.randint(111,999)
    mpin=random.randint(1111,9999)
    balance=input("Enter the balance in card you want to put: ")
    cmd1= "insert into Cards(Name,type_of_card,Card_number,CVV_no,mpin,balance) values(%s,%s,%s,%s,%s,%s)"
    var1=(username,type_of_card,Card_number,CVV_no,mpin,balance)
    x.execute(cmd1,var1)
    cmd2 = "select * from Cards where Name=%s"
    var2 = (username,)
    x.execute(cmd2,var2)
    result=cur.fetchone()
    sav={1:'Name', 2:'type_of_card', 3:'Card_number', 4:'CVV_no', 5:'balance', 6:'mpin'}
    acc = list(sav.values())
    print('-'*54)
    for i in zip(acc,result[0:]):
        print('|  {:^16}  |      {:<20}     |'.format(i[0],i[1]))
        print('-'*54)
    

     





