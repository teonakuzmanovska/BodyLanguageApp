from django.contrib import admin

# Register your models here.
from django.contrib.admin import display

from BodyLanguage.models import *


class MeaningAdmin(admin.ModelAdmin):
    list_display = ('meaning',)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(Meaning, MeaningAdmin)


class ContextAdmin(admin.ModelAdmin):
    list_display = ('context',)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(Context, ContextAdmin)


class BehaviourAdmin(admin.ModelAdmin):
    list_display = ('behaviour',)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(Behaviour, BehaviourAdmin)


class GestureAdmin(admin.ModelAdmin):
    list_display = ('gesture', 'category')
    list_filter = ('category', 'meaning', 'context', 'behaviour')

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(Gesture, GestureAdmin)
