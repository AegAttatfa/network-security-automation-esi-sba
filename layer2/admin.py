from django.contrib import admin

from .models import Device, Interface


class RuleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Device, RuleAdmin)
admin.site.register(Interface, RuleAdmin)
