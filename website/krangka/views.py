from turtle import title
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Item
from django.contrib.auth.decorators import login_required
import bcrypt

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'].encode('utf-8')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            # Hash password with bcrypt
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            user = User.objects.create_user(username=username)
            user.password = hashed_password.decode('utf-8')
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'].encode('utf-8')

        try:
            user = User.objects.get(username=username)
           
            if bcrypt.checkpw(password, user.password.encode('utf-8')):
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials')
        except User.DoesNotExist:
            messages.error(request, 'Invalid credentials')

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

@login_required
def add_item(request):
    user = request.user
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        price = request.POST["price"]

        if Item.objects.filter(name=name).exists():
            messages.error(request, "Item already exists")
        else:
            item = Item.objects.create(
                name=name, description=description, price=price, created_by=user
            )
            item.save()
            return redirect("home")
    return render(request, "add.html")

@login_required
def edit_item(request):
    items = Item.objects.filter(created_by=request.user)
    return render(request, "edit.html", {"items": items})

@login_required
def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id, created_by=request.user)
    if request.method == "POST":
        item.name = request.POST.get("name")
        item.description = request.POST.get("description")
        item.price = request.POST.get("price")
        item.save()
        return redirect("home")
    return render(request, "update.html", {"item": item})

@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, id=id, created_by=request.user)
    item.delete()
    return redirect("edit")
# Create your views here.
def login(request):
    context={
        "login":title
    }
    return render (request, 'login.html', context)

def home(request):
    context={
        "home":title
    }
    return render (request, 'home.html', context)

def ruangan(request):
    context={
        "ruangan":title
    }
    return render (request, 'ruangan.html', context)

def alat(request):
    context={
        "alat":title
    }
    return render (request, 'alat.html', context)

def paduan(request):
    context={
        "paduan":title
    }
    return render (request, 'paduan.html', context)

def borangkomputer(request):
    context={
        "borangkomputer":title
    }
    return render (request, 'borangkomputer.html', context)

def gor(request):
    context={
        "borang-gor-lapangan":title
    }
    return render (request, 'borang-gor-lapangan.html', context)

def labkimia(request):
    context={
        "borang-kimia":title
    }
    return render (request, 'borang-kimia.html', context)

def auditorium(request):
    context={
        "borang-auditorium":title
    }
    return render (request, 'borang-auditorium.html', context)

def laptop(request):
    context={
        "borang-laptop":title
    }
    return render (request, 'borang-laptop.html', context)

def kamera(request):
    context={
        "borang-kamera":title
    }
    return render (request, 'borang-kamera.html', context)

def drone(request):
    context={
        "borang-drone":title
    }
    return render (request, 'borang-drone.html', context)

def ipad(request):
    context={
        "borang-ipad":title
    }
    return render (request, 'borang-ipad.html', context)