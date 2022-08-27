from django.contrib import admin

# Register your models here.
from django.contrib.admin import display

from BodyLanguage.models import *


# class MeaningGestureAdmin(admin.StackedInline):
#     model = MeaningGesture
#     extra = 0


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


class BodyPartGestureAdmin(admin.ModelAdmin):
    list_display = ('gesture', 'category')
    # inlines = [MeaningGestureAdmin, ]
    list_filter = ('category', )

    # @display(ordering='meaning__meaning', description='Meaning')
    # def get_meaning(self, obj):
    #     return obj.meaning.meaning

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


admin.site.register(BodyPartGesture, BodyPartGestureAdmin)


class ContextGestureAdmin(admin.ModelAdmin):

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


admin.site.register(ContextGesture, ContextGestureAdmin)


class BehaviourAdmin(admin.ModelAdmin):

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




