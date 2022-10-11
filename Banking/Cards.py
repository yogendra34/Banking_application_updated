import random
from Connection import sqlexecution
x=sqlexecution()
cur = x.cur
def Cards(username):
    print("---------Please enter the following information for Credit/Debit card allotment----------")
    # username=input("Enter the user name : ")
    # temp=username.isalpha()
    # while temp==False:
    #     print("username is not valid, please try again....")
    #     username=str(input("Enter the user name : "))
    #     temp=username.isalpha()
    # cmd='select Name from Registration'
    # var=()
    # x.execute(cmd,var)
    # result=cur.fetchall()
    # l=[]
    # for i in result:
    #     l.append(i[0])
    # temp= username in l
    # while temp==False:
    #     print("This username has not been registered,Please register first.......")
    #     username=str(input("Enter the user name : "))
    #     temp= username in l
    # print(".......Thank you for conforming the username.........")
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
    acc = list(sav.values())
    print('-'*54)
    for i in zip(acc,result[0:]):
        print('|  {:^16}  |      {:<20}     |'.format(i[0],i[1]))
        print('-'*54)
    

     





