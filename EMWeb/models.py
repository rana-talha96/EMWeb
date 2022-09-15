import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class EMmodels(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title


class Btdetail(models.Model):
    id = models.IntegerField(primary_key=True)
    BatType = models.CharField(max_length=200, default=1)
    MaxVolt = models.FloatField()
    MinVolt = models.FloatField()
    MaxAmp = models.FloatField()
    MinAmp = models.FloatField()
    SCMaxVolt = models.FloatField()
    SCMinVolt = models.FloatField()
    Temp = models.FloatField()
    DatePur = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    Manf_ID = models.CharField(max_length=200)
    Latitude = models.CharField(max_length=200)
    Longitude = models.CharField(max_length=200)

    class Meta:
        db_table = "batdetail"

    def __str__(self):
        return self.BatType

    def was_published_recently(self):
        return self.DatePur >= timezone.now() - datetime.timedelta(days=1)


class CustomerDetail(models.Model):
    Ship_No = models.IntegerField(null=True, blank=True)
    Cell_Type = models.CharField(max_length=200, null=True, blank=True)
    Cell_qty = models.FloatField(null=True, blank=True)
    Cell_pup = models.FloatField(null=True, blank=True)
    Cell_price = models.FloatField(default=0, blank=True)
    Cell_Type1 = models.CharField(max_length=200, null=True, blank=True)
    Cell_qty1 = models.FloatField(null=True, blank=True)
    Cell_pup1 = models.FloatField(null=True, blank=True)
    Cell_price1 = models.FloatField(default=0, blank=True)
    Cell_Type2 = models.CharField(max_length=200, null=True, blank=True)
    Cell_qty2 = models.FloatField(null=True, blank=True)
    Cell_pup2 = models.FloatField(null=True, blank=True)
    Cell_price2 = models.FloatField(default=0, blank=True)
    Cell_Type3 = models.CharField(max_length=200, null=True, blank=True)
    Cell_qty3 = models.FloatField(null=True, blank=True)
    Cell_pup3 = models.FloatField(null=True, blank=True)
    Cell_price3 = models.FloatField(default=0, blank=True)
    Cell_Type4 = models.CharField(max_length=200, null=True, blank=True)
    Cell_qty4 = models.FloatField(null=True, blank=True)
    Cell_pup4 = models.FloatField(null=True, blank=True)
    Cell_price4 = models.FloatField(default=0, blank=True)
    BMS_Type = models.CharField(max_length=200, null=True, blank=True)
    BMSType = models.CharField(max_length=200, null=True, blank=True)
    BMS_qty = models.FloatField(null=True, blank=True)
    BMS_pup = models.FloatField(null=True, blank=True)
    BMS_price = models.FloatField(default=0, blank=True)
    BMS_Type1 = models.CharField(max_length=200, null=True, blank=True)
    BMSType1 = models.CharField(max_length=200, null=True, blank=True)
    BMS_qty1 = models.FloatField(null=True, blank=True)
    BMS_pup1 = models.FloatField(null=True, blank=True)
    BMS_price1 = models.FloatField(default=0, blank=True)
    BMS_Type2 = models.CharField(max_length=200, null=True, blank=True)
    BMSType2 = models.CharField(max_length=200, null=True, blank=True)
    BMS_qty2 = models.FloatField(null=True, blank=True)
    BMS_pup2 = models.FloatField(null=True, blank=True)
    BMS_price2 = models.FloatField(default=0, blank=True)
    Battery_pack = models.CharField(max_length=200, null=True, blank=True)
    Battery_pack_qty = models.FloatField(null=True, blank=True)
    Battery_pack_pup = models.FloatField(null=True, blank=True)
    Battery_pack_price = models.FloatField(default=0, blank=True)
    Bike_pack = models.CharField(max_length=200, null=True, blank=True)
    Bike_pack_qty = models.FloatField(null=True, blank=True)
    Bike_pack_pup = models.FloatField(null=True, blank=True)
    Bike_pack_price = models.FloatField(default=0, blank=True)
    motor_type = models.CharField(max_length=200, null=True, blank=True)
    motor_qty = models.FloatField(null=True, blank=True)
    motor_pup = models.FloatField(null=True, blank=True)
    motor_price = models.FloatField(default=0, blank=True)
    controller_type = models.CharField(max_length=200, null=True, blank=True)
    controller_qty = models.FloatField(null=True, blank=True)
    controller_pup = models.FloatField(null=True, blank=True)
    controller_price = models.FloatField(default=0, blank=True)
    throttle = models.FloatField(null=True, blank=True)
    throttle_pup = models.FloatField(null=True, blank=True)
    throttle_price = models.FloatField(default=0, blank=True)
    brake = models.FloatField(null=True, blank=True)
    brake_pup = models.FloatField(null=True, blank=True)
    brake_price = models.FloatField(default=0, blank=True)
    spokes = models.FloatField(null=True, blank=True)
    spokes_pup = models.FloatField(null=True, blank=True)
    spokes_price = models.FloatField(default=0, blank=True)
    enclosure = models.FloatField(null=True, blank=True)
    enclosure_pup = models.FloatField(null=True, blank=True)
    enclosure_price = models.FloatField(default=0, blank=True)
    breaker = models.FloatField(null=True, blank=True)
    breaker_pup = models.FloatField(null=True, blank=True)
    breaker_price = models.FloatField(default=0, blank=True)
    display = models.FloatField(null=True, blank=True)
    display_pup = models.FloatField(null=True, blank=True)
    display_price = models.FloatField(default=0, blank=True)
    B_Connector = models.FloatField(null=True, blank=True)
    B_Connector_pup = models.FloatField(null=True, blank=True)
    B_Connector_price = models.FloatField(default=0, blank=True)
    wire = models.FloatField(null=True, blank=True)
    wire_pup = models.FloatField(null=True, blank=True)
    wire_price = models.FloatField(default=0, blank=True)
    thimble = models.FloatField(null=True, blank=True)
    thimble_pup = models.FloatField(null=True, blank=True)
    thimble_price = models.FloatField(default=0, blank=True)
    customer_name = models.CharField(max_length=200, null=True, blank=True)
    customer_number = models.CharField(max_length=200, null=True, blank=True)
    customer_type = models.CharField(max_length=200, null=True, blank=True)
    customer_use = models.CharField(max_length=200, null=True, blank=True)
    customer_address = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(default=0, blank=True)
    otheramount = models.FloatField(null=True, blank=True)
    tax = models.FloatField(null=True, blank=True)
    taxprice = models.FloatField(default=0, blank=True)
    total = models.FloatField(default=0, blank=True)
    payment_type = models.CharField(max_length=200, null=True, blank=True)
    delivery_type = models.CharField(max_length=200, null=True, blank=True)
    Description = models.CharField(max_length=200, null=True, blank=True)
    DatePur = models.DateTimeField()
    date_update = models.DateTimeField(auto_now=True)
    User = models.CharField(max_length=200, null=True)

    def save(self, *args, **kwargs):
        self.Cell_price = float(self.Cell_qty or 0) * float(self.Cell_pup or 0)
        self.Cell_price1 = float(self.Cell_qty1 or 0) * float(self.Cell_pup1 or 0)
        self.Cell_price2 = float(self.Cell_qty2 or 0) * float(self.Cell_pup2 or 0)
        self.Cell_price3 = float(self.Cell_qty3 or 0) * float(self.Cell_pup3 or 0)
        self.Cell_price4 = float(self.Cell_qty4 or 0) * float(self.Cell_pup4 or 0)
        self.BMS_price = float(self.BMS_qty or 0) * float(self.BMS_pup or 0)
        self.BMS_price1 = float(self.BMS_qty1 or 0) * float(self.BMS_pup1 or 0)
        self.BMS_price2 = float(self.BMS_qty2 or 0) * float(self.BMS_pup2 or 0)
        self.Battery_pack_price = float(self.Battery_pack_qty or 0) * float(self.Battery_pack_pup or 0)
        self.Bike_pack_price = float(self.Bike_pack_qty or 0) * float(self.Bike_pack_pup or 0)
        self.motor_price = float(self.motor_qty or 0) * float(self.motor_pup or 0)
        self.controller_price = float(self.controller_qty or 0) * float(self.controller_pup or 0)
        self.throttle_price = float(self.throttle or 0) * float(self.throttle_pup or 0)
        self.brake_price = float(self.brake or 0) * float(self.brake_pup or 0)
        self.spokes_price = float(self.spokes or 0) * float(self.spokes_pup or 0)
        self.enclosure_price = float(self.enclosure or 0) * float(self.enclosure_pup or 0)
        self.breaker_price = float(self.breaker or 0) * float(self.breaker_pup or 0)
        self.display_price = float(self.display or 0) * float(self.display_pup or 0)
        self.B_Connector_price = float(self.B_Connector or 0) * float(self.B_Connector_pup or 0)
        self.wire_price = float(self.wire or 0) * float(self.wire_pup or 0)
        self.thimble_price = float(self.thimble or 0) * float(self.thimble_pup or 0)
        self.price = self.Cell_price + self.Cell_price1 + self.Cell_price2 + self.Cell_price3 + self.Cell_price4 + self.BMS_price +\
            self.BMS_price1 + self.BMS_price2 + self.Battery_pack_price + self.Bike_pack_price + self.motor_price + self.controller_price +\
            self.throttle_price + self.brake_price + self.spokes_price + self.enclosure_price + self.breaker_price + self.display_price +\
            self.B_Connector_price + self.wire_price + self.thimble_price
        self.taxprice = self.tax * self.price
        self.total = float(self.taxprice or 0) + self.price + float(self.otheramount or 0)
        super(CustomerDetail, self).save(*args, **kwargs)

    class Meta:
        db_table = "customer_detail"

    def __str__(self):
        return self.customer_name

    def was_published_recently(self):
        return self.DatePur >= timezone.now() - datetime.timedelta(days=1)


class Celldetail(models.Model):
    CellInvoiceNo = models.IntegerField(null=True, blank=True)
    Cell_Type = models.CharField(max_length=200, null=True)
    Cell_qty = models.FloatField(null=True)
    Cell_price = models.FloatField(null=True)
    Cell_PUP = models.FloatField(default=0)
    CellDescription = models.CharField(max_length=200, null=True, blank=True)
    DatePur = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    User = models.CharField(max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.Cell_PUP = self.Cell_price / self.Cell_qty
        super(Celldetail, self).save(*args, **kwargs)

    class Meta:
        db_table = "cell_detail"

    def was_published_recently(self):
        return self.DatePur >= timezone.now() - datetime.timedelta(days=1)


class BMSdetail(models.Model):
    BMSInvoiceNo = models.IntegerField(null=True, blank=True)
    BMS_Type = models.CharField(max_length=200, default=1, null=True)
    BMSType = models.CharField(max_length=200, null=True)
    BMS_qty = models.FloatField(null=True)
    BMS_price = models.FloatField(null=True)
    BMS_PUP = models.FloatField(default=0)
    BMSDescription = models.CharField(max_length=200, null=True, blank=True)
    DatePur = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    User = models.CharField(max_length=200, null=True)

    def save(self, *args, **kwargs):
        self.BMS_PUP = self.BMS_price / self.BMS_qty
        super(BMSdetail, self).save(*args, **kwargs)

    class Meta:
        db_table = "bms_detail"

    def was_published_recently(self):
        return self.DatePur >= timezone.now() - datetime.timedelta(days=1)


class BatteryPackdetail(models.Model):
    BatteryInvoiceNo = models.IntegerField(null=True, blank=True)
    Battery_pack = models.CharField(max_length=200, null=True)
    Battery_pack_qty = models.FloatField(null=True)
    Battery_pack_price = models.FloatField(default=0)
    Battery_pack_PUP = models.FloatField(default=0)
    BatteryDescription = models.CharField(max_length=200, null=True, blank=True)
    DatePur = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    User = models.CharField(max_length=200, null=True)

    def save(self, *args, **kwargs):
        self.Battery_pack_PUP = self.Battery_pack_price / self.Battery_pack_qty
        super(BatteryPackdetail, self).save(*args, **kwargs)

    class Meta:
        db_table = "battery_pack_detail"

    def was_published_recently(self):
        return self.DatePur >= timezone.now() - datetime.timedelta(days=1)


class BikePackdetail(models.Model):
    BikeInvoiceNo = models.IntegerField(null=True, blank=True)
    Bike_pack = models.CharField(max_length=200, null=True)
    Bike_pack_qty = models.FloatField(null=True)
    Bike_pack_price = models.FloatField(null=True)
    Bike_pack_PUP = models.FloatField(default=0)
    BikeDescription = models.CharField(max_length=200, null=True, blank=True)
    DatePur = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    User = models.CharField(max_length=200, null=True)

    def save(self, *args, **kwargs):
        self.Bike_pack_PUP = self.Bike_pack_price / self.Bike_pack_qty
        super(BikePackdetail, self).save(*args, **kwargs)

    class Meta:
        db_table = "bike_pack_detail"

    def was_published_recently(self):
        return self.DatePur >= timezone.now() - datetime.timedelta(days=1)


class BikeAccessorydetail(models.Model):
    Bike_InvoiceNo = models.IntegerField(null=True, blank=True)
    motor_type = models.CharField(max_length=200, null=True, blank=True)
    motor_qty = models.FloatField(default=0)
    motor_price = models.FloatField(default=0)
    motor_PUP = models.FloatField(default=0)
    controller_type = models.CharField(max_length=200, null=True, blank=True)
    controller_qty = models.FloatField(default=0)
    controller_price = models.FloatField(default=0)
    controller_PUP = models.FloatField(default=0)
    throttle = models.FloatField(default=0)
    throttle_price = models.FloatField(default=0)
    throttle_PUP = models.FloatField(default=0)
    brake = models.FloatField(default=0)
    brake_price = models.FloatField(default=0)
    brake_PUP = models.FloatField(default=0)
    spokes = models.FloatField(default=0)
    spokes_price = models.FloatField(default=0)
    spokes_PUP = models.FloatField(default=0)
    Bike_Description = models.CharField(max_length=200, null=True, blank=True)
    DatePur = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    User = models.CharField(max_length=200, null=True)

    def save(self, *args, **kwargs):
        if self.motor_qty:
            self.motor_PUP = self.motor_price / self.motor_qty
        if self.controller_qty:
            self.controller_PUP = self.controller_price / self.controller_qty
        if self.throttle:
            self.throttle_PUP = self.throttle_price / self.throttle
        if self.brake:
            self.brake_PUP = self.brake_price / self.brake
        if self.spokes:
            self.spokes_PUP = self.spokes_price / self.spokes
        super(BikeAccessorydetail, self).save(*args, **kwargs)

    class Meta:
        db_table = "bike_accessory_detail"

    def was_published_recently(self):
        return self.DatePur >= timezone.now() - datetime.timedelta(days=1)


class BatteryAccessorydetail(models.Model):
    Battery_InvoiceNo = models.IntegerField(null=True, blank=True)
    enclosure = models.FloatField(default=0)
    enclosure_price = models.FloatField(default=0)
    enclosure_PUP = models.FloatField(default=0)
    breaker = models.FloatField(default=0)
    breaker_price = models.FloatField(default=0)
    breaker_PUP = models.FloatField(default=0)
    display = models.FloatField(default=0)
    display_price = models.FloatField(default=0)
    display_PUP = models.FloatField(default=0)
    B_Connector = models.FloatField(default=0)
    B_Connector_price = models.FloatField(default=0)
    B_Connector_PUP = models.FloatField(default=0)
    wire = models.FloatField(default=0)
    wire_price = models.FloatField(default=0)
    wire_PUP = models.FloatField(default=0)
    thimble = models.FloatField(default=0)
    thimble_price = models.FloatField(default=0)
    thimble_PUP = models.FloatField(default=0)
    Battery_Description = models.CharField(max_length=200, null=True, blank=True)
    DatePur = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    User = models.CharField(max_length=200, null=True)

    def save(self, *args, **kwargs):
        if self.enclosure:
            self.enclosure_PUP = self.enclosure_price / self.enclosure
        if self.breaker:
            self.breaker_PUP = self.breaker_price / self.breaker
        if self.display:
            self.display_PUP = self.display_price / self.display
        if self.B_Connector:
            self.B_Connector_PUP = self.B_Connector_price / self.B_Connector
        if self.wire:
            self.wire_PUP = self.wire_price / self.wire
        if self.thimble:
            self.thimble_PUP = self.thimble_price / self.thimble
        super(BatteryAccessorydetail, self).save(*args, **kwargs)

    class Meta:
        db_table = "battery_accessory_detail"

    def was_published_recently(self):
        return self.DatePur >= timezone.now() - datetime.timedelta(days=1)
