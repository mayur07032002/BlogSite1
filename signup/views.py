from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
import smtplib
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase",
  port = 3366
)

sender = "blogsiteforum@gmail.com"
password = "Blogsite@2021"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender,password)

mycursor = mydb.cursor()
data = []

def index(request):
    return render(request,'signup/index.html')

def sign(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    user = request.POST.get('user')
    password = request.POST.get('password')   
    global data 
    data = [fname, lname, email, user, password]

    if(verify(email, user)):
      reciever = email

      send_code = random.randint(100000,999999)
      data.append(send_code)
      code_generated = send_code
      
      subject = "Email Verification Process."
      body = "Hello!! " + fname + " " + lname + "\nThis is Email verification process for sign up.\nPlease enter OTP given below on site\n OTP : " + str(send_code)
      
      message = "Subject:{}\n\n{}".format(subject, body)

      server.sendmail(sender, reciever, message)

      return render(request,'signup/verify.html')
    return HttpResponse("Email already exists!!")


def verify(email, user):
    query = "SELECT * FROM signup"
    mycursor.execute(query)
    results = mycursor.fetchall()

    for result in results:
      if result[3]==email or result[4]==user:
        return False
    return True


def verify_email(request):
    code = request.POST.get('code')
   
    if code == str(data[5]):
        query = "INSERT INTO signup (first_name, last_name, email_id, user_name, password) VALUES (%s, %s, %s, %s, %s)"
        values = (data[0], data[1], data[2], data[3], data[4])

        mycursor.execute(query, values)
        mydb.commit()
        return HttpResponse('Successfully Signed Up!! <a href="/login">Login</a> ')
    else:
      return HttpResponse("Invalid Code.")