from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector 
import random
import smtplib

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)
mycursor = mydb.cursor()


sender = "blogsiteforum@gmail.com"
password = "Blogsite@2021"
reciever = ""
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender,password)
code_generated = 0
def index(request):
    return render(request,'login/index.html')

def login(request):
    user = request.POST.get('user')
    password = request.POST.get('password')
    print(user,password)

    query = "SELECT * FROM signup"
    
    mycursor.execute(query)
    results = mycursor.fetchall()

    flag = False
    for i in results:
      if i[4]==user:
        if i[5]==password:
          flag = True
          return HttpResponse("Login Successful!!")
        else:
          return HttpResponse("Invalid Password.")

      if flag==False:
        return HttpResponse("Invalid Username.")
    return HttpResponse("Ok.")

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
    print(code_entered,code_generated)
    print(type(code_entered),type(code_generated))
    if code_entered == str(code_generated):
      return render(request, 'login/reset.html')
    else:
      return HttpResponse("Wrong code")

def reset(request):
    new_user = request.POST.get('user')
    new_password = request.POST.get('password')
    print(new_user, new_password)
    query = "UPDATE signup SET user_name=%s , password=%s WHERE email_id=%s"

    mycursor.execute(query, [new_user, new_password,reciever])

    mydb.commit()
    return render(request, 'login/index.html')
   




