"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.core.mail import send_mail
from random import randint
from datetime import datetime
import os

''' Do'nt Edit anything '''

def currentDateTime(number):
    now = datetime.now()
    if number == 'number' or number == 'numb':
        now = {
            'date':int(now.strftime("%d")),
            'month':int(now.strftime("%m")),
            'year':int(now.strftime("%Y")),
            'hour':int(now.strftime("%H")),
            'minute':int(now.strftime("%M")),
            'second':int(now.strftime("%S"))
        }
    elif number == 'str' or number == 'string' or number == 'character' or number == 'char':
        now = {
            'date':now.strftime("%d"),
            'month':now.strftime("%m"),
            'year':now.strftime("%Y"),
            'hour':now.strftime("%H"),
            'minute':now.strftime("%M"),
            'second':now.strftime("%S")
        }
    else:
        try:
            number.replace("dd", "%d")
            number.replace("mm", "%m")
            number.replace("yy", "%Y")
            number.replace("HH", "%H")
            number.replace("MM", "%M")
            number.replace("SS", "%S")
            now.strftime(number)
        except:
            now.strftime("%d %m %Y %H %M %S")
    return now 

def read_array(filename):
    with open(filename, 'r') as myfile:
        a = myfile.read()
    array_d = [0, 0]
    k = 0
    refer = ''   
    for i in range(0, len(a)): 
        if a[i] == '\n':
            break
        if a[i] != ' ' and a[i] != '\n':
            refer = refer + a[i]
        if a[i] == ' ':
            try:
                array_d[k] = int(refer)
            except:
                array_d[k] = refer
            k += 1
            refer = ''           
    b = list(range(0, array_d[0]))
    for i in range(0, array_d[0]):
        b[i] = list(range(0, array_d[1]))
    array_D = True 
    for i in range(0, len(a)):
        if a[i] == '\n' and array_D:
            array_D = False
            k = 0
            j = 0
            refer = ''
            continue
        if not array_D:
            if a[i] != ' ' and a[i] != '\n':
                refer = refer + a[i]
            if a[i] == ' ':
                try:
                    b[j][k] = int(refer)
                except:
                    b[j][k] = refer
                k += 1
                refer = ''
            if a[i] == '\n':
                k = 0
                j += 1
    return b

def write_array(filename, array, mode):
    with open(filename, mode) as myfile:
        r = len(array)
        c = len(array[0])
        if mode == 'w':
            myfile.write(str(r) + ' ' + str(c) +  ' ')
        for i in range(0, r):
            myfile.write('\n')
            for j in range(0, c):
                myfile.write(str(array[i][j]))
                myfile.write(' ')

file_location = {}
directory = os.path.dirname(os.path.abspath(__file__))
directory = directory.replace('\\','/') + '/'
file_location['loginFiles'] = directory + 'templates/login/files/'
file_location['loginDir'] = directory
file_location['projectDir'] = os.path.dirname(os.path.dirname(directory))
file_location['projectDir'] += '/'

for x in os.listdir('.'):
    if os.path.isfile(x) and (x.find('.pyproj.user') != -1 or x.find('.pyproj') != -1): 
        yourProjectName = x
        yourProjectName = yourProjectName.replace('.pyproj.user','')
        yourProjectName = yourProjectName.replace('.pyproj','')
        break

file_location['projectApp'] = file_location['projectDir'] + yourProjectName + '/'

try:
    from . import importing
    EMAIL_HOST_USER = importing.EMAIL_HOST_USER
    website = importing.WEBSITE_NAME
except:
    with open(directory + 'importing.py' , 'w') as file:
        file.write('\nfrom ' + yourProjectName + '.settings import EMAIL_HOST_USER, WEBSITE_NAME\n')
    try:
        from . import importing
        EMAIL_HOST_USER = importing.EMAIL_HOST_USER
        website = importing.WEBSITE_NAME
    except:
        try:
            with open(file_location['projectApp'] + 'settings.py', 'r') as file:
                settings = file.read()
        except:
            print("Location")
            print("your _______login_______ app location: " + file_location['loginDir'])
            print("your _______Project_______ directory location: " + file_location['projectDir'])
            print(file_location['projectApp'] + "settings.py")
            print("!!!!!!!!!!!!!!!!!!!!ERROR!!!!!!!!!!!!!!!!!!!!")
            print('settings.py not found in this' + file_location['projectApp'])
            print("Setup Your Email Details in " + file_location['projectApp'] + 'settings.py')
            print("Or Try to keep _________" + yourProjectName + "_________ Project in this " + file_location['projectDir'])
            print("Or Try to keep _________login_________ App in this " + file_location['projectDir'])
        if settings.find('EMAIL_HOST_PASSWORD') != -1 and settings.find('EMAIL_BACKEND') != -1 and settings.find('EMAIL_HOST') != -1  and settings.find('EMAIL_USE_TLS') != -1 and settings.find('EMAIL_PORT') != -1 and settings.find('EMAIL_HOST_USER') != -1:
            print("!!!!!!!!!!!!!!!!!!!!ERROR!!!!!!!!!!!!!!!!!!!!")
            print("Restart Your Program Execution")
        else:
            print("!!!!!!!!!!!!!!!!!!!!ERROR!!!!!!!!!!!!!!!!!!!!")
            print("Restart Your Program Execution")
            print("Learn How to setup email ")
            print("Follow the instructions : https://data-flair.training/blogs/django-send-email/ ")
            settings += "\n# Email\nEMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'\nEMAIL_HOST = 'smtp.gmail.com'\nEMAIL_USE_TLS = True\nEMAIL_PORT = 587\nEMAIL_HOST_USER = " + "Follow the instructions : https://data-flair.training/blogs/django-send-email/" + "\nEMAIL_HOST_PASSWORD = " + "Follow the instructions : https://data-flair.training/blogs/django-send-email/" + "\nEMAIL_USE_SSl = False"
            settings += '\n\nWEBSITE_NAME = "MY WEBSITE NAME"\n'
            with open(file_location['projectApp'] + 'settings.py', 'w') as file:
                file.write(settings)
try:
    details = read_array(file_location['loginFiles'] + 'login.txt')
    a = list(range(0, 10))
    for i in range(0, 10):
        a = details[0][i]
    del a
    del details
except:
    current = currentDateTime('str')
    array = [['Sample_name', 'Sample1234@gmail.com', 'Sample1234@', current['date'], current['month'], current['year'], current['hour'], current['minute'], current['second'], 0]]
    write_array(file_location['loginFiles'] + 'login.txt', array, 'w')

storage = {'OTP':'', 'name':'', 'email':'', 'password':'', 'time':0}

def storageReset():
    storage['name'] = ''
    storage['email'] = ''
    storage['password'] = ''
    storage['OTP'] = str(randint(0,1000)) + str(randint(0,1000)) + str(randint(0,1000)) + str(randint(0,1000))
    storage['time'] = 0

def htmlContent(array):
    t = '<p>'
    for j in range(0,len(array)):
        if array[j]=='~':       
            t += '</p>~<p>'     
        elif array[j]=='\n':    
            t += '</p><p>'      
        elif array[j]==' ':     
            t += '&nbsp;'       
        elif array[j]=='>':     
            t += '&gt;'         
        elif array[j]=='<':     
            t += '&lt;'         
        else:                   
            t += array[j]       
    return t

def gmail(recepient, subject, message):
    try:
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    except:
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)

def signin(request):
    """Renders the signin page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'login/signin.html',
        {
            'website':website,
            'title':'Signin',
        }
   )

def signup(request):
    """Renders the signup page."""
    assert isinstance(request, HttpRequest)                   
    return render(
        request,
        'login/signup.html',
        {
            'website':website,
            'title':'Signup',
        }
   )

def load(request):
    """Renders the signin page."""
    assert isinstance(request, HttpRequest)
    if storage['time']:
        current = currentDateTime('yy-mm-dd HH:MM:SS')
        time_delta = (current - storage['time'])
        total_seconds = time_delta.total_seconds()
        if total_seconds/60 > 30:
            storageReset()
    name = ''
    email = ''
    content = request.POST
    length = len(content)
    if length == 5:
        # signup # csfr, name, email, password, confirm password
        details = read_array(file_location['loginFiles'] + 'login.txt')
        failure = False
        for i in range(0, len(details)):
            if details[i][1] == content['email']:
                failure = True
                break
        storage['OTP'] = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
        storage['name'] = content['name']
        storage['email'] = content['email']
        storage['password'] = content['password']
        subject = 'One Time Password(OTP) from' + website + 'Website'
        message = 'Hello ' + storage['name'] +' Your OTP is ' + storage['OTP']
        recepient = storage['email']
        gmail(recepient, subject, message)
        title = 'Verification'
        content = 'Enter the OTP send from ' + 'website' + ' to ' + storage['email']
        storage['time'] = currentDateTime('yy-mm-dd HH:MM:SS');
        if failure:
            content += '. <br>Email ID Already exists. <br>Your details will be overwrited.' 
    elif length == 3:
        # signin # csfr, email, password
        details = read_array(file_location['loginFiles'] + 'login.txt')
        failure = True
        success = False
        for i in range(0, len(details)):
            if details[i][1] == content['email']:
                failure = False
                if str(details[i][2]) == str(content['password']):
                    success = True
                    number = i
                break
        if not failure and not success:
            title = 'Failure!!!'
            content = 'Invalid Password'
        elif not failure and success:
            title = 'Successful!!!'
            content = 'Hello ' + details[number][0] + ' !!!'
            name = details[number][0]
            email = details[number][1]
            storageReset();
        elif failure:
            title = 'Failure!!!'
            content = 'Invalid Email ID'
    elif length == 2:
        # load # csfr, OTP
        if storage['OTP'] == content['OTP']:
            title = 'Successful!!!'
            content = 'Hello ' + storage['name'] + ' !!!'
            name = storage['name']
            email = storage['email']
            details = read_array(file_location['loginFiles'] + 'login.txt')
            length = len(details)
            available = False
            for i in range(0,length):
                if email == details[i][1]:
                    available = True
                    break
            if available:
                array = list(range(0, length))
            else:
                array = list(range(0, length + 1))
            j = -1
            for i in range(0, length):
                if email != details[i][1]:
                    array[i] = details[i]
                else:
                    j = i
            current = currentDateTime('str')
            if j == -1:
                j = length
            array[j] = [str(storage['name']), str(storage['email']), str(storage['password']), current['date'], current['month'], current['year'], current['hour'], current['minute'], current['second'], j]
            write_array(file_location['loginFiles'] + 'login.txt', array, 'w')
            storageReset();
        else:
            title = 'Failure!!!'
            content = 'OTP does\'nt match'
    elif storage['name'] != '' and storage['email'] != '' and storage['password'] != '' and storage['OTP'] != '':
        storage['OTP'] = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
        subject = 'One Time Password(OTP) from ' + website + ' Website'
        message = 'Hello ' + storage['name'] +' Your OTP is ' + storage['OTP']
        recepient = storage['email']
        gmail(recepient, subject, message)
        title = 'Verification'
        content = 'Enter the OTP send from '+ 'website' +' to ' + storage['email']
    else:
       title = 'Error!!!'
       content = 'Invalid Website link'
    return render(
        request,
        'login/load.html',
        {
            'title':title,
            'content':content,
            'name':name,
            'email':email,
            'website':website,
        }
   )