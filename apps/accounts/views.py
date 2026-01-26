from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        selected_role = request.POST.get('role') 
        
        user = authenticate(username=u, password=p)
        
        if user:
            access_granted = False
            target_url = 'accounts:login' 
            
            if selected_role == 'student' and user.is_student:
                access_granted = True
                target_url = 'students:dashboard'
            elif selected_role == 'professor' and user.is_professor:
                access_granted = True
                target_url = 'professors:my_courses'
            elif selected_role == 'admin' and (user.is_staff or user.is_superuser):
                access_granted = True
                target_url = 'courses:manage_list' 
            
            if access_granted:
                login(request, user)
                return redirect(target_url)
            else:
                messages.error(request, f"شما دسترسی ورود به عنوان {selected_role} را ندارید.")
        else:
            messages.error(request, "نام کاربری یا رمز عبور اشتباه است.")
            
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')