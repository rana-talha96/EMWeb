from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('add_battery/', views.add_battery_view, name='add_battery'),
    path('add_charger/', views.add_charger_view, name='add_charger'),
    path('add_inventory/', views.add_inventory_view.add_inventory, name='add_inventory'),
    path('AddCell/', views.add_inventory_view.AddCell, name='AddCell'),
    path('AddBMS/', views.add_inventory_view.AddBMS, name='AddBMS'),
    path('AddBattery/', views.add_inventory_view.AddBattery, name='AddBattery'),
    path('AddBike/', views.add_inventory_view.AddBike, name='AddBike'),
    path('AddBikeAccess/', views.add_inventory_view.AddBikeAccess, name='AddBikeAccess'),
    path('AddBatteryAccess/', views.add_inventory_view.AddBatteryAccess, name='AddBatteryAccess'),
    path('battery/', views.battery_view, name='battery'),
    path('charger/', views.charger_view, name='charger'),
    path('deletecharger/<int:id>', views.deletecharger_view, name='deletecharger'),
    path('inventory/', views.inventory_view, name='inventory'),
    path('deletecell/<int:id>', views.deleteinventory.deletecell_view, name='deletecell'),
    path('deletebms/<int:id>', views.deleteinventory.deletebms_view, name='deletebms'),
    path('deletebattery/<int:id>', views.deleteinventory.deletebattery_view, name='deletebattery'),
    path('deletebike/<int:id>', views.deleteinventory.deletebike_view, name='deletebike'),
    path('deletebatteryA/<int:id>', views.deleteinventory.deletebatteryA_view, name='deletebatteryA'),
    path('deletebikeA/<int:id>', views.deleteinventory.deletebikeA_view, name='deletebikeA'),
    path('store/', views.store_view, name='store'),
    path('device_data/', views.device_data_view, name='device_data'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register_view, name='register'),
    path('forgot-password/', views.forgotpassword_view, name='forgot-password'),
    path('warning/', views.warning_view, name='warning'),
    path('addcustomer/', views.addcustomer_view, name='addcustomer'),
    path('customer/', views.customer_view, name='customer'),
    path('customer/<int:id>/', views.customerprint_view, name='customer'),
    path('customerupdate/<int:id>/', views.customerupdate_view, name='customerupdate'),
    path('customerupdaterecord/<int:id>', views.customerupdaterecord, name='customerupdaterecord'),
    path('deletecustomer/<int:id>/', views.deleteinventory.deletecustomer_view, name='deletecustomer'),
    path('locations/', views.locations_view, name='locations'),
    path('battery/<int:btinfo_id>/', views.other_view, name='battery'),
    path('sale/<int:id>/', views.update_view, name='sale'),  #
    path('updaterecord/<int:id>', views.updaterecord, name='updaterecord'),  #
    path('updatecell/<int:id>/', views.updatecell_view, name='updatecell'),  #
    path('updatecellrecord/<int:id>', views.updatecellrecord, name='updatecellrecord'),  #
    path('updatebms/<int:id>/', views.updatebms_view, name='updatebms'),  #
    path('updatebmsrecord/<int:id>', views.updatebmsrecord, name='updatebmsrecord'),  #
    path('updatebattery/<int:id>/', views.updatebattery_view, name='updatebattery'),  #
    path('updatebatteryrecord/<int:id>', views.updatebatteryrecord, name='updatebatteryrecord'),  #
    path('updatebike/<int:id>/', views.updatebike_view, name='updatebike'),  #
    path('updatebikerecord/<int:id>', views.updatebikerecord, name='updatebikerecord'),  #
    path('updateBikeAccess/<int:id>/', views.updateBikeAccess_view, name='updateBikeAccess'),  #
    path('updateBikeAccessrecord/<int:id>', views.updateBikeAccess, name='updateBikeAccessrecord'),  #
    path('updateBatteryAccess/<int:id>/', views.updateBatteryAccess_view, name='updateBatteryAccess'),
    path('updateBatteryAccessrecord/<int:id>', views.updateBatteryAccess, name='updateBatteryAccessrecord'),
]