from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
from .forms import AddRecordForm


def home(request):
    records = Record.objects.all()
    context = { 'records': records }

    #check to see if logging in 
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        #authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Successfully Logged In')
            return redirect('home')
        else: 
            messages.success(request, 'Something Went Wrong')
            return redirect('home')

    else:
        return render(request, 'home.html', context)



def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Logged Out Successfully')
    return redirect('home')



def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You Have Successfully Registered')
            return redirect('home')
        else:
            # If the form is invalid, it will fall through to render the form again
            messages.error(request, 'Please correct the errors below.')  # Optionally add an error message

    else: 
        form = SignUpForm()
    context = {'form': form }
    return render(request, 'register.html', context)



def customer_record(request, id):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id= id)
        return render(request, 'record.html', { 'customer_record': customer_record })
    
    else:
        messages.success(request, 'You Must Be Logged In First')
        return redirect('home')


def delete_record(request, id):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id= id)
        delete_it.delete()
        messages.success(request, 'You Have Successfully Deleted The Record')
        return redirect('home')
    else:
        messages.success(request, 'You Must Be Logged In First')
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'You Have Added A Record Successfully')
                return redirect('home')
            else:
            # If the form is invalid, it will fall through to render the form again
                messages.error(request, 'Please correct the errors below.')  # Optionally add an error message
        return render(request, 'add_record.html', { 'form': form })
    else:
        messages.success(request, 'You Must Be Logged In First')
        return redirect('home')


def update_record(request, id):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id= id)
        form = AddRecordForm(request.POST or None, instance= current_record )
        if form.is_valid():
            form.save()
            messages.success(request, 'You Have Successfully Updated The Record')
            return redirect('home')
        return render(request, 'update_record.html', { 'form': form })
    else:
        messages.success(request, 'You Must Be Logged In First')
        return redirect('home')

