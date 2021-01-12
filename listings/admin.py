from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','realtor','list_date','price','is_published')
    list_display_links = ('id','title')
    list_filter = ('realtor','price')
    list_per_page = 25
    search_fields = ('title',)


admin.site.register(Listing,ListingAdmin)