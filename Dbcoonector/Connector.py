import  mysql.connector

class A:
  def coonection(self):
    mydb = mysql.connector.connect(host='localhost', user='root', password='17311A04dx@', database='sumanth')
    return mydb

