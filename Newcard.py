from Connection import sqlexecution
x=sqlexecution()
cur = x.cur

def new_card_and_delete_previous_card_details():
    Name=input("Enter the name whom do you want to assign a new card : ")
    type_of_card=input("Enter the type of card : ")
    Name_of_card=input("Enter the name of card : ")
    Card_number=input("Enter the card_number : ")
    CVV_no=input("Enter the CVV_no : ")
    balance=input("Enter the balance in card : ")
    cmd="delete from Cards where Name=%s"
    var=(Name,)
    x.execute(cmd,var)
    cmd1='insert into Cards values(%s,%s,%s,%s,%s,%s)'
    var1=(Name,type_of_card,Name_of_card,Card_number,CVV_no,balance)
    x.execute(cmd1,var1)
    cmd2='select * from Cards where Name=%s'
    var2=(Name,)
    x.execute(cmd2,var2)
    result=cur.fetchall()
    for i in result:
        for j in i:
            print(j)
    print("New card has been alloted and previous card information got deleted")

def new_card_and_keep_previous_card_details():
    Name=input("Enter the name whom do you want to assign a new card : ")
    type_of_card=input("Enter the type of card : ")
    Name_of_card=input("Enter the name of card : ")
    Card_number=input("Enter the card_number : ")
    CVV_no=input("Enter the CVV_no : ")
    balance=input("Enter the balance in card : ")
    cmd1='insert into Cards values(%s,%s,%s,%s,%s,%s)'
    var1=(Name,type_of_card,Name_of_card,Card_number,CVV_no,balance)
    x.execute(cmd1,var1)
    cmd2='select * from Cards where Name=%s'
    var2=(Name,)
    x.execute(cmd2,var2)
    result=cur.fetchall()
    for i in result:
        for j in i:
            print(j)
    print("New card has been alloted and previous card inforamation retained")

def main1():
    inp = int(input("1.Register for a new card and delete previous card info 2. Register for a new card and keep previous card info "))

    if inp == 1:
       new_card_and_delete_previous_card_details()
    else:
        new_card_and_keep_previous_card_details()

main1()

 
