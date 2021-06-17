from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)
mycursor = mydb.cursor()
def index(request):
    return render(request,'signup/index.html')

def sign(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    user = request.POST.get('user')
    password = request.POST.get('password')

    # print(fname,lname,email,user,password,cpassword)
    # print(fname)

    query = "INSERT INTO signup (first_name, last_name, email_id, user_name, password) VALUES (%s, %s, %s, %s, %s)"
    values = (fname, lname, email, user, password)

    mycursor.execute(query, values)
    mydb.commit()

    return HttpResponse("Submitted!!")