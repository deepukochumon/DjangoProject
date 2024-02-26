# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token
from django.views.decorators.cache import never_cache
from .models import students
from .forms import insert_Form

@never_cache
@ensure_csrf_cookie
def login_view(request):
    if request.method == 'POST':
        csrf_token=get_token(request)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        
        if user_type == 'faculty':
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('faculty_home')
        elif user_type == 'student':
            user = authenticate(request, username=username, password=password)
            if user is not None and not user.is_staff:
                login(request, user)
                redirect_url=f'/home/?variable={username}'
                return redirect(redirect_url)
            # Return an 'invalid login' error message.
        
        error_message = 'Invalid username or password.'
        return render(request, 'login.html', {'error_message': error_message})

        
    else:
        return render(request, 'login.html')
    
def home_view(request):
    try:
        username=request.GET.get('variable')
        student_data=students.objects.get(name=username)
        return render(request,'student.html',{'student_data':student_data})
    except students.DoesNotExist:
        # Handle the case when the student with the given username is not found
        return redirect('login')

def fhome_view(request):
    return render(request,'faculty.html')

def authlogout(request):
    return redirect('login')

def insert_data(request):
    if request.method == 'POST':
        frm=insert_Form(request.POST)
        if frm.is_valid():
            frm.save()
    frm=insert_Form()
    return render(request,'create.html',{'frm':frm})