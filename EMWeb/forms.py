from django import forms
from .models import Btdetail, CustomerDetail, BMSdetail, Celldetail, BatteryPackdetail, BikePackdetail, BikeAccessorydetail, BatteryAccessorydetail


class EMDataForm(forms.ModelForm):
    class Meta:
        model = Btdetail
        fields = [
            # 'id',
            'BatType',
            'MaxVolt',
            'MinVolt',
            'MaxAmp',
            'MinAmp',
            'SCMaxVolt',
            'SCMinVolt',
            'Temp',
            'Manf_ID',
            'Latitude',
            'Longitude',
        ]


Battery_Type = (
    "Lithium Batteries",
    "Alkaline Batteries",
    "Carbon Zinc Batteries",
    "Silver Oxide Batteries",
    "Zinc Air Batteries",
)


class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerDetail
        fields = [
            'Ship_No',
            'Cell_Type',
            'Cell_qty',
            'Cell_pup',
            'Cell_price',
            'Cell_Type1',
            'Cell_qty1',
            'Cell_pup1',
            'Cell_price1',
            'Cell_Type2',
            'Cell_qty2',
            'Cell_pup2',
            'Cell_price2',
            'Cell_Type3',
            'Cell_qty3',
            'Cell_pup3',
            'Cell_price3',
            'Cell_Type4',
            'Cell_qty4',
            'Cell_pup4',
            'Cell_price4',
            'BMS_Type',
            'BMSType',
            'BMS_qty',
            'BMS_pup',
            'BMS_price',
            'BMS_Type1',
            'BMSType1',
            'BMS_qty1',
            'BMS_pup1',
            'BMS_price1',
            'BMS_Type2',
            'BMSType2',
            'BMS_qty2',
            'BMS_pup2',
            'BMS_price2',
            'Battery_pack',
            'Battery_pack_qty',
            'Battery_pack_pup',
            'Battery_pack_price',
            'Bike_pack',
            'Bike_pack_qty',
            'Bike_pack_pup',
            'Bike_pack_price',
            'motor_type',
            'motor_qty',
            'motor_pup',
            'motor_price',
            'controller_type',
            'controller_qty',
            'controller_pup',
            'controller_price',
            'throttle',
            'throttle_pup',
            'throttle_price',
            'brake',
            'brake_pup',
            'brake_price',
            'spokes',
            'spokes_pup',
            'spokes_price',
            'enclosure',
            'enclosure_pup',
            'enclosure_price',
            'breaker',
            'breaker_pup',
            'breaker_price',
            'display',
            'display_pup',
            'display_price',
            'B_Connector',
            'B_Connector_pup',
            'B_Connector_price',
            'wire',
            'wire_pup',
            'wire_price',
            'thimble',
            'thimble_pup',
            'thimble_price',
            'customer_name',
            'customer_number',
            'customer_type',
            'customer_use',
            'customer_address',
            'price',
            'otheramount',
            'tax',
            # 'taxprice',
            # 'total',
            'payment_type',
            'delivery_type',
            'Description',
            'DatePur',
            'User',
        ]

class CellForm(forms.ModelForm):
    class Meta:
        model = Celldetail
        fields = [
            'CellInvoiceNo',
            'Cell_Type',
            'Cell_qty',
            'Cell_price',
            'CellDescription',
            'User',
        ]


class BMSForm(forms.ModelForm):
    class Meta:
        model = BMSdetail
        fields = [
            'BMSInvoiceNo',
            'BMS_Type',
            'BMSType',
            'BMS_qty',
            'BMS_price',
            'BMSDescription',
            'User',
        ]


class BatteryPackForm(forms.ModelForm):
    class Meta:
        model = BatteryPackdetail
        fields = [
            'BatteryInvoiceNo',
            'Battery_pack',
            'Battery_pack_qty',
            'Battery_pack_price',
            'BatteryDescription',
            'User',
        ]


class BikePackForm(forms.ModelForm):
    class Meta:
        model = BikePackdetail
        fields = [
            'BikeInvoiceNo',
            'Bike_pack',
            'Bike_pack_qty',
            'Bike_pack_price',
            'BikeDescription',
            'User',
        ]


class BatteryAccessoryForm(forms.ModelForm):
    class Meta:
        model = BatteryAccessorydetail
        fields = [
            'enclosure',
            'enclosure_price',
            'breaker',
            'breaker_price',
            'display',
            'display_price',
            'B_Connector',
            'B_Connector_price',
            'wire',
            'wire_price',
            'thimble',
            'thimble_price',
            'Battery_InvoiceNo',
            'Battery_Description',
            'User',
        ]


class BikeAccessoryForm(forms.ModelForm):
    class Meta:
        model = BikeAccessorydetail
        fields = [
            'motor_type',
            'motor_qty',
            'motor_price',
            'controller_type',
            'controller_qty',
            'controller_price',
            'throttle',
            'throttle_price',
            'brake',
            'brake_price',
            'spokes',
            'spokes_price',
            'Bike_InvoiceNo',
            'Bike_Description',
            'User',
        ]



BMS_Type = (
    'BMS Type',
    "LifoPO4 4S 20A",
    "LifoPO4 4S 50A",
    "LifoPO4 4S 100A",
    "LifoPO4 4S 200A",
    "LifoPO4 8S 50A",
    "LifoPO4 8S 100A",
    "LifoPO4 8S 200A",
    "LifoPO4 15S 50A",
    "LifoPO4 15S 100A",
    "LifoPO4 15S 200A",
    "LifoPO4 16S 50A",
    "LifoPO4 16S 100A",
    "LifoPO4 16S 200A",
    "LifoPO4 19S 60A",
    "LifoPO4 19S 100A",
    "LifoPO4 20S 60A",
    "LifoPO4 20S 100A",
    "LifoPO4 23S 50A",
    "LifoPO4 23S 100A",
    "LifoPO4 24S 50A",
    "LifoPO4 24S 100A",
)

Cell_Type = (
    'Cell Type',
    "LifoPO4 6Ah",
    "LifoPO4 20Ah",
    "LifoPO4 25Ah",
    "LifoPO4 40Ah",
    "LifoPO4 50Ah",
    "LifoPO4 105Ah",
    "LifoPO4 205Ah",
)

Battery_pack = (
    'Battery Type',
    "12V 25Ah",
    "12V 40Ah",
    "12V 50Ah",
    "12V 100Ah",
    "12V 200Ah",
    "24V 50Ah",
    "24V 100Ah",
    "24V 200Ah",
    "48V 25Ah",
    "48V 40Ah",
    "48V 50Ah",
    "48V 100Ah",
    "48V 200Ah",
    "60V 25Ah",
    "60V 40Ah",
    "60V 50Ah",
    "60V 100Ah",
    "72V 25Ah",
    "72V 40Ah",
    "72V 50Ah",
    "72V 100Ah",
    "72V 200Ah",
)

motor_type = (
    'Motor Type',
    'Motor 1',
    'Motor 2',
    'Motor 3',
    'Motor 4',
)

controller_type = (
    'Controller Type',
    'Controller 1',
    'Controller 2',
    'Controller 3',
    'Controller 4',
)

Bike_pack = (
    'Bike Pack',
    'Bike 1',
    'Bike 2',
    'Bike 3',
    'Bike 4',
)

payment_type = (
    'Payment Method',
    'Cash',
    'Bank Transfer',
    'Easypesa',
    'Jazzcash',
)
