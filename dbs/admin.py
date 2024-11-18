from django.contrib import admin

from dbs.models import Customer, Deposit

# Register your models here.
admin.site.site_header = 'dbs admin'

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','gender','email','dob']
    search_fields = ['first_name','last_name','email']
    list_filter = ['gender']
    list_per_page = 25
class DepositAdmin(admin.ModelAdmin):
    list_display = ['amount','status','created_at','customer']
    search_fields = ['amount','status','created_at']
    list_per_page = 25
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Deposit, DepositAdmin)
#pyton manage.py --help
