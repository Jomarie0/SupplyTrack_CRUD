from django.contrib.auth.models import User
from django.shortcuts import render

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})