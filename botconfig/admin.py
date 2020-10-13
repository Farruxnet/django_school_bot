from django.contrib import admin
from . models import SiteConf

class SiteConfAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        if SiteConf.objects.all():
            return False
        else:
            return True

    list_display = ('email', 'tel', 'starttext', 'qoida', 'address', 'aboutschool')

admin.site.register(SiteConf, SiteConfAdmin)