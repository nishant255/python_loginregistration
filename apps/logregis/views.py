from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

# ==============================================================================
#                                   Render
# ==============================================================================

# ---------------------------
#       Index Route
# ---------------------------

def index(request):
    if 'user_id' in request.session:
        return redirect('/success')

    return render(request, 'logregis/index.html')

# ---------------------------
#       Register
# ---------------------------

def register(request):
    if 'user_id' in request.session:
        return redirect('/success')
    return render(request, 'logregis/register.html')

# ---------------------------
#       Login_Success
# ---------------------------

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request, 'logregis/success.html')

# ==============================================================================
#                                   Process
# ==============================================================================

# ---------------------------
#       Registration
# ---------------------------

def registration(request):
    if 'user_id' in request.session:
        return redirect('/success')

    if request.method == 'POST':
        reg_data = User.objects.reg_validator(request.POST)
        if reg_data[0]:
            request.session['user_id'] = reg_data[1].id
            return redirect('/success')

        for error in reg_data[1]:
            messages.add_message(request, messages.INFO ,error)
    return redirect('/register')

# ---------------------------
#           Login
# ---------------------------

def login(request):
    if 'user_id' in request.session:
        return redirect('/success')

    if request.method == 'POST':
        login_data = User.objects.login_validate(request.POST)

        if login_data[0]:
            request.session['user_id'] = login_data[1].id
            return redirect('/success')

        for error in login_data[1]:
            messages.add_message(request, messages.INFO ,error)
    return redirect('/')

# ---------------------------
#           Logout
# ---------------------------

def logout(request):
    if 'user_id' in request.session:
        messages.add_message(request, messages.INFO ,"You're Successfully Logged Out")
    else:
        messages.add_message(request, messages.INFO ,"You're Already logged Out")
    request.session.flush()
    return redirect('/')

def changepass(arg):
    pass
