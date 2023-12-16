from django.shortcuts import render,redirect
from BackendApp.models import HairTypeDB,HairproblemDB,HairBrandDB,Product_typeDB,AddproductDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.



def index(request):
    return render(request,"index.html")


def Haircate(request):
    return render(request,"Hairtype.html")

def Hairdata(request):
    if request.method=="POST":
        na = request.POST.get('name')
        des = request.POST.get('description')
        im = request.FILES['HairtypeImage']

        obj = HairTypeDB(Hair_name=na,Hair_des=des,Hair_image=im)
        obj.save()
        messages.success(request,'Successfully added HairType.')
        return redirect(Haircate)

def displayhair(request):
    hair = HairTypeDB.objects.all()
    return render(request,"displayhair.html",{'hair':hair})


def edithair(request,dataid):
    hairt = HairTypeDB.objects.get(id=dataid)
    return render(request,"edithair.html",{'hairt':hairt})

def hairupdate(request,dataid):
    if request.method=="POST":
        nm = request.POST.get('name')
        de = request.POST.get('description')

        HairTypeDB.objects.filter(id=dataid).update(Hair_name=nm,Hair_des=de)
        return redirect(displayhair)

def hairdelete(request,dataid):
        hairt = HairTypeDB.objects.filter(id=dataid)
        hairt.delete()
        return redirect(displayhair)



def hairpr(request):
    return render(request,"hairproblem.html")


def hairprbl_data(request):
    if request.method=="POST":
        ne = request.POST.get('name')
        ds = request.POST.get('description')
        ig = request.FILES['HairProblem']

        obj = HairproblemDB(hair_prblm=ne,hairprblm_de=ds,prblm_image=ig)
        obj.save()
        messages.success(request,'Successfully Added.')
        return redirect(hairpr)

def hair_problemdisplay(request):
    hairpro = HairproblemDB.objects.all()
    return render(request,"displayhairproblem.html", {'hairpro':hairpro})


def edit_hairproblem(request,dataid):
    hairprb = HairproblemDB.objects.get(id=dataid)
    return render(request,"edithairproblem.html",{'hairprb':hairprb})

def hairproblem_upade(request,dataid):
    if request.method=="POST":
        nm = request.POST.get('name')
        de = request.POST.get('description')
        try:
            im = request.FILES['HairProblem']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = HairproblemDB.objects.get(id=dataid).prblm_image
        HairproblemDB.objects.filter(id=dataid).update(hair_prblm=nm,hairprblm_de=de,prblm_image=file)
        return redirect(hair_problemdisplay)


def hairproblem_delete(request,dataid):
    hairprb = HairproblemDB.objects.filter(id=dataid)
    hairprb.delete()
    return redirect(hair_problemdisplay)


def brand(request):
    return render(request,"Brand.html")

def brand_data(request):
    if request.method=="POST":
        nm = request.POST.get('name')
        img = request.FILES['brandImage']

        obj = HairBrandDB(hairbrand_name=nm,hairbrand_img=img)
        obj.save()
        messages.success(request,'Successfully added Brand')
        return redirect(brand)


def displaybrand(request):
    brand = HairBrandDB.objects.all()
    return render(request,"displaybrand.html",{'brand':brand})

def brand_edit(request,dataid):
    brande = HairBrandDB.objects.get(id=dataid)
    return render(request,"brandedit.html",{'brande':brande})

def brand_update(request,dataid):
    if request.method == "POST":
        ne = request.POST.get('name')

        try:
            im = request.FILES['brandImage']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = HairBrandDB.objects.get(id=dataid).hairbrand_img
        HairBrandDB.objects.filter(id=dataid).update(hairbrand_name=ne, hairbrand_img=file)
        return redirect(displaybrand)

def brand_delete(request,dataid):
    brande = HairBrandDB.objects.filter(id=dataid)
    brande.delete()
    return redirect(displaybrand)


def product_type(request):
    return render(request,"producttype.html")

def product_typedata(request):
    if request.method=="POST":
        na = request.POST.get('name')
        de = request.POST.get('description')
        im = request.FILES['ProducttypeImage']

        obj = Product_typeDB(product_name=na,product_des=de,Product_img=im)
        obj.save()
        messages.success(request,'Successfully Added.')
        return redirect(product_type)


def product_typedisplay(request):
    prot = Product_typeDB.objects.all()
    return render(request,"producttypedisplay.html",{'prot':prot})


def product_typeedit(request,dataid):
    data = Product_typeDB.objects.get(id=dataid)
    return render(request,"producttype_edit.html",{'data':data})


def producttype_update(request,dataid):
    if request.method == "POST":
        ne = request.POST.get('name')
        de = request.POST.get('description')

        try:
            im = request.FILES['ProducttypeImage']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = Product_typeDB.objects.get(id=dataid).Product_img
        Product_typeDB.objects.filter(id=dataid).update(product_name=ne,product_des=de,Product_img=file)
        return redirect(product_typedisplay)

def producttype_delete(request,dataid):
    data = Product_typeDB.objects.filter(id=dataid)
    data.delete()
    return redirect(product_typedisplay)


def addproduct(request):
    hairty = HairTypeDB.objects.all()
    hairpr = HairproblemDB.objects.all()
    hairpro = Product_typeDB.objects.all()
    brand = HairBrandDB.objects.all()
    return render(request,"Addproduct.html",{'hairty':hairty,'hairpr':hairpr,'hairpro':hairpro,'brand':brand})



def product_data(request):
    if request.method == "POST":
        tna = request.POST.get('hairtypename')
        prn = request.POST.get('hairproblemname')
        pdn = request.POST.get('hairproductname')
        bna = request.POST.get('brandname')
        nae = request.POST.get('productname')
        de = request.POST.get('desription')
        pri = request.POST.get('prize')
        img = request.FILES['productimage']

        obj = AddproductDB(Hairtype_name=tna,Problem_name=prn,Producttype_name=pdn,Brand_name=bna,Product_name=nae,Product_des=de,Prize=pri,Image=img)
        obj.save()
        messages.success(request,'Successfully Added products')
        return redirect(addproduct)


def adddisplay(request):
    addpro = AddproductDB.objects.all()
    return render(request,"addprodisplay.html",{'addpro':addpro})


def addedit(request,dataid):
    add = AddproductDB.objects.get(id=dataid)
    return render(request,"editaddpro.html",{'add':add})

def addpro_update(request,dataid):
    if request.method == "POST":
        tne = request.POST.get('hairtypename')
        prn = request.POST.get('hairproblemname')
        pdna = request.POST.get('hairproductname')
        bnam = request.POST.get('brandname')
        nae = request.POST.get('productname')
        de = request.POST.get('desription')
        pri = request.POST.get('prize')

        try:
            im = request.FILES['productimage']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = AddproductDB.objects.get(id=dataid).Image
        AddproductDB.objects.filter(id=dataid).update(Hairtype_name=tne,Problem_name=prn,Producttype_name=pdna,Brand_name=bnam,Product_name=nae,Product_des=de,Prize=pri,Image=file)
        return redirect(adddisplay)


def add_delete(request,dataid):
    add = AddproductDB.objects.filter(id=dataid)
    add.delete()
    return redirect(adddisplay)

def adminlogin(request):
    return render(request,"login.html")


def admin_login(request):
    if request.method == "POST":
        un = request.POST.get('user_name')
        pwd = request.POST.get('pass_word')

        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username'] = un
                request.session['password'] = pwd
                return redirect(index)
            else:
                return redirect(admin_login)
        else:
            return redirect(adminlogin)



def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminlogin)