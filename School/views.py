from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from School.models import student_details,admin,inquary,student_log,teacher_log,ExamQ,meating
from django.contrib.sessions.models import Session
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

def home(request):
    return render(request,'schoolwebsite.html')
def adform(request):
    return render(request,'adform.html')
#office
def login(request):
    if request.session.has_key("b"):
        b = student_details.objects.all()
        return render(request,'officedash.html',{"b":b})
    return render(request,'login.html')
#office LogOut
def logoff(request):
    del request.session['b']
    return render(request,"schoolwebsite.html")
def back(request):
    del request.session['b']
    return render(request,"schoolwebsite.html")
def exoffice(request):
    permission_classes = (IsAuthenticated,)
    return render(request,'video.html')
#student
def sexam(request):
    return render(request,'Examdash.html')
def exam2(request):
    a=ExamQ.objects.all()
    #a. delete()
    return render(request,'Examdemo.html',{"b":a})
def student(request):
    if request.session.has_key("s"):
        return render(request,'studentdash.html')
    else:
        return render(request,'studentlog.html')
def slogof(request):
    del request.session['s']
    return render(request,'schoolwebsite.html')
def slog(request):
    roll = request.POST.get('roll')
    passw = request.POST.get('pass')
    passw = str(passw)
    try:
        if roll!="" and passw!='':

            try:
                a = student_log.objects.filter(suser=roll, spin=passw)
                if a[0].suser==roll and a[0].spin==passw:
                    request.session["s"] = "l"
                    b = meating.objects.filter()
                    return render(request,'studentdash.html')
            except:
                return render(request,'studentlog.html',{"msg":2})
        return render(request, 'studentlog.html', {"msg": 2})
    except:
        return render(request,'studentlog.html',{"msg":2})
def stdsignup(request):

    return render(request,'studsinup.html')

def adstd(request):
    suser =request.POST.get('user')
    spass =request.POST.get('pass')
    try:
        if suser!="" and spass!="":
            a = student_log(suser = suser,spin =spass)
            a.save()
            return render(request,'studsinup.html',{"msg":1})
        else:
            return render(request, 'studsinup.html', {"msg": 2})
    except:
        return render(request,'studsinup.html',{'msg':1})

def liv(request):
    clas = request.POST.get("cars")
    subj = request.POST.get("subj")
    link = request.POST.get("comment")
    a = meating(clas =clas , subj=subj,link=link)
    a.save()
    return render(request,'teacherdash.html')


## teacher
def taddstd(request):
    std=request.POST.get("cars")
    rollno=request.POST.get("rollno")
    name =request.POST.get("name")
    usrid=request.POST.get("usrid")
    passw =request.POST.get("passw")
    try:
        if std !="" and rollno!="" and name!="" and usrid!="" and passw !="":
            a = student_log(cls =std, rollno=rollno, name=name, suser=usrid,spin=passw)
            a.save()
            return render(request,'teacherdash.html',{"msg":2})
        else:
            return render(request,'teacherdash.html',{"msg":1})
    except:


        return render(request, 'teacherdash.html',{"msg":1})


def exam(request):
    clas =request.POST.get("cars")
    question = request.POST.get("comment")
    choice =request.POST.get("optradio")

    opta =request.POST.get("text2")
    optb=request.POST.get("text2")
    optc=request.POST.get("text3")
    optd=request.POST.get("text4")
    '''
    print(clas)
    print(question)
    print(anstype)
    print(opta)
    print(optb)
    print(optc)
    print(optd)
    '''
    try:
        if  clas != "" and question !="" and choice !="" and opta !="" and optb !=""and optc !=""and optd !="":

            a=ExamQ(clas=clas, question=question,choice=choice,a=opta,b=optb,c=optc,d=optd)
            a.save()

            return render(request,'teacherdash.html')
        else:
            return render(request,'teacherdash.html',{"msg":1})
    except:
        return render(request, 'teacherdash.html', {"msg": 1})
def teacher(request):
    if request.session.has_key("t"):
        return render(request,'teacherdash.html')
    return render(request,'teacherlog.html')
def tecsin(request):
    return render(request,'teachersinup.html')
def tlogof(request):
    del request.session['t']
    return render(request,'schoolwebsite.html')
def adtech(request):
    tuserr = request.POST.get('user')
    tpass = request.POST.get('pass')
    try:
        if tuserr!="" and tpass!="":
            a =teacher_log(tuser=tuserr,tpin =tpass)
            a.save()
        return render(request,'teachersinup.html',{"msg":1})
    except:
        return render(request,'teachersinup.html',{"msg":2})
def tlog(request):
    tuser = request.POST.get("roll")
    tpass =request.POST.get('pass')
    a= teacher_log.objects.filter(tuser=tuser,tpin =tpass)
    try:
        if a[0].tuser ==tuser and a[0].tpin==tpass:
            request.session["t"] = "o"
            return render(request,'teacherdash.html')
    except:
        return render(request,'teacherlog.html',{"msg":2})
def otp(request):
    return render(request,'otp.html')
def veri(request):
    user = request.POST.get("user")
    mob = request.POST.get("mob")
    if user != "" and mob !="":
        return render(request,'otp.html',{"msg":1})
    else:
        if user != "":
            try:
                a = admin.objects.filter(Userid=user)
                if a != None:

                    import requests

                    url = "https://www.fast2sms.com/dev/bulk"

                    querystring = {
                        "authorization": "WXYMP3QVadGfvDmrSOTkgHxtyUEZ5c8epF1BNb4lhLCj0nqR9ukrtY2FJM5GdN6C7HT1yx3QLDifWqul",
                        "sender_id": "FSTSMS", "message": "This is Your Password "+str(a[0].pin), "language": "english", "route": "p",
                        "numbers": a[0].phno}

                    headers = {
                        'cache-control': "no-cache"
                    }

                    response = requests.request("GET", url, headers=headers, params=querystring)

                    res=response.text
                    return render(request,'otp.html',{"msg":2,"res":res})
                else:

                    return render(request,'otp.html',{"msg":3})
            except:
                return render(request,'otp.html',{"msg":6})
        else:
            mob =int(mob)
            try:


                a = admin.objects.filter(phno=mob)

                if a!=None:

                    import requests

                    url = "https://www.fast2sms.com/dev/bulk"

                    querystring = {
                        "authorization": "WXYMP3QVadGfvDmrSOTkgHxtyUEZ5c8epF1BNb4lhLCj0nqR9ukrtY2FJM5GdN6C7HT1yx3QLDifWqul",
                        "sender_id": "FSTSMS", "message": "This is Your Password " + str(a[0].pin), "language": "english",
                        "route": "p",
                        "numbers": a[0].phno}

                    headers = {
                        'cache-control': "no-cache"
                    }

                    response = requests.request("GET", url, headers=headers, params=querystring)

                    res=response.text
                    return render(request,'otp.html',{"msg":4,"res":res})
                else:
                    return render(request,'otp.html',{"msg":5})
            except:
                return render(request,'otp.html',{"msg":6})

def logs(request):

    user = request.POST.get("user")
    passw = request.POST.get("pass")

    try:
        passw = int(passw)
        if user != "" and passw != "":

            a = admin.objects.filter(Userid__exact=user,pin__exact= passw)
            if a[0].Userid == user and a[0].pin == passw:

                b = student_details.objects.all()
                request.session["b"]="m"
                return render(request,'officedash.html',{"b":b})
            else:
                msg=1
                return render(request, 'login.html', {"msg": msg})
        else:
            msg=3
            return render(request, 'login.html', {"msg": msg})
    except:
        msg = 3
        return render(request, 'login.html', {"msg": msg})

def inq(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    message = request.POST.get("msg")
    try:
        if email != "" and phone!="" and message!="":
            a = inquary(name=name,email=email,phno=phone,Comment=message)
            a.save()
            b= inquary.objects.all()
            #b.delete()
            return render(request,'schoolwebsite.html',{"inq":b})
    except:
        return  render(request,'template.html')


    return render(request,'template.html')
def signup(request):
    import smtplib
    sender = request.POST.get('email')
    msg = request.POST.get('msg')
    send = sender
    rec = ['shrikantsawarkar97@gmail.com']
    message = msg
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, rec, message)
        print("Successfully sent email")

    except :

        print("Error: unable to send email")


    return render(request,'signup.html')

def adminadd(request):

    user = request.POST.get('user')
    passw = request.POST.get("pass")
    mob = request.POST.get("mobile")
    if user != "" and passw != "":

        a = admin(Userid=user,pin=passw,phno = mob)
        a.save()

        msg = 1
        return render(request, 'signup.html', {"msg": msg})
    else:
        msg = 2
        return render(request,'signup.html',{"msg":msg})

def dimm(request):
    cars =request.POST['cars']
    Username =request.POST['Username']
    Middlename =request.POST['Middlename']
    Lastname =request.POST['Lastname']

    Mothers_Name =request.POST['Mothers_Name']

    Nationality =request.POST['Nationality']

    Religion =request.POST['Religion']

    Category =request.POST['Category']

    Caste =request.POST['Caste']

    Mother_Tongue =request.POST['Mother_Tongue']

    Gender =request.POST['Gender']

    dob =request.POST['dob']

    pob =request.POST['pob']

    Age =request.POST['Age']

    Aadhar_no =request.POST['Aadhar_no']

    Bg =request.POST['Bg']

    Addr_of_com =request.POST['Addr_of_com']
    School_attended_by_the_child =request.POST['School_attended_by_the_child']
    school_mob =request.POST['school_mob']
    # guardian info

    Gurdian_Name =request.POST['Gurdian_Name']

    Relationship =request.POST['Relationship']

    Contact_No =request.POST['Contact_No']

    # parent information

    fatherdob =request.POST['fatherdob']

    father_Quli =request.POST['father_Quli']

    mother_name =request.POST['mother_name']

    Mother_dob =request.POST['Mother_dob']

    mother_Quli =request.POST['mother_Quli']

    E_mail =request.POST['E_mail']

    father_mob =request.POST['father_mob']

    parents_addr =request.POST['parents_addr']

    LGSPOKEH =request.POST['LGSPOKEH']
    bestlang =request.POST['bestlang']
    howtakecare =request.POST['howtakecare']
    speccial_needs =request.POST['speccial_needs']
    date =request.POST['date']
    place = request.POST['place']
    # files

    parentsign =  request.FILES.get('parentsign',None)

    aadhar =request.FILES.get('aadhar',None)
    birthcirti =request.FILES.get('birthcirti',None)

    tc = request.FILES.get('tc',None)

    Marksheet = request.FILES.get('Marksheet',None)
    san = request.FILES.get('san',None)

    IDProof = request.FILES.get('IDProof',None)
    stdphoto = request.FILES.get('stdphoto',None)

    dic={"parentsign":parentsign,
         "aadhar": aadhar,
        "birthcirti":birthcirti,
        "tc":tc,
        "Marksheet":Marksheet,
        "san":san,
        "IDProof":IDProof,
         "stdphoto":stdphoto
         }


    for i in dic:


        if dic.get(i)==None:
            dic[i]=":(NOimg.png"

    if cars!="" and Username!="":
            a= student_details(
                cars=cars,
            Username =Username,
            Middlename = Middlename,
            Lastname = Lastname,

            Mothers_Name = Mothers_Name,

            Nationality =Nationality ,

            Religion = Religion,

            Category =Category ,

            Caste =Caste ,
            Mother_Tongue = Mother_Tongue,

            Gender = Gender,

            dob =dob ,

            pob =pob ,

            Age = Age,

            Aadhar_no =Aadhar_no ,

            Bg =  Bg ,

            Addr_of_com =Addr_of_com ,
            School_attended_by_the_child = School_attended_by_the_child,
            school_mob =school_mob ,
            # guardian info

            Gurdian_Name =Gurdian_Name ,

            Relationship = Relationship,

             Contact_No=Contact_No ,

            # parent information

            fatherdob = fatherdob,

            father_Quli =father_Quli ,

            mother_name = mother_name,

            Mother_dob =Mother_dob ,

            mother_Quli =mother_Quli ,

            E_mail =E_mail ,

            father_mob =father_mob ,

            parents_addr = parents_addr,

            LGSPOKEH =LGSPOKEH ,
                bestlang =bestlang ,
            howtakecare = howtakecare,
            speccial_needs =speccial_needs ,
            date =date ,
            place=place,

            # files

            parentsign =dic.get("parentsign")  ,

            aadhar =dic.get("aadhar") ,
            birthcirti = dic.get("birthcirti"),

            tc = dic.get("tc"),

            Marksheet = dic.get("Marksheet"),
            san = dic.get("san"),
            stdphoto = dic.get("stdphoto"),

            IDProof =dic.get("IDProof")
                )

            a.save()

    msg ="recoard inserted suscessfully "




    return  render(request,"adform.html",{"msg":msg})

'''
def show(request):
    rec = student_details.objects.all()
    return render(request,'home.html',{"rec":rec})
'''
def update(request,id):
    b= student_details.objects.filter(id = id)

    dist={
          1:"one",
          2:"two",
          3:"three",
          4:"four",
          5:"five",
          6:"six",
          7:"seven",
          8:"eight",
          9:"nine",
          10:"ten"

          }
   
    xb=dist[b[0].cars]

    min={"Indian":"one",
         "Foreign":"two"
         }
    min =min[b[0].Nationality]
    rel = {"Hinduism": "one",
           "Islam": "two",
           "Christianity":"three",
           "Sikhism":"four",
           "Buddhism":"five",
           "Jainism":"six",
           "Zoroastrianism": "seven",
           "Judaism": "eight"
           }
    rel =rel[b[0].Religion]
    cat = {"OPEN":"one",
           "OBC": "two",
           "SC": "three",
           "ST": "four",
           "NT": "five",
           "VJNT": "six",
           "OTHER": "seven"
           }
    cat =cat[b[0].Category]
    gen={"Male":"one",
         "Female":"two"}
    gen =gen[b[0].Gender]


    bg ={"Apos":"one",
         "Anv": "two",
         "Bpos": "three",
         "Bnv": "four",
         "Opos": "five",
         "Onv": "six",
         "ABpos": "seven",
         "ABnv": "eight",
         }
    bg= bg[b[0].Bg]
    res =b[0]
    return render(request,"adform.html",{xb:"selected",min:"selected",rel:"selected",cat:"selected",gen:"selected",bg:"selected","res":res})

def delete(request,id):
    b = student_details.objects.filter(id=id)
    b.delete()
    msg = "recrd deleted "
    return  render(request,"home.html",{"msg":msg})

def display(request):

    b = student_details.objects.all()
    return render(request,"display.html",{"b":b})

def search(request):
    msg="this is rup"
    name =request.POST.get('namee')
    id = request.POST.get('id')
    #roll =request.POST['rol']
    std = request.POST.get('std')
    if name != None:
        b =student_details.objects.filter(Username=name)
        return render(request,"display.html",{"b":b})
    elif id != None:
        b= student_details.objects.filter(id =id)
        return render(request, "display.html", {"b": b})
    elif std != None:
        b=student_details.objects.filter(cars=std)
        return render(request, "display.html", {"b": b})


    return  render(request,'home.html',{"msg":msg})



