# Banking application Project
This is the Banking application project. It is the first python project which I have developed with the guidance of my mentor. I also updated this code and by the help of our mentor I debug each file of the code.
# Requirements
1.Visual Studio Code

2.MySql (above version 8.0)
# Modules used
1 mysql.connector
2.random
# Mysql Code
1. Database
I created a database 'bank', where I stored all the tables that will be useful for my project.
# Tables
# 1.Registration:- 
        This table contains the information of a new user.
        columns
        (Name, address, Aadhar, mobile_no, amount, confirm_password, account_no)
# 2.Cards:- 
        This table contains the information of a card that a particular person hold.
        columns
        (Name , type_of_card , Card_number, CVV_no ,balance, mpin)
# 3.Beneficiaries:- 
        This table contains the information about the person's beneficiaries 
        columns
        (Name, account_no, beneficiary_to)
# 4.add_beneficiary:-
        This table used for adding the beneficiary for a user.
        columns
        (Name, account_no)
# Python Code
# Connection.py
This file used for connecting Mysql and python
# Mainfile.py
This is the python file which connects through all the files.
# Registration.py
This file used for registering a new user in a bank and entered their information.
# Login.py
This file used for already registered user to login their profile and see the different features of the bank.
# info.py
This file used for the showing details of the registered user in the bank.
# Beneficiary
This file used for displaying all the beneficiaries of a user.
# add_beneficiary
This file is used for adding new beneficiary for a user.
# Cards
This file is used for alloting the different cards to a user.
# renewcard
This file is used for either keeeping previous card information and add new card or deleting previous information of card and alloting a new card.
# Transfer
This file is used for the transactionn that a user can proceed.




