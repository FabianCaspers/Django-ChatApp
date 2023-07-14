from django.shortcuts import render
from .models import Message, Chat
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from datetime import datetime
from django.core import serializers
from django.http import JsonResponse




# Create your views here.
@login_required(login_url='/login/')
def index(request):
    chatMessages = None
    current_date = datetime.now()  
    if request.method == 'POST':
        print("Received data " + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        author = request.user
        new_message = Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=author)
        serialized_obj = serializers.serialize('json', [new_message, ])
        return JsonResponse(serialized_obj[1:-1], safe=False)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessages, 'current_date': current_date})



def login_view(request):
    redirect = request.GET.get('next')
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user: 
            login(request, user)
            return HttpResponseRedirect(request.POST.get('redirect'))
        else:
            return render(request, 'auth/login.html', {'wrongPassword': True, 'redirect': redirect})
    return render(request, 'auth/login.html', {'redirect': redirect})




@csrf_protect
def register_view(request):
    redirect_to_login = '/login/'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect_to_login)
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})



