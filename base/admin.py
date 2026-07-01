from django.contrib import admin
from .models import *

# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ['flight_company',
                    'flight_name',
                    'flight_no',
                    'from_city',
                    'to_city',
                    'depature_time',
                    'depature_date',
                    'price'
                    ]
    
    search_fields = ['flight_company']
  
admin.site.register(FlightModel,FlightAdmin)
