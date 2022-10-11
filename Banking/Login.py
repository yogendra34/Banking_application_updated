
from Connection import sqlexecution
x=sqlexecution()
cur = x.cur

def login():
    print(".........Welcome to login.........")
    username=input("Enter username: ")
    temp=username.isalpha()
    while temp==False:
        print("username is not valid, please try again....")
        username=str(input("Enter the username : "))
        temp=username.isalpha()
    cmd='select Name from Registration'
    var=()
    x.execute(cmd,var)
    result=cur.fetchall()
    l=[]
    for i in result:
        l.append(i[0])
    temp = username in l
    while temp==False:    
      print("This username has not been registered.......")
      username=str(input("Enter the username : "))
      temp = username in l
    print("Thank you for conforming the user name....")
    confirm_password=input("Enter the password : ")
    cmd1='select Name,confirm_password from Registration'
    var1=()
    x.execute(cmd1,var1)
    result2=cur.fetchall()
    l={}
    for i,j in result2:
        l.setdefault(i,[]).append(j)
    temp=l[username][0]!=confirm_password
    
    while temp==True:
        print("entered password is incorrect,please try again.......")
        confirm_password=input("Enter the password : ")
        temp=l[username][0]!=confirm_password
    print("Thanks for logging in .......")
    print("1.The account details...")
    print("2. Transfer fund...")
    print("3. Cards...")
    print("4. Register the new card...")
    print("5. Beneficiary....")
    print("6. add_beneficiary....")
    print("Thank you .........")
    inp=int(input("Enter the no you want to proceed...... : "))
    if inp==1:
        from info import info
        info(username)
    elif inp==2:
        from Transfer import Trans
        Trans(username)
    elif inp==3:
        from Cards import Cards
        Cards(username)
    elif inp==4:
        from renewcard import main1
        main1(username)
    elif inp==5:
        from Beneficiary import beneficiary
        beneficiary()
    elif inp==6:
        from add_beneficiary import add_beneficiary
        add_beneficiary()
    else:
        print("Invalid choice.....")
    login()
login()
    
    

    
