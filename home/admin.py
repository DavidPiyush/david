from django.contrib import admin
from .models import Contact 
from django.db.models import Count






# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('sno','name','phone','email')
    ordering = ('name',)
    search_fields = ('email','name',)

    def order_count(self, obj):
        return obj._sno

    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _order_count=Count("name", distinct=True),
        )
        return queryset
	
admin.site.register(Contact,ContactAdmin) 