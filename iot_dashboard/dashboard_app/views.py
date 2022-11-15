from django.shortcuts import render,redirect
from django import template
from .forms import SignUpForm,DeviceDetailsModelForm,LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
import requests
from requests.auth import HTTPDigestAuth
from datetime import datetime
from sqlite3 import Timestamp
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import pymongo
from pymongo import MongoClient
from .models import DeviceDetails
from .serializer import DeviceDetailsSerializer
import requests
from django.http import HttpResponse
from rest_framework import status
import pprint
# Create your views here.

def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://localhost:27017"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database
    return client['emv_db']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    db = get_database()
    collection = db["user"]
    collection = db["user_device"]


def users(username):
    CONNECTION_STRING = "mongodb://localhost:27017"
    client = MongoClient(CONNECTION_STRING)

    db  = client['emv_db']
    collection = db["user"]

    for x in collection.find({'username':username}):
        print(x)
def Merge(dict1, dict2):
    return(dict2.update(dict1))

def coll_user(collection_name,input):
    db =  get_database()
    collection =  db[collection_name]
    timestamp = {"Timestamp":datetime.utcnow().now()}
    Merge(input,timestamp)
    collection.insert_one(timestamp).acknowledged
    return {"Success"}

def display_userdetails(username,password1):
    db = get_database()
    collection =  db["username"+"email"+"password1"+"password2"]
    dict = []
    for display in collection.find():
        dict.append({"username":display['username'],"email":display['email'],"password1":display['password1'],"password2":display['password2']}) 
    return dict

def Merge1(dict1, dict2):
    return(dict2.update(dict1))

def coll_device(collection_name,input):
    db =  get_database()
    collection =  db[collection_name]
    timestamp = {"Timestamp":datetime.utcnow().now()}
    Merge1(input,timestamp)
    collection.insert_one(timestamp).acknowledged
    return {"Success"}

def display_devicedetails(userID):
    db = get_database()
    collection =  db["userID"+"status"+"devicetype"+"name"]
    dict = []
    for display in collection.find():
        dict.append({"userID":display['userID'],"status":display['status'],"devicetype":display['devicetype'],"name":display['name']}) 
    return dict

def single_statusupdate(username,password):
    db = get_database()
    collection =  db['username'+'password']
    x = collection.find_one({"username":username})
    dict = []
    dict.append({"deviceID":x['deviceID'],"status":x['status'],"device_name":x['device_name'],"device_type":x['device_type'],"data":x['device_data']}) 
    return dict


# def home(request):
#     response = requests.get('http://127.0.0.1:3000/device/')
#     user_device = response.json()
#     # pprint.pprint(user_device)
#     return render(request, "hello.html", {'user_device': user_device})
#     pass

def home(request):
    return render(request,'hello.html', {})

def about(request):
    return render(request,'about.html',{})

def signup(request):
    msg = None
    success = False
    # print('xyz')
    if request.method == "POST":
        form = SignUpForm(request.POST)
        # print(form)
        # response = request.get('form')
        # ans = coll_user('user',form)
        if form.is_valid():
            instance = form.save()
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password1 = form.cleaned_data.get("password1")
            # print(username)
            password2 = form.cleaned_data.get("password2")
            #user = authenticate(username=username, password=raw_password)


            msg = 'User created - please <a href="/login">login</a>.'
            success = True
            add_user(username,email,password1,password2)

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"register_form": form, "msg": msg, "success": success})


    

def signin(request):
    form = LoginForm(request.POST or None)
    # print(user)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            # password1 = form.cleaned_data.get("password1")
            # user = authenticate(username=username, password1=password1)
            user = get_user(username)
            print(user)
            if username in user:
                # login(request, user)
                return redirect("/home")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "signin.html", {"login_form": form, "msg": msg})

    
def logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("/signin")





def get_user(username):
    url = 'http://127.0.0.1:3000/user/'
    
    data = {
            "username": username,           
        }
    response = requests.get(url, data=data)
    response = response.json()
    ans = users('username')



def add_user(username,email, password1,password2):
    url = 'http://127.0.0.1:3000/user/'
    data = {
            "username": username,
            "email" : email,
            "password1": password1,
            "password2" :password2
            
        }
    response = requests.post(url, data=data)
    ans = coll_user('user',data)

