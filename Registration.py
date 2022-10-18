import random
from Connection import sqlexecution
x=sqlexecution()
def Registration():
    username=input("Enter the user name : ")
    temp=username.isalpha()
    while temp==False:
        print("username is not valid, please try again....")
        username=str(input("Enter the user name : "))
        temp=username.isalpha()
    address=input("enter the address : ")
    Aadhar=input("enter the Aadhar no : ")
    Aadhar=Aadhar.replace(' ','')

    temp=Aadhar.isnumeric() and len(str(Aadhar))==12
    while temp == False:
        print("invalid aadhar no, please enter again....")
        Aadhar=input("Enter the Aadhar no : ")
        temp=Aadhar.isnumeric() and len(str(Aadhar))==12
    print("........Valid Aadhar no.......")
    mobile_no=input("enter the mobile no : ")
    mobile_no=mobile_no.replace(' ','')
    temp=mobile_no.isnumeric() and len(str(mobile_no))==10 and mobile_no[0]==['6','7','8','9']
    while temp == False:
        print("invalid mobile no, please enter again....")
        mobile_no=input("Enter the mobile no : ")
        temp=mobile_no.isnumeric() and len(str(mobile_no))==10
    print("......Valid mobile no.......")
    while True:
        amount=input("Enter the initial amount you want to put in the bank : ")
        amount=amount.replace(' ','')
        if int(amount)>0 and amount.isnumeric():
                print("Thank you for confirming the amount..")
                break
        else:
                print("..invalid amount..")
    special_character=['@','#','$','&']
    while True:
        try:
                password=input("Please enter a password : ")
                password=password.replace(' ','')
                if len(password)<8:
                        raise ValueError("entered password should contain at least 8 character")
                if not any(char.isdigit()for char in password):
                        raise ValueError("there should be at least one digit")
                if not any(char.upper()for char in password):
                         raise KeyError ()
                if not any(char.islower() for char in password):
                        raise KeyError
                if not any(char in special_character for char in password ):
                        raise KeyError
                break
        except ValueError:
                print("There should be one uppercase, one lowercase, one special character, one integer and should have at least 8 character in the entered password...")
        except KeyError:
                print("There should be one uppercase, one lowercase, one special character, one integer and should have at least 8 character in the entered password...")

                
    confirm_password=input("please confirm the entered password : ")
    temp=confirm_password!=password
    while temp==True:
            print("Your password is not matching, please try again........")
            confirm_password=input("please confirm the entered password : ")
            temp=confirm_password!=password
    print("Thank you for confirming the password........")
    print("Assign the account_no: ")
    z=random.randint(345,876)*7678767
    print(z)
    cmd="insert into Registration(Name, address, Aadhar, mobile_no, amount,confirm_password,account_no)values(%s,%s,%s,%s,%s,%s,%s)"
    var=(username, address, Aadhar, mobile_no, amount,confirm_password,z)
    x.execute(cmd,var)



