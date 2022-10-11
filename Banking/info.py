from Connection import sqlexecution
x=sqlexecution()
cur = x.cur
def info(username):
    sav={1:'Name',2: 'address',3:'Aadhar',4:'mobile_no',5:'amount',6:'confirm_password',7:'account_no' }
    
    cmd='select * from Registration where Name=%s'
    var=(username,)
    x.execute(cmd,var)
    result=cur.fetchone()
    acc = list(sav.values())
    print('-'*54)
    for i in zip(acc,result[0:]):
        print('|  {:^16}  |      {:<20}     |'.format(i[0],i[1]))
        print('-'*54)
    
        
    

