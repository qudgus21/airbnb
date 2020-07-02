from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """ Message Admin Definition """

    list_display = ("__str__", "created")


@admin.register(models.Conversations)
class ConversationAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "count_messages",
        "count_participants",
    )
