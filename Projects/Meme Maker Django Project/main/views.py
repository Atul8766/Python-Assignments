from django.http import HttpResponse
from django.shortcuts import render, redirect
from .utils import registerUser, loginUser
from django.contrib.sessions.backends.db import SessionStore  # For session Storage
import psycopg2
import requests
import bcrypt

session = SessionStore()

# Create your views here.
try:
    conn = psycopg2.connect(
        host='127.0.0.1',
        port='5432',
        database='memestore',
        user='postgres',
        password='root'
    )
    print("Database Connect Succesfully")
except Exception as e:
    print('Error : ', e)
    print("Database Connection Failed")


conn.autocommit = True
cursor = conn.cursor()


def blank(request):
    return HttpResponse("<h1>Welcome to the project</h1>")


def home(request):
    return HttpResponse("<h1>Welcome To Django Boy</h1>")


# MiddleWare

def checkSession():
    try:
        email = session['email']
        return True
    except Exception as error:
        print(error)
        return False


def register(request):

    sessionExists = checkSession()
    if sessionExists == False:
        if request.method == 'POST':
            # collecting all data from client

            name = request.POST['name']
            contact = request.POST['contact']
            email = request.POST['email']
            password = request.POST['password']

            print(f'Name : {name}')
            print(f'Contact : {contact}')
            print(f'Email : {email}')
            print(f'Password : {password}')

            password = password.encode()
            # hashing the passwords
            hashed = bcrypt.hashpw(password,bcrypt.gensalt())
            hashed = hashed.decode('utf-8')

            # create userDictionary
            userData = {
                'name': name,
                'contact': contact,
                'email': email,
                'password': hashed
            }

            response = registerUser(userData, cursor)

            print(response)

            if response['statuscode'] == 200:
                # session Store
                session['email'] = userData['email']
                session['password'] = userData['password']

                # return render(request, 'register.html', {'message': "Succesfully Recived"})
                return redirect('/dashboard/')

            else:
                return render(request, 'register.html', {'message': 'Already Registerd'})
        else:
            return render(request, 'register.html')
    else:
        return redirect('/dashboard/')


def login(request):

    sessionExist = checkSession()
    if sessionExist == False:

        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']

            print("Email : ", email)
            print("password : ", password)

            userData = {
                'email': email,
                'password': password
            }

            response = loginUser(userData, cursor)

            if response['statuscode'] == 200:
                session['email'] = userData['email']
                session['password'] = userData['password']

                # return render(request, 'login.html', {'message': "Succesfully Logged In"})
                return redirect('/dashboard/')
            elif response['statuscode'] == 503 and response['message'] == 'pwderror':
                return render(request, 'login.html', {'message1': "Password Not Matched"})
            else:
                return render(request, 'register.html', {'message': "User Not Found/Not Registered"})
        else:
            return render(request, 'login.html')
    else:
        return redirect('/dashboard/')


def logout(request):
    try:
        session.clear()
        return redirect('/login/')
    except:
        return render(request, 'dashboard.html')


def dashboard(request):
    sessionexists = checkSession()

    r = requests.get("https://api.imgflip.com/get_memes")

    meme_data = r.json()

    #meme name ,meme url, meme id

    if sessionexists == False:
        return redirect('/login/')


    else:
        print(meme_data['data']['memes'])
        memes_data = {
            'data' : r.json()['data']['memes']
        }
        return render(request, 'dashboard.html',context=memes_data)

def editmeme(request):
   sessiostatus = checkSession()
   if sessiostatus:
        #display edit page
        template_id = request.GET['id'] 

        context={
            'meme_id':template_id
        }

        return render(request,"editmeme.html",context)
   else:
        return redirect("/login/")


def memedetails(request):
    sessiostatus = checkSession()

    if sessiostatus:
        if request.method == 'POST':
            template_id = request.POST['id']
            text0 = request.POST['text1']
            text1 = request.POST['text2']
            
            #POST request meme API

            payload = {
                'template_id' : template_id,
                'username' : 'Shukla_.ji',
                'password' : 'Q3YTGyvb+6CWsrc',
                'text0' : text0,
                'text1' : text1
            } 

            response = requests.request('POST','https://api.imgflip.com/caption_image',params=payload).json()
            print(response)
            html_str = f'''
                    <h1>Response</h1>
                    <img style = "height:200px, width:200px" src="{response['data']['url']}" alt="meme">
                    <a href="{response['data']['url']}">View Image </a>
            '''
            return HttpResponse(html_str)
    else:
        return redirect("/login/")
