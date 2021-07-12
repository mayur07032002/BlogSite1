from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector 
import random
import smtplib
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase",
  port = 3366
)
mycursor = mydb.cursor()


sender = "blogsiteforum@gmail.com"
password = "Blogsite@2021"
reciever = ""
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender,password)
code_generated = 0
login_time = 0

def index(request):
    return render(request,'login.html')

def login(request):
    user = request.POST.get('user')
    password = request.POST.get('password')
    print(user,password)

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
          return render(request, 'index.html',{'name':user})
        else:
          return HttpResponse("Invalid Password.")

    if flag==False:
      return HttpResponse("Invalid Username.")
    

def change(request):
    return render(request, 'login/change_user.html')

def send_code(request):
    email = request.POST.get('email')
    global reciever
    reciever = email

    send_code = random.randint(100000,999999)
    global code_generated
    code_generated = send_code
    
    subject = "Email Verification Process."
    body = "Hello!! " + email + "\nThis is Email verification process for sign up.\nPlease enter OTP given below on site\n OTP : " + str(send_code)
    
    message = "Subject:{}\n\n{}".format(subject, body)

    server.sendmail(sender, reciever, message)

    return render(request,'login/verify.html')

def verify(request):
    code_entered = request.POST.get('code')
    if code_entered == str(code_generated):
      return render(request, 'login/reset.html')
    else:
      return HttpResponse("Wrong code")

def reset(request):
    new_user = request.POST.get('user')
    new_password = request.POST.get('password')
    query = "UPDATE signup SET user_name=%s , password=%s WHERE email_id=%s"

    mycursor.execute(query, [new_user, new_password,reciever])

    mydb.commit()
    return render(request, 'login/index.html')
   

def logout(request):
  return render(request, 'index.html')

def entry_database(user, password):
  query = "INSERT INTO login_data(username, password, time_stamp) VALUES (%s, %s, %s)"
  mycursor.execute(query, [user, password, datetime.datetime.now()])
  mydb.commit()
  return 





