from Dbcoonector.Connector import A
#from Connector import A
from math import factorial
import pandas as pd
import csv
import numpy as np


# mydb=a.coonection()
def db_data():
        a = A()
        mydb = a.coonection()
        mycursor = mydb.cursor()
        mycursor.execute("select * from employee")
        users = mycursor.fetchall()
      #  print(type(users))
        df1 = pd.DataFrame(users, columns=['id', 'name', 'salary', 'designation'])
       # print("Data frame data\n", df)
       # print("**************************************************************")
        mycursor.execute("select * from employees")
        users1 = mycursor.fetchall()
       # print(type(users1))
       # print(users1)
        df2 = pd.DataFrame(users1, columns=['ide', 'nameee', 'salaryee', 'designatione'])
       # print("Users1", df1)
       # df['pricematch']=np.where(df['salary']==df1['salaryee'],'True','False')
        df3=df1.append(df2)
        df4=df3.append(df1)
        #print(df3)

       # print("Final db",df)
        return df4


db_data()


# df = pd.DataFrame(users, columns=['id', 'name', 'salary', 'designation'])
        #print("Data frame data\n", df)









"""
        # df = pd.DataFrame(user, columns=['id', 'salary', 'salary', 'designation'])
        df.to_csv("C:\\Users\\922619\\OneDrive - Cognizant\\Documents\\Pandacsv.csv", index=False)
        output = np.asarray(users)
        #  print("New  Array \n",output,type(output))
        mycursor.execute("select * from employees")
        user = mycursor.fetchall()
        ucemp = mycursor.execute("select * from employee where employee.id not in (select id from employees)")
        ucemp = mycursor.fetchall()
        ucemps = mycursor.execute("select * from employees where employees.id not in (select id from employee)")
        ucemps = mycursor.fetchall()
#   print("Employee Table Values \n", users, "\n")
#  print("Employees Table Values \n", user, "\n")
# print("Uncoomon Employee Table Values \n", ucemp, "\n")
# print("Uncoomon Employees Table Values \n", ucemps, "\n")
# print("Uncoomon Employees Table Values \n", ucemps + ucemp, "\n")

       """














