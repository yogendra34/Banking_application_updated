def temp1():

    while True:

        print("----------Welcome to world bank-----------")
        print(".........If new to the bank, please register here........")
        print("1. Registration")
        print("2. Login")
        inp=int(input("Enter the no you want to proceed...... : "))

        if inp==1:
            from Registration import Registration
            Registration()
        elif inp==2:
            from Login import login
            login()
            break
        else:
            print("Invalid choice.....")
    
temp1()
        



        
         
           
    