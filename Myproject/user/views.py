from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from .models import *


# Create your views here.

def home(request):
    data = category.objects.all().order_by('-id')[0:12]
    sliderdata = slider.objects.all().order_by('-id')[0:3]
    pdata = myproduct.objects.all().order_by('-id')[0:18]
    odata = myproduct.objects.filter(total_discount__gte=30)


    md = {"cdata": data, "sdata": sliderdata, "pdata": pdata, "odata": odata}
    return render(request,'user/home.html', md)

def aboutus(request):
    return render(request, 'user/aboutus.html')

def insta(request):
    return render(request,'user/insta.html')

def orderslist(request):
    oid=request.GET.get('get')
    user=request.session.get('user')
    pdata=myorders.objects.filter(userid=user,status="Pending")
    adata = myorders.objects.filter(userid=user, status="Accepted")
    ddata = myorders.objects.filter(userid=user, status="Delivered")
    if oid is not None:
        myorders.objects.filter(id=oid).delete()
        return HttpResponse("<script>alert(Your Order Has been Canceled...); location.href='/user/orderslist/'</script>")
    mydict={"pdata":pdata,"adata":adata,"ddata":ddata}
    return render(request,'user/orderslist.html',mydict)

def contactus(request):
    if request.method == "POST":
        a1 = request.POST.get('name')
        a2 = request.POST.get('email')
        a3 = request.POST.get('mobile')
        a4 = request.POST.get('message')
        contact(Name=a1,Email=a2,Mobile=a3,Message=a4).save()
        return HttpResponse("<script>alert('Thank you for contacting with us..');location.href='/user/contactus'</script>")
    return render(request, 'user/contactus.html')

def signin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        passwd = request.POST.get('passwd')
        x = register.objects.filter(email=email, passwd=passwd).count()
        if x == 1:
            y = register.objects.filter(email=email, passwd=passwd)
            request.session['user'] = email
            request.session['userpic'] = str(y[0].profile)
            request.session['username'] = str(y[0].name)
            user=request.session.get('user')
            cartitems=cart.objects.filter(userid=user).count()
            request.session['caritems'] = cartitems

            return HttpResponse("<script>alert('login successful..');location.href='/user/signin/'</script>")
        else:
            return HttpResponse("<script>alert('Your username or password is incorrect..');location.href='/user/signin/'</script>")

    return render(request, 'user/signin.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        passwd = request.POST.get('passwd')
        address = request.POST.get('address')
        pic = request.FILES['fu']
        x = register.objects.all().filter(email=email).count()
        if x==1:
            return HttpResponse("<script>alert('You are already registered...');location.href='/user/signup/'</script>")
        else:
            register(name=name, mobile=mobile, email=email, passwd=passwd, address=address, profile=pic).save()
            return HttpResponse("<script>alert('You are registered successfully...');location.href='/user/signup/'</script>")
    return render(request, 'user/signup.html')

def event(request):
    return render(request, 'user/event.html')

def profile(request):
    return render(request, 'user/profile.html')

def mproduct(request): #myproduct
    catid = request.GET.get('cid')
    subcatid = request.GET.get('sid')
    sdata = subcategory.objects.all().order_by('-id')
    if subcatid is not None:
        pdata = myproduct.objects.all().filter(subcategory_name=subcatid)
    elif catid is not None:
        pdata = myproduct.objects.all().filter(product_category=catid)
    else:
        pdata = myproduct.objects.all().order_by('-id')
    md = {"subcat": sdata, "pdata": pdata}
    return render(request, 'user/product.html', md)
def signout(request):
    if request.session.get('user'):
        del request.session['user']
        del request.session['userpic']
        return HttpResponse("<script>location.href='/user/home/'</script>")
    return render(request,'user/signout.html')

def myprofile(request):
    user = request.session.get('user')
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        passwd = request.POST.get('passwd')
        address = request.POST.get('address')
        register(name=name, email=user, mobile=mobile, passwd=passwd, address=address).save()
        return HttpResponse("<script>alert('Your Profile is updated successfully. .. ...');location.href='/user/myprofile/'</script>")
    rdata = ""
    if user:
        rdata = register.objects.filter(email=user)
    md = {"rdata": rdata}
    return render(request, 'user/myprofile.html',md)

def mycart(request):
    user=request.session.get('user')
    if user:
        qt=int(request.GET.get('qt'))#5
        pname=request.GET.get('pname')
        ppic=request.GET.get('ppic')
        pw=request.GET.get('pw')
        price=int(request.GET.get('price'))#50
        total_price=qt*price
        if qt>0:
            cart(userid=user,product_name=pname,quantity=qt,price=price,total_price=total_price,product_picture=ppic,pw=pw,added_date=datetime.now().date()).save()
            cartitems=cart.objects.filter(userid=user).count()
            request.session['cartitems']=cartitems
            return HttpResponse("<script>alert('Your item is added in Cart...');location.href='/user/product/'</script>")
        else:
            return HttpResponse("<script>alert('Please Increase Your Cartitems...');location.href='/user/product/'</script>")
    return render(request,'user/mycart.html')
def cartitems(request):
    user=request.session.get('user')
    cid=request.GET.get('cid')
    cartdata="";
    if user:
        cartdata=cart.objects.filter(userid=user)
        if cid is not None:
            cart.objects.filter(id=cid).delete()
            cartitems = cart.objects.filter(userid=user).count()
            request.session['cartitems'] = cartitems
            return HttpResponse("<script>alert('Your Cart items is removed successfully..');location.href='/user/cartitems/'</script>")
    md={"cartdata":cartdata}

    return render(request,'user/cartitems.html',md)

def morder(request):
    msg=request.GET.get('msg')
    user = request.session.get('user')
    if msg is not None:
        cursor=connection.cursor()
        cursor.execute("insert into user_myorders(product_name,price,total_price,quantity,pw,product_picture,userid,status,order_date) select product_name,price,total_price,quantity,pw,product_picture,'"+str(user)+"','Pending','"+str(datetime.now().date())+"' from user_cart where userid='"+str(user)+"'")
        cart.objects.filter(userid=user).delete()
        cartitems=cart.objects.filter(userid=user).count()
        request.session['cartitems']=cartitems
        return HttpResponse("<script>alert('Your order has been Placed Successfuly...');location.href='/user/orderslist';</script>")

    return render(request,'user/order.html')

def indexcart(request):
    user = request.session.get('user')
    if user:
        qt = int(request.GET.get('qt'))
        pname = request.GET.get('pname')
        ppic = request.GET.get('ppic')
        pw = request.GET.get('pw')

        if qt > 0:
            price = int(request.GET.get('price'))
            total_price = qt * price
            cart(userid=user, product_name=pname, quantity=qt, price=price, total_price=total_price,
                 product_picture=ppic, pw=pw, added_date=datetime.now().date()).save()
            cartitems = cart.objects.filter(userid=user).count()
            request.session['cartitems'] = cartitems
            return HttpResponse("<script>alert('Your item is added in Cart...');location.href='/user/home/'</script>")
        else:
            return HttpResponse("<script>alert('Please increase your cart items...');"
                                "location.href='/user/home/'</script>")

    return render(request,'user/indexcart.html')










