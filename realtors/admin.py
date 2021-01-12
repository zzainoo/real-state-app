from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','photo','hire_date','is_mvp')
    list_display_links = ('id','name')
    list_filter = ('is_mvp',)
    list_per_page = 25
    search_fields = ('name',)


admin.site.register(Realtor,RealtorAdmin)