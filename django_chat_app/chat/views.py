from django.shortcuts import render
from .models import Message, Chat

# Create your views here.
def index(request):
    chatMessages = None
    if request.method == 'POST':
        print("Reveived data " + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        author = request.user
        Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=author)
        chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessages})