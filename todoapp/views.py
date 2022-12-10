from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, "home.html")

def getitems(request):
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.user = request.user
            todo_item.save()
            messages.success(request, "ITEM ADDED SUCCESSFULLY")
        return redirect("index")
    todo = Item.objects.filter(user=request.user)
    context = {
        "items": todo,
        "form": form,
    }
    return render(request, "index.html", context)


def updateItem(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(instance=item)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {"form": form}
    return render(request, "edit.html", context)

 
def deleteItem(request, item_id):
    item_to_delete = Item.objects.get(pk=item_id)
    item_to_delete.delete()
    messages.error(request, "ITEM DELECTED")

    return redirect("index")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect("login")
    
    return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return redirect("home")



def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Rgistered Successfully, Please add new task items ")
            
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect("index")


    context = {
        "form": form,
    }
    return render(request, "register.html", context)