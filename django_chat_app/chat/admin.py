from django.contrib import admin
from .models import Message, Chat

class MessageAdmin(admin.ModelAdmin):
    fields = ('chat','text','createt_at', 'author', 'receiver')
    list_display = ('createt_at', 'author', 'text', 'receiver')
    search_fields = ('text',)

# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)