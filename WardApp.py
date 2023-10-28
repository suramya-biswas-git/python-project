import DatabaseConnect

# function to add new ward in Hospital. Ward number will be auto generated
def wardAddition():
    wardName=input("Enter ward name:")
    bedNumber=int(input("Enter the number of beds present in ward:"))
    available=bedNumber
    rate=float(input("Enter rate per day per bed:"))
    conn=DatabaseConnect.databaseConnector()
    mycursor = conn.cursor()
    mycursor.execute("SELECT count(*) FROM ward")
    myresult = mycursor.fetchone()
    x=int(myresult[0])
    wardId=0
    if x==0 :
        wardId=1001
    else:
        wardId=1000+x+1
    sql = "INSERT INTO ward  VALUES (%s, %s, %s, %s, %s)"
    val = (wardId,wardName,bedNumber,available,rate)
    mycursor.execute(sql, val)
    conn.commit()
    print("New Ward is added")
    conn.close()

 # function to allocate bed for new patient or release patient's bed of a  ward        

def wardUpdate(wardId,status):
    conn=DatabaseConnect.databaseConnector()
    mycursor = conn.cursor()
    sql1 = "SELECT available from ward where ward_id="+str(wardId)
    mycursor.execute(sql1)
    myresult = mycursor.fetchone()
    x=int(myresult[0])
    if status=="I":
        x=x-1
    else:
        x=x+1
        
    sql2="UPDATE ward set available="+str(x)+" where ward_id="+str(wardId)
    mycursor.execute(sql2)
    conn.commit()
    print("Ward bed availabilty is updated")
    conn.close()
    
#wardUpdate(1001,"I")
#wardUpdate(1002,"R")

# function to search a ward based on ward id
def wardFind(wardId):
    conn=DatabaseConnect.databaseConnector()
    mycursor = conn.cursor()
    sql = "SELECT ward_id from ward where ward_id="+str(wardId)
    flag=True
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    if myresult == None:
        flag=False
    conn.close()
    return flag
    
#wardFind(1002)

# function to search a bed rate per day based on ward id
def findBedRate(wardId):
    conn=DatabaseConnect.databaseConnector()
    mycursor = conn.cursor()
    sql = "SELECT rate from ward where ward_id="+str(wardId)
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    rate=float(myresult[0])
    conn.close()
    return rate

#findBedRate(1001)   

# function to show all wards
def wardReport():
    conn=DatabaseConnect.databaseConnector()
    mycursor = conn.cursor()
    sql = "SELECT * from ward"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for ward in myresult:
        print(str(ward[0])+" "+ward[1]+" "+str(ward[2])+" "+str(ward[3])+" "+str(ward[4]))
    conn.close()

#wardReport()
   






    
