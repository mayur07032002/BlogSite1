from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
import datetime
def index(request):
    return render(request,'index.html',{'name':None})

    

def login(request):
    return render(request,'login.html')

def signin(request):
    return render(request,'sign_index.html')


def entry_database(user, password):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mydatabase"
    )
    mycursor = mydb.cursor()
    query = "INSERT INTO login_data(username, password, time_stamp) VALUES (%s, %s, %s)"
    mycursor.execute(query, [user, password, datetime.datetime.now()])
    mydb.commit()
    return 

def log(request):
    user = request.POST.get('user')
    password = request.POST.get('password')
    if user==None and password==None:
        return render(request,'index.html',{'name':None})

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="mydatabase"
    )
    mycursor = mydb.cursor()
    query = "SELECT * FROM signup"
    
    mycursor.execute(query)
    results = mycursor.fetchall()

    flag = False
    for i in results:
      if i[4]==user:
        if i[5]==password:
          flag = True
          entry_database(i[4], i[5])
          return render(request, 'index.html',{'name':user,'flag':flag})
        else:
          return HttpResponse("Invalid Password.")

    if flag==False:
      return HttpResponse("Invalid Username.")
