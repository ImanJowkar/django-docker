from django.shortcuts import render, redirect
from .forms import CreateUserForm
from .models import Profile

# Create your views here.

def home(request):
    return render(request, 'todo/index.html')


def register(request):
    if request.method == 'GET':
        form = CreateUserForm()
        return render(request, 'todo/register.html', {'form': form})

    elif request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            current_user = form.save(commit=False)
            form.save()
            
            1
            profile = Profile.objects.create(user=current_user)
            
            return redirect('my-login')
        
        return render(request, 'todo/register.html', {'form':form})
            

def my_login(request):
    return render(request, 'todo/my_login.html')



def dashboard(request):
    return render(request, 'todo/dashboard.html')


def profile_management(request):
    return render(request, 'todo/profile_management.html')
