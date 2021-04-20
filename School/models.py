from django.db import models

# Create your models here.
class student_details(models.Model):
    cars = models.IntegerField()
    Username= models.CharField(max_length=100)
    Middlename =models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Mothers_Name = models.CharField(max_length=100)
    Nationality = models.CharField(max_length=50)
    Religion = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    Caste = models.CharField(max_length=100)
    Mother_Tongue= models.CharField(max_length=100)
    Gender= models.CharField(max_length=100)
    dob=models.DateField(auto_now=False, auto_now_add=False)
    pob= models.CharField(max_length=100)
    Age= models.IntegerField()
    Aadhar_no = models.BigIntegerField()
    Bg = models.CharField(max_length=100)
    Addr_of_com = models.CharField(max_length=100)
    School_attended_by_the_child = models.CharField(max_length=100)
    school_mob = models.BigIntegerField()
    #guardian info
    Gurdian_Name= models.CharField(max_length=100)
    Relationship= models.CharField(max_length=100)
    Contact_No= models.BigIntegerField()
#parent information
    fatherdob=models.DateField(auto_now=False, auto_now_add=False)
    father_Quli= models.CharField(max_length=100)
    mother_name= models.CharField(max_length=100)
    Mother_dob=models.DateField(auto_now=False, auto_now_add=False)
    mother_Quli= models.CharField(max_length=100)
    E_mail =models.EmailField(max_length=254)
    father_mob= models.BigIntegerField()
    parents_addr= models.CharField(max_length=100)
    LGSPOKEH= models.CharField(max_length=100)
    bestlang= models.CharField(max_length=100)
    howtakecare= models.CharField(max_length=100)
    speccial_needs= models.CharField(max_length=100)
    date=models.DateField(auto_now=False, auto_now_add=False)
    place = models.CharField(max_length=100)
#files
    parentsign=models.ImageField(upload_to="media",default='shri.jpg')
    aadhar=models.ImageField(upload_to="media",default='shri.jpg')
    birthcirti=models.ImageField(upload_to="media",default='shri.jpg')
    tc=models.ImageField(upload_to="media",default='shri.jpg')
    Marksheet=models.ImageField(upload_to="media",default='shri.jpg')
    san=models.ImageField(upload_to="media",default='shri.jpg')
    IDProof=models.ImageField(upload_to="media",default='shri.jpg')
    stdphoto =models.ImageField(upload_to="media",default='shri.jpg')
class admin(models.Model):
    Userid = models.CharField(max_length=100)
    pin = models.IntegerField()
    phno = models.BigIntegerField()
class inquary(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phno = models.BigIntegerField()
    Comment = models.CharField(max_length=400)
class student_log(models.Model):
    suser = models.CharField(max_length=100)
    spin = models.CharField(max_length=100)
    name =models.CharField(max_length=100)
    cls =models.CharField(max_length=100)
    rollno =models.CharField(max_length=100)
class student_subjects(models.Model):
    clas = models.IntegerField()
    phy =models.CharField(max_length=100)
    chi =models.CharField(max_length=100)
    math =models.CharField(max_length=100)
    bio =models.CharField(max_length=100)
    eng =models.CharField(max_length=100)
    mar =models.CharField(max_length=100)
    hist =models.CharField(max_length=100)
    skil =models.CharField(max_length=100)
    gio =models.CharField(max_length=100)
    geo =models.CharField(max_length=100)
class teacher_log(models.Model):
    tuser =models.CharField(max_length=100)
    tpin = models.CharField(max_length=100)
class meating(models.Model):
    clas =models.CharField(max_length=100)
    subj =models.CharField(max_length=100)
    link =models.CharField(max_length=100)
'''
## new
class notic(models.Model):
    head =models.CharField(max_length=100)
    txt = models.CharField(max_length=100)
    
    img = models.ImageField(upload_to="media",default='shri.jpg')
## new
class assinment(models.Model):
    rollno =models.ImageField()
    name = models.CharField(max_length=100)
    cls =models.CharField(max_length=100)
    assinno =models.CharField(max_length=100)
    img = models.ImageField(upload_to="media", default='shri.jpg')
'''
class ExamQ(models.Model):
    clas = models.IntegerField()
    question = models.CharField(max_length=100)
    choice = models.CharField(max_length=100)
    ##opt
    a =models.CharField(max_length=100)
    b =models.CharField(max_length=100)
    c =models.CharField(max_length=100)
    d =models.CharField(max_length=100)
