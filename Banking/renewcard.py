import random
from Connection import sqlexecution
x=sqlexecution()
cur = x.cur

def new_card_and_delete_previous_card_details(username):
    cmd="delete from Cards where Name=%s"
    var=(username,)
    x.execute(cmd,var)
    # print("---------Please enter the following information for Credit/Debit card allotment----------")
    # username=input("Enter the user name : ")
    type_of_card=input("Enter the type of  Card : ")
    temp=type_of_card in ('credit','Credit','Debit','debit')
    while temp==False:
        print("........Invalid type of Cards.....")
        type_of_card=input("Enter the type of Card : ")
        temp=type_of_card in ('credit','Credit','Debit','debit')
    print(".......Thank you for conforming the type of card.....")
    # print("......Choose the Bank from which you want the Credit Card......")
    # Name_of_card=input("Enter the name of card : ")
    Name_of_card = str(input("Choose the Bank from which you want the credit/Debit card? : 1.Yes bank 2. SBI 3. Axis bank 4.PNB 5.Bank of Baroda "))
    if Name_of_card=='Yes bank':
        print("Thank you for conforming the bank name....")
    elif Name_of_card=='SBI':
        print("Thank you for conforming the bank name....")
    elif Name_of_card=='Axis bank':
        print("Thank you for conforming the bank name....")   
    elif Name_of_card=='PNB':
        print("Thank you for conforming the bank name....")
    elif Name_of_card=='Bank of Baroda':
        print("Thank you for conforming the bank name....")
    else:
        print("Invalid bank name...")
    Card_number=random.randint(111111111111,999999999999)
    CVV_no=random.randint(111,999)
    mpin=random.randint(1111,9999)
    balance=input("Enter the balance in card you want to put: ")
    cmd1= "insert into Cards(Name,type_of_card,Name_of_card,Card_number,CVV_no,mpin,balance) values(%s,%s,%s,%s,%s,%s,%s)"
    var1=(username,type_of_card,Name_of_card,Card_number,CVV_no,mpin,balance)
    x.execute(cmd1,var1)
    cmd2 = "select * from Cards where Name=%s"
    var2 = (username,)
    x.execute(cmd2,var2)
    result=cur.fetchone()
    sav={1:'Name', 2:'type_of_card', 3:'Name_of_card', 4:'Card_number', 5:'CVV_no', 6:'balance', 7:'mpin'}
    
    cmd3='select * from Cards where Name=%s'
    var3=(username,)
    x.execute(cmd3,var3)
    result2=cur.fetchone()
    acc = list(sav.values())
    print('-'*54)
    for i in zip(acc,result2[0:]):
        print('|  {:^16}  |      {:<20}     |'.format(i[0],i[1]))
        print('-'*54)
    print("New Card has been alloted and previous information got deleted to this username")
     

def new_card_and_keep_previous_card_details(username):
    type_of_card=input("Enter the type of  Card : ")
    temp=type_of_card in ('credit','Credit','Debit','debit')
    while temp==False:
        print("........Invalid type of Cards.....")
        type_of_card=input("Enter the type of Card : ")
        temp=type_of_card in ('credit','Credit','Debit','debit')
    print(".......Thank you for conforming the type of card.....")
    # print("......Choose the Bank from which you want the Credit Card......")
    # Name_of_card=input("Enter the name of card : ")
    Name_of_card = str(input("Choose the Bank from which you want the credit/Debit card? : 1.Yes bank 2. SBI 3. Axis bank 4.PNB 5.Bank of Baroda "))
    if Name_of_card=='Yes bank':
        print("Thank you for conforming the bank name....")
    elif Name_of_card=='SBI':
        print("Thank you for conforming the bank name....")
    elif Name_of_card=='Axis bank':
        print("Thank you for conforming the bank name....")   
    elif Name_of_card=='PNB':
        print("Thank you for conforming the bank name....")
    elif Name_of_card=='Bank of Baroda':
        print("Thank you for conforming the bank name....")
    else:
        print("Invalid bank name...")
    Card_number=random.randint(111111111111,999999999999)
    CVV_no=random.randint(111,999)
    mpin=random.randint(1111,9999)
    balance=input("Enter the balance in card you want to put: ")
    cmd1= "insert into Cards(Name,type_of_card,Name_of_card,Card_number,CVV_no,mpin,balance) values(%s,%s,%s,%s,%s,%s,%s)"
    var1=(username,type_of_card,Name_of_card,Card_number,CVV_no,mpin,balance)
    x.execute(cmd1,var1)
    cmd2 = "select * from Cards where Name=%s"
    var2 = (username,)
    x.execute(cmd2,var2)
    result=cur.fetchone()
    sav={1:'Name', 2:'type_of_card', 3:'Name_of_card', 4:'Card_number', 5:'CVV_no', 6:'balance', 7:'mpin'}
    
    cmd3='select * from Cards where Name=%s'
    var3=(username,)
    x.execute(cmd3,var3)
    result2=cur.fetchone()
    acc = list(sav.values())
    print('-'*54)
    for i in zip(acc,result2[0:]):
        print('|  {:^16}  |      {:<20}     |'.format(i[0],i[1]))
        print('-'*54)
    print("New card has been alloted and previous information got retained...")
def main1(username):
    inp = int(input("1.Register for a new card and delete previous card info 2. Register for a new card and keep previous card info "))

    if inp == 1:
       new_card_and_delete_previous_card_details(username)
    else:
        new_card_and_keep_previous_card_details(username)


 
