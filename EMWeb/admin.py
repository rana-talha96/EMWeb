from django.contrib import admin
from . models import Btdetail, CustomerDetail, BMSdetail, Celldetail, BatteryPackdetail,BikePackdetail, BikeAccessorydetail, BatteryAccessorydetail

# Register your models here.
admin.site.register(Btdetail)
admin.site.register(CustomerDetail)
admin.site.register(BMSdetail)
admin.site.register(Celldetail)
admin.site.register(BatteryPackdetail)
admin.site.register(BikePackdetail)
admin.site.register(BikeAccessorydetail)
admin.site.register(BatteryAccessorydetail)
