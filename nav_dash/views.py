from django.shortcuts import render,redirect
from django.contrib import admin
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout
from .forms import  CreateUserForm,pickerinput
from django.contrib import messages
from nav_dash.models import Post



def user_dashboard(request):
    # context={}
    # context['form']= pickerinput()

    return render(request, 'dashboard.html')


def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()    #when we save this form its gonna create that user
            username = form.cleaned_data.get('username')  # this allows us to get that username without getting any othr form attributes and at this point we have our flash msg that gets sent , we redirect to the login page.

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')


    context = {'form':form}
    return render(request, 'register.html', context)

def loginPage(request):
# #  # our login form sends our username and password ans postdata
# #
    if request.method == 'POST': # checking if the method is post or not.
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

 #once we authenticate it we first wanna check if tht user is actually there before we redirect him .

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request) # it handles logging the user out.
    return redirect('login')

# def picker(response):
#     if response.method == "POST":
#         form = Post(response.POST)
#         if form.is_valid:
#             form.save()
#         return redirect('dashboard')
#     else:
#         form = Post()
#     return render(response, 'dashboard.html', {'form' : form })

def post(self, request, *args, **kwargs):
    print("im in here now")
    
def picker(request):
    print("printing request messaghes: " + request.headers())
    if request.method == "POST":
        form = Post(request.POST)
        if form.is_valid:
            form.save()
        # return redirect('dashboard')
    # else:
        # form = Post()
    return render(request, 'dashboard.html', {'form' : form })