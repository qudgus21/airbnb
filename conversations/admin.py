from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Conversations)
class ConversationAdmin(admin.ModelAdmin):
    pass
