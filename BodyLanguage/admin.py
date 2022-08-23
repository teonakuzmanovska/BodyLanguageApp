from django.contrib import admin

# Register your models here.
from BodyLanguage.models import *


class ReadInlineAdmin(admin.StackedInline):
    model = Read
    extra = 0


class BodyPartGestureAdmin(admin.ModelAdmin):
    inlines = [ReadInlineAdmin, ]

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(BodyPartGesture, BodyPartGestureAdmin)

class EmotionAdmin(admin.ModelAdmin):
    inlines = [ReadInlineAdmin, ]

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(Emotion, EmotionAdmin)


class ContextGestureAdmin(admin.ModelAdmin):
    inlines = [ReadInlineAdmin, ]

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(ContextGesture, ContextGestureAdmin)


class BehaviourAdmin(admin.ModelAdmin):
    inlines = [ReadInlineAdmin, ]

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(Behaviour, BehaviourAdmin)


class TestResultsAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(TestResults, TestResultsAdmin)


class StatisticsAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(Statistics, StatisticsAdmin)




