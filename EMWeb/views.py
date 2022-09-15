from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Avg, Count, Min, Sum
from django.template import loader
from django.urls import reverse
from django.utils.safestring import mark_safe
from .forms import EMDataForm, Battery_Type, CustomerForm, BMS_Type, Cell_Type, Battery_pack, motor_type, \
    controller_type, Bike_pack, BMSForm, CellForm, BatteryPackForm, BikePackForm, BikeAccessoryForm, \
    BatteryAccessoryForm, payment_type
from .models import Btdetail, CustomerDetail, Celldetail, BMSdetail, BatteryPackdetail, BikePackdetail, \
    BatteryAccessorydetail, BikeAccessorydetail
from django.contrib.auth.models import User
from datetime import datetime
from dateutil.relativedelta import relativedelta
import serial.tools.list_ports
import serial
import time

ports = serial.tools.list_ports.comports(include_links=False)
batt = Btdetail.objects.all()
btinfo = Btdetail.objects.order_by('-date_update')
T_Chargers = Btdetail.objects.all().count()


def index_view(request, x=0, y=0):
    now = datetime.now()
    month6 = now - relativedelta(months=5)
    modified6 = month6.replace(day=1)
    month5 = now - relativedelta(months=4)
    modified5 = month5.replace(day=1)
    month4 = now - relativedelta(months=3)
    modified4 = month4.replace(day=1)
    month3 = now - relativedelta(months=2)
    modified3 = month3.replace(day=1)
    month2 = now - relativedelta(months=1)
    modified2 = month2.replace(day=1)
    month1 = now - relativedelta(months=0)
    modified1 = month1.replace(day=1)
    mon6 = Btdetail.objects.filter(DatePur__range=[modified6, modified5]).count()
    mon5 = Btdetail.objects.filter(DatePur__range=[modified5, modified4]).count()
    mon4 = Btdetail.objects.filter(DatePur__range=[modified4, modified3]).count()
    mon3 = Btdetail.objects.filter(DatePur__range=[modified3, modified2]).count()
    mon2 = Btdetail.objects.filter(DatePur__range=[modified2, modified1]).count()
    mon1 = Btdetail.objects.filter(DatePur__range=[modified1, now]).count()

    mon6cell = Celldetail.objects.filter(DatePur__range=[modified6, modified5]).aggregate(Sum('Cell_price')).get(
        'Cell_price__sum')
    mon6bms = BMSdetail.objects.filter(DatePur__range=[modified6, modified5]).aggregate(Sum('BMS_price')).get(
        'BMS_price__sum')
    mon6battery = BatteryPackdetail.objects.filter(DatePur__range=[modified6, modified5]).aggregate(
        Sum('Battery_pack_price')).get('Battery_pack_price__sum')
    mon6bike = BikePackdetail.objects.filter(DatePur__range=[modified6, modified5]).aggregate(
        Sum('Bike_pack_price')).get('Bike_pack_price__sum')
    mon6motor = BikeAccessorydetail.objects.filter(DatePur__range=[modified6, modified5]).aggregate(
        Sum('motor_price')).get('motor_price__sum')
    mon6controller = BikeAccessorydetail.objects.filter(DatePur__range=[modified6, modified5]).aggregate(
        Sum('controller_price')).get('controller_price__sum')
    mon6throttle = BikeAccessorydetail.objects.filter(DatePur__range=[modified6, modified5]).aggregate(
        Sum('throttle_price')).get('throttle_price__sum')
    mon6brake = BikeAccessorydetail.objects.filter(DatePur__range=[modified6, modified5]).aggregate(
        Sum('brake_price')).get('brake_price__sum')
    mon6spokes = BikeAccessorydetail.objects.filter(DatePur__range=[modified6, modified5]).aggregate(
        Sum('spokes_price')).get('spokes_price__sum')
    mon6enclosure = BatteryAccessorydetail.objects.filter(DatePur__range=[modified6, modified5]).aggregate(
        Sum('enclosure_price')).get('enclosure_price__sum')
    mon6breaker = BatteryAccessorydetail.objects.filter(DatePur__range=[modified6, modified5]).aggregate(
        Sum('breaker_price')).get('breaker_price__sum')
    mon6display = BatteryAccessorydetail.objects.filter(DatePur__range=[modified6, modified5]).aggregate(
        Sum('display_price')).get('display_price__sum')
    mon6connector = BatteryAccessorydetail.objects.filter(DatePur__range=[modified6, modified5]).aggregate(
        Sum('B_Connector_price')).get('B_Connector_price__sum')
    mon6wire = BatteryAccessorydetail.objects.filter(DatePur__range=[modified6, modified5]).aggregate(
        Sum('wire_price')).get('wire_price__sum')
    mon6thimble = BatteryAccessorydetail.objects.filter(DatePur__range=[modified6, modified5]).aggregate(
        Sum('thimble_price')).get('thimble_price__sum')
    mon5cell = Celldetail.objects.filter(DatePur__range=[modified5, modified4]).aggregate(Sum('Cell_price')).get(
        'Cell_price__sum')
    mon5bms = BMSdetail.objects.filter(DatePur__range=[modified5, modified4]).aggregate(Sum('BMS_price')).get(
        'BMS_price__sum')
    mon5battery = BatteryPackdetail.objects.filter(DatePur__range=[modified5, modified4]).aggregate(
        Sum('Battery_pack_price')).get('Battery_pack_price__sum')
    mon5bike = BikePackdetail.objects.filter(DatePur__range=[modified5, modified4]).aggregate(
        Sum('Bike_pack_price')).get('Bike_pack_price__sum')
    mon5motor = BikeAccessorydetail.objects.filter(DatePur__range=[modified5, modified4]).aggregate(
        Sum('motor_price')).get('motor_price__sum')
    mon5controller = BikeAccessorydetail.objects.filter(DatePur__range=[modified5, modified4]).aggregate(
        Sum('controller_price')).get('controller_price__sum')
    mon5throttle = BikeAccessorydetail.objects.filter(DatePur__range=[modified5, modified4]).aggregate(
        Sum('throttle_price')).get('throttle_price__sum')
    mon5brake = BikeAccessorydetail.objects.filter(DatePur__range=[modified5, modified4]).aggregate(
        Sum('brake_price')).get('brake_price__sum')
    mon5spokes = BikeAccessorydetail.objects.filter(DatePur__range=[modified5, modified4]).aggregate(
        Sum('spokes_price')).get('spokes_price__sum')
    mon5enclosure = BatteryAccessorydetail.objects.filter(DatePur__range=[modified5, modified4]).aggregate(
        Sum('enclosure_price')).get('enclosure_price__sum')
    mon5breaker = BatteryAccessorydetail.objects.filter(DatePur__range=[modified5, modified4]).aggregate(
        Sum('breaker_price')).get('breaker_price__sum')
    mon5display = BatteryAccessorydetail.objects.filter(DatePur__range=[modified5, modified4]).aggregate(
        Sum('display_price')).get('display_price__sum')
    mon5connector = BatteryAccessorydetail.objects.filter(DatePur__range=[modified5, modified4]).aggregate(
        Sum('B_Connector_price')).get('B_Connector_price__sum')
    mon5wire = BatteryAccessorydetail.objects.filter(DatePur__range=[modified5, modified4]).aggregate(
        Sum('wire_price')).get('wire_price__sum')
    mon5thimble = BatteryAccessorydetail.objects.filter(DatePur__range=[modified5, modified4]).aggregate(
        Sum('thimble_price')).get('thimble_price__sum')
    mon4cell = Celldetail.objects.filter(DatePur__range=[modified4, modified3]).aggregate(Sum('Cell_price')).get(
        'Cell_price__sum')
    mon4bms = BMSdetail.objects.filter(DatePur__range=[modified4, modified3]).aggregate(Sum('BMS_price')).get(
        'BMS_price__sum')
    mon4battery = BatteryPackdetail.objects.filter(DatePur__range=[modified4, modified3]).aggregate(
        Sum('Battery_pack_price')).get('Battery_pack_price__sum')
    mon4bike = BikePackdetail.objects.filter(DatePur__range=[modified4, modified3]).aggregate(
        Sum('Bike_pack_price')).get('Bike_pack_price__sum')
    mon4motor = BikeAccessorydetail.objects.filter(DatePur__range=[modified4, modified3]).aggregate(
        Sum('motor_price')).get('motor_price__sum')
    mon4controller = BikeAccessorydetail.objects.filter(DatePur__range=[modified4, modified3]).aggregate(
        Sum('controller_price')).get('controller_price__sum')
    mon4throttle = BikeAccessorydetail.objects.filter(DatePur__range=[modified4, modified3]).aggregate(
        Sum('throttle_price')).get('throttle_price__sum')
    mon4brake = BikeAccessorydetail.objects.filter(DatePur__range=[modified4, modified3]).aggregate(
        Sum('brake_price')).get('brake_price__sum')
    mon4spokes = BikeAccessorydetail.objects.filter(DatePur__range=[modified4, modified3]).aggregate(
        Sum('spokes_price')).get('spokes_price__sum')
    mon4enclosure = BatteryAccessorydetail.objects.filter(DatePur__range=[modified4, modified3]).aggregate(
        Sum('enclosure_price')).get('enclosure_price__sum')
    mon4breaker = BatteryAccessorydetail.objects.filter(DatePur__range=[modified4, modified3]).aggregate(
        Sum('breaker_price')).get('breaker_price__sum')
    mon4display = BatteryAccessorydetail.objects.filter(DatePur__range=[modified4, modified3]).aggregate(
        Sum('display_price')).get('display_price__sum')
    mon4connector = BatteryAccessorydetail.objects.filter(DatePur__range=[modified4, modified3]).aggregate(
        Sum('B_Connector_price')).get('B_Connector_price__sum')
    mon4wire = BatteryAccessorydetail.objects.filter(DatePur__range=[modified4, modified3]).aggregate(
        Sum('wire_price')).get('wire_price__sum')
    mon4thimble = BatteryAccessorydetail.objects.filter(DatePur__range=[modified4, modified3]).aggregate(
        Sum('thimble_price')).get('thimble_price__sum')
    mon3cell = Celldetail.objects.filter(DatePur__range=[modified3, modified2]).aggregate(Sum('Cell_price')).get(
        'Cell_price__sum')
    mon3bms = BMSdetail.objects.filter(DatePur__range=[modified3, modified2]).aggregate(Sum('BMS_price')).get(
        'BMS_price__sum')
    mon3battery = BatteryPackdetail.objects.filter(DatePur__range=[modified3, modified2]).aggregate(
        Sum('Battery_pack_price')).get('Battery_pack_price__sum')
    mon3bike = BikePackdetail.objects.filter(DatePur__range=[modified3, modified2]).aggregate(
        Sum('Bike_pack_price')).get('Bike_pack_price__sum')
    mon3motor = BikeAccessorydetail.objects.filter(DatePur__range=[modified3, modified2]).aggregate(
        Sum('motor_price')).get('motor_price__sum')
    mon3controller = BikeAccessorydetail.objects.filter(DatePur__range=[modified3, modified2]).aggregate(
        Sum('controller_price')).get('controller_price__sum')
    mon3throttle = BikeAccessorydetail.objects.filter(DatePur__range=[modified3, modified2]).aggregate(
        Sum('throttle_price')).get('throttle_price__sum')
    mon3brake = BikeAccessorydetail.objects.filter(DatePur__range=[modified3, modified2]).aggregate(
        Sum('brake_price')).get('brake_price__sum')
    mon3spokes = BikeAccessorydetail.objects.filter(DatePur__range=[modified3, modified2]).aggregate(
        Sum('spokes_price')).get('spokes_price__sum')
    mon3enclosure = BatteryAccessorydetail.objects.filter(DatePur__range=[modified3, modified2]).aggregate(
        Sum('enclosure_price')).get('enclosure_price__sum')
    mon3breaker = BatteryAccessorydetail.objects.filter(DatePur__range=[modified3, modified2]).aggregate(
        Sum('breaker_price')).get('breaker_price__sum')
    mon3display = BatteryAccessorydetail.objects.filter(DatePur__range=[modified3, modified2]).aggregate(
        Sum('display_price')).get('display_price__sum')
    mon3connector = BatteryAccessorydetail.objects.filter(DatePur__range=[modified3, modified2]).aggregate(
        Sum('B_Connector_price')).get('B_Connector_price__sum')
    mon3wire = BatteryAccessorydetail.objects.filter(DatePur__range=[modified3, modified2]).aggregate(
        Sum('wire_price')).get('wire_price__sum')
    mon3thimble = BatteryAccessorydetail.objects.filter(DatePur__range=[modified3, modified2]).aggregate(
        Sum('thimble_price')).get('thimble_price__sum')
    mon2cell = Celldetail.objects.filter(DatePur__range=[modified2, modified1]).aggregate(Sum('Cell_price')).get(
        'Cell_price__sum')
    mon2bms = BMSdetail.objects.filter(DatePur__range=[modified2, modified1]).aggregate(Sum('BMS_price')).get(
        'BMS_price__sum')
    mon2battery = BatteryPackdetail.objects.filter(DatePur__range=[modified2, modified1]).aggregate(
        Sum('Battery_pack_price')).get('Battery_pack_price__sum')
    mon2bike = BikePackdetail.objects.filter(DatePur__range=[modified2, modified1]).aggregate(
        Sum('Bike_pack_price')).get('Bike_pack_price__sum')
    mon2motor = BikeAccessorydetail.objects.filter(DatePur__range=[modified2, modified1]).aggregate(
        Sum('motor_price')).get('motor_price__sum')
    mon2controller = BikeAccessorydetail.objects.filter(DatePur__range=[modified2, modified1]).aggregate(
        Sum('controller_price')).get('controller_price__sum')
    mon2throttle = BikeAccessorydetail.objects.filter(DatePur__range=[modified2, modified1]).aggregate(
        Sum('throttle_price')).get('throttle_price__sum')
    mon2brake = BikeAccessorydetail.objects.filter(DatePur__range=[modified2, modified1]).aggregate(
        Sum('brake_price')).get('brake_price__sum')
    mon2spokes = BikeAccessorydetail.objects.filter(DatePur__range=[modified2, modified1]).aggregate(
        Sum('spokes_price')).get('spokes_price__sum')
    mon2enclosure = BatteryAccessorydetail.objects.filter(DatePur__range=[modified2, modified1]).aggregate(
        Sum('enclosure_price')).get('enclosure_price__sum')
    mon2breaker = BatteryAccessorydetail.objects.filter(DatePur__range=[modified2, modified1]).aggregate(
        Sum('breaker_price')).get('breaker_price__sum')
    mon2display = BatteryAccessorydetail.objects.filter(DatePur__range=[modified2, modified1]).aggregate(
        Sum('display_price')).get('display_price__sum')
    mon2connector = BatteryAccessorydetail.objects.filter(DatePur__range=[modified2, modified1]).aggregate(
        Sum('B_Connector_price')).get('B_Connector_price__sum')
    mon2wire = BatteryAccessorydetail.objects.filter(DatePur__range=[modified2, modified1]).aggregate(
        Sum('wire_price')).get('wire_price__sum')
    mon2thimble = BatteryAccessorydetail.objects.filter(DatePur__range=[modified2, modified1]).aggregate(
        Sum('thimble_price')).get('thimble_price__sum')
    mon1cell = Celldetail.objects.filter(DatePur__range=[modified1, now]).aggregate(Sum('Cell_price')).get(
        'Cell_price__sum')
    mon1bms = BMSdetail.objects.filter(DatePur__range=[modified1, now]).aggregate(Sum('BMS_price')).get(
        'BMS_price__sum')
    mon1battery = BatteryPackdetail.objects.filter(DatePur__range=[modified1, now]).aggregate(
        Sum('Battery_pack_price')).get('Battery_pack_price__sum')
    mon1bike = BikePackdetail.objects.filter(DatePur__range=[modified1, now]).aggregate(Sum('Bike_pack_price')).get(
        'Bike_pack_price__sum')
    mon1motor = BikeAccessorydetail.objects.filter(DatePur__range=[modified1, now]).aggregate(Sum('motor_price')).get(
        'motor_price__sum')
    mon1controller = BikeAccessorydetail.objects.filter(DatePur__range=[modified1, now]).aggregate(
        Sum('controller_price')).get('controller_price__sum')
    mon1throttle = BikeAccessorydetail.objects.filter(DatePur__range=[modified1, now]).aggregate(
        Sum('throttle_price')).get('throttle_price__sum')
    mon1brake = BikeAccessorydetail.objects.filter(DatePur__range=[modified1, now]).aggregate(Sum('brake_price')).get(
        'brake_price__sum')
    mon1spokes = BikeAccessorydetail.objects.filter(DatePur__range=[modified1, now]).aggregate(Sum('spokes_price')).get(
        'spokes_price__sum')
    mon1enclosure = BatteryAccessorydetail.objects.filter(DatePur__range=[modified1, now]).aggregate(
        Sum('enclosure_price')).get('enclosure_price__sum')
    mon1breaker = BatteryAccessorydetail.objects.filter(DatePur__range=[modified1, now]).aggregate(
        Sum('breaker_price')).get('breaker_price__sum')
    mon1display = BatteryAccessorydetail.objects.filter(DatePur__range=[modified1, now]).aggregate(
        Sum('display_price')).get('display_price__sum')
    mon1connector = BatteryAccessorydetail.objects.filter(DatePur__range=[modified1, now]).aggregate(
        Sum('B_Connector_price')).get('B_Connector_price__sum')
    mon1wire = BatteryAccessorydetail.objects.filter(DatePur__range=[modified1, now]).aggregate(Sum('wire_price')).get(
        'wire_price__sum')
    mon1thimble = BatteryAccessorydetail.objects.filter(DatePur__range=[modified1, now]).aggregate(
        Sum('thimble_price')).get('thimble_price__sum')

    mon6sale = CustomerDetail.objects.filter(DatePur__range=[modified6, modified5]).aggregate(Sum('total')).get(
        'total__sum')
    mon5sale = CustomerDetail.objects.filter(DatePur__range=[modified5, modified4]).aggregate(Sum('total')).get(
        'total__sum')
    mon4sale = CustomerDetail.objects.filter(DatePur__range=[modified4, modified3]).aggregate(Sum('total')).get(
        'total__sum')
    mon3sale = CustomerDetail.objects.filter(DatePur__range=[modified3, modified2]).aggregate(Sum('total')).get(
        'total__sum')
    mon2sale = CustomerDetail.objects.filter(DatePur__range=[modified2, modified1]).aggregate(Sum('total')).get(
        'total__sum')
    mon1sale = CustomerDetail.objects.filter(DatePur__range=[modified1, now]).aggregate(Sum('total')).get('total__sum')

    mon6purchase = float(mon6cell or 0) + float(mon6bms or 0) + float(mon6battery or 0) + float(mon6bike or 0) + float(
        mon6motor or 0) + float(mon6controller or 0) + float(mon6throttle or 0) + float(mon6brake or 0) + float(
        mon6spokes or 0) + float(mon6enclosure or 0) + float(mon6breaker or 0) + float(mon6display or 0) + float(
        mon6connector or 0) + float(mon6wire or 0) + float(mon6thimble or 0)
    mon5purchase = float(mon5cell or 0) + float(mon5bms or 0) + float(mon5battery or 0) + float(mon5bike or 0) + float(
        mon5motor or 0) + float(mon5controller or 0) + float(mon5throttle or 0) + float(mon5brake or 0) + float(
        mon5spokes or 0) + float(mon5enclosure or 0) + float(mon5breaker or 0) + float(mon5display or 0) + float(
        mon5connector or 0) + float(mon5wire or 0) + float(mon5thimble or 0)
    mon4purchase = float(mon4cell or 0) + float(mon4bms or 0) + float(mon4battery or 0) + float(mon4bike or 0) + float(
        mon4motor or 0) + float(mon4controller or 0) + float(mon4throttle or 0) + float(mon4brake or 0) + float(
        mon4spokes or 0) + float(mon4enclosure or 0) + float(mon4breaker or 0) + float(mon4display or 0) + float(
        mon4connector or 0) + float(mon4wire or 0) + float(mon4thimble or 0)
    mon3purchase = float(mon3cell or 0) + float(mon3bms or 0) + float(mon3battery or 0) + float(mon3bike or 0) + float(
        mon3motor or 0) + float(mon3controller or 0) + float(mon3throttle or 0) + float(mon3brake or 0) + float(
        mon3spokes or 0) + float(mon3enclosure or 0) + float(mon3breaker or 0) + float(mon3display or 0) + float(
        mon3connector or 0) + float(mon3wire or 0) + float(mon3thimble or 0)
    mon2purchase = float(mon2cell or 0) + float(mon2bms or 0) + float(mon2battery or 0) + float(mon2bike or 0) + float(
        mon2motor or 0) + float(mon2controller or 0) + float(mon2throttle or 0) + float(mon2brake or 0) + float(
        mon2spokes or 0) + float(mon2enclosure or 0) + float(mon2breaker or 0) + float(mon2display or 0) + float(
        mon2connector or 0) + float(mon2wire or 0) + float(mon2thimble or 0)
    mon1purchase = float(mon1cell or 0) + float(mon1bms or 0) + float(mon1battery or 0) + float(mon1bike or 0) + float(
        mon1motor or 0) + float(mon1controller or 0) + float(mon1throttle or 0) + float(mon1brake or 0) + float(
        mon1spokes or 0) + float(mon1enclosure or 0) + float(mon1breaker or 0) + float(mon1display or 0) + float(
        mon1connector or 0) + float(mon1wire or 0) + float(mon1thimble or 0)

    for bat1 in batt:
        if 30 >= bat1.MinVolt >= 0:
            x += 1
    for bat1 in batt:
        if bat1.MaxVolt >= 250:
            y += 1
    context = {
        'T_Chargers': T_Chargers,
        'batt': batt,
        'x': x,
        'y': y,
        'btinfo': btinfo,
        'mon6': mon6,
        'mon5': mon5,
        'mon4': mon4,
        'mon3': mon3,
        'mon2': mon2,
        'mon1': mon1,
        'mon6purchase': mon6purchase,
        'mon5purchase': mon5purchase,
        'mon4purchase': mon4purchase,
        'mon3purchase': mon3purchase,
        'mon2purchase': mon2purchase,
        'mon1purchase': mon1purchase,
        'mon6sale': float(mon6sale or 0),
        'mon5sale': float(mon5sale or 0),
        'mon4sale': float(mon4sale or 0),
        'mon3sale': float(mon3sale or 0),
        'mon2sale': float(mon2sale or 0),
        'mon1sale': float(mon1sale or 0),
        'mon6profit': float(mon6sale or 0) - mon6purchase,
        'mon5profit': float(mon5sale or 0) - mon5purchase,
        'mon4profit': float(mon4sale or 0) - mon4purchase,
        'mon3profit': float(mon3sale or 0) - mon3purchase,
        'mon2profit': float(mon2sale or 0) - mon2purchase,
        'mon1profit': float(mon1sale or 0) - mon1purchase,
    }
    return render(request, "index.html", context)


#  @login_required()
def add_battery_view(request):
    form = EMDataForm(request.POST or None)
    if form.is_valid():
        form.save()
    if 'submitData' in request.POST:
        p1 = request.POST['BatType']
        p2 = request.POST['MaxVolt']
        p3 = request.POST['MinVolt']
        p4 = request.POST['MaxAmp']
        p5 = request.POST['MinAmp']
        p6 = request.POST['SCMaxVolt']
        p7 = request.POST['SCMinVolt']
        p8 = request.POST['Temp']
        p9 = request.POST['Manf_ID']
        p10 = request.POST['Latitude']
        p11 = request.POST['Longitude']
        port = request.POST['port']
        port = port.split().pop(0)
        baud_rate = request.POST['baud_rate']
        bmsdata = p1 + "#" + p2 + "#" + p3 + "#" + p4 + "#" + p5 + "#" + p6 + "#" + p7 + "#" + p8 + "#" + p9 + "#" + \
                  p10 + "#" + p11

        str1 = bmsdata
        ser = serial.Serial(
            port,
            baud_rate,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
        )
        time.sleep(1)
        # serial.write(str1.encode())
        if ser.isOpen():
            ser.close()
        ser.open()
        ser.isOpen()
        ser.write(str1.encode())
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(40)

        if out != '':
            print(">>" + out)

        ser.close()

    context = {
        'form': form,
        'Battery_Type': Battery_Type,
        'ports': ports
    }
    return render(request, "addbattery.html", context)


#    @login_required()
def add_charger_view(request):
    form = EMDataForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
        'Battery_Type': Battery_Type
    }

    return render(request, "addcharger.html", context)


#   @login_required()
class add_inventory_view:
    def add_inventory(request):
        activeuser = request.user.first_name
        if activeuser == "":
            activeuser = request.user
        context = {
            'BMS_Type': BMS_Type,
            'Cell_Type': Cell_Type,
            'Battery_pack': Battery_pack,
            'Bike_pack': Bike_pack,
            'motor_type': motor_type,
            'controller_type': controller_type,
            'activeuser': activeuser
        }
        return render(request, "addinventory.html", context)

    def AddCell(request):
        form = CellForm(request.POST or None)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
        }
        return render(request, "addinventory.html", context)

    def AddBMS(request):
        form = BMSForm(request.POST or None)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
        }
        return render(request, "addinventory.html", context)

    def AddBattery(request):
        form = BatteryPackForm(request.POST or None)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
        }
        return render(request, "addinventory.html", context)

    def AddBike(request):
        form = BikePackForm(request.POST or None)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
        }
        return render(request, "addinventory.html", context)

    def AddBikeAccess(request):
        form = BikeAccessoryForm(request.POST or None)
        if form.is_valid():
            motor_qty = request.POST.get('motor_qty')
            motor_price = request.POST.get('motor_price')
            motor_PUP = motor_price / motor_qty
            form.instance.motor_PUP = motor_PUP
            form.save()
        context = {
            'form': form,
        }
        return render(request, "addinventory.html", context)

    def AddBatteryAccess(request):
        form = BatteryAccessoryForm(request.POST or None)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
        }
        return render(request, "addinventory.html", context)


def battery_view(request):
    battery = Btdetail.objects.all()
    return render(request, "batterydetail.html", {'battery': battery})


def charger_view(request):
    battery = Btdetail.objects.all()
    return render(request, "chargerdetail.html", {'battery': battery})


def deletecharger_view(request, id):
    Btdetail.objects.get(id=id).delete()
    return redirect("charger")


def inventory_view(request):
    Cell_detail = Celldetail.objects.all().order_by('-DatePur')
    BMS_detail = BMSdetail.objects.all().order_by('-DatePur')
    Battery_pack = BatteryPackdetail.objects.all().order_by('-DatePur')
    Bike_pack = BikePackdetail.objects.all().order_by('-DatePur')
    Battery_detail = BatteryAccessorydetail.objects.all().order_by('-DatePur')
    Bike_detail = BikeAccessorydetail.objects.all().order_by('-DatePur')

    context = {
        'Cell_detail': Cell_detail,
        'BMS_detail': BMS_detail,
        'Battery_pack': Battery_pack,
        'Bike_pack': Bike_pack,
        'Battery_detail': Battery_detail,
        'Bike_detail': Bike_detail,
    }
    return render(request, "inventorydetail.html", context)


class deleteinventory:
    def deletecell_view(request, id):
        Celldetail.objects.get(id=id).delete()
        return redirect("inventory")

    def deletebms_view(request, id):
        BMSdetail.objects.get(id=id).delete()
        return redirect("inventory")

    def deletebattery_view(request, id):
        BatteryPackdetail.objects.get(id=id).delete()
        return redirect("inventory")

    def deletebike_view(request, id):
        BikePackdetail.objects.get(id=id).delete()
        return redirect("inventory")

    def deletebatteryA_view(request, id):
        BatteryAccessorydetail.objects.get(id=id).delete()
        return redirect("inventory")

    def deletebikeA_view(request, id):
        BikeAccessorydetail.objects.get(id=id).delete()
        return redirect("inventory")

    def deletecustomer_view(request, id):
        CustomerDetail.objects.get(id=id).delete()
        return redirect("customer")


# @login_required()
def store_view(request):
    # Cell
    L6_ah = Celldetail.objects.filter(Cell_Type='LifoPO4 6Ah').aggregate(Sum('Cell_qty'))['Cell_qty__sum']
    if CustomerDetail.objects.filter(Cell_Type='LifoPO4 6Ah').aggregate(Sum('Cell_qty'))['Cell_qty__sum']:
        L6_ah = L6_ah - CustomerDetail.objects.filter(Cell_Type='LifoPO4 6Ah').aggregate(Sum('Cell_qty'))[
            'Cell_qty__sum']
    if CustomerDetail.objects.filter(Cell_Type1='LifoPO4 6Ah').aggregate(Sum('Cell_qty1'))['Cell_qty1__sum']:
        L6_ah = L6_ah - CustomerDetail.objects.filter(Cell_Type1='LifoPO4 6Ah').aggregate(Sum('Cell_qty1'))[
            'Cell_qty1__sum']
    if CustomerDetail.objects.filter(Cell_Type2='LifoPO4 6Ah').aggregate(Sum('Cell_qty2'))['Cell_qty2__sum']:
        L6_ah = L6_ah - CustomerDetail.objects.filter(Cell_Type2='LifoPO4 6Ah').aggregate(Sum('Cell_qty2'))[
            'Cell_qty2__sum']
    if CustomerDetail.objects.filter(Cell_Type3='LifoPO4 6Ah').aggregate(Sum('Cell_qty3'))['Cell_qty3__sum']:
        L6_ah = L6_ah - CustomerDetail.objects.filter(Cell_Type3='LifoPO4 6Ah').aggregate(Sum('Cell_qty3'))[
            'Cell_qty3__sum']
    if CustomerDetail.objects.filter(Cell_Type4='LifoPO4 6Ah').aggregate(Sum('Cell_qty4'))['Cell_qty4__sum']:
        L6_ah = L6_ah - CustomerDetail.objects.filter(Cell_Type4='LifoPO4 6Ah').aggregate(Sum('Cell_qty4'))[
            'Cell_qty4__sum']
    L6_ahPrize = L6_ah * (Celldetail.objects.filter(Cell_Type='LifoPO4 6Ah').aggregate(Sum('Cell_PUP'))[
                              'Cell_PUP__sum'] / Celldetail.objects.filter(Cell_Type='LifoPO4 6Ah').count())
    L6_ahPUP = L6_ahPrize/L6_ah if L6_ah else 0

    L20_ah = Celldetail.objects.filter(Cell_Type='LifoPO4 20Ah').aggregate(Sum('Cell_qty'))['Cell_qty__sum']
    if CustomerDetail.objects.filter(Cell_Type='LifoPO4 20Ah').aggregate(Sum('Cell_qty'))['Cell_qty__sum']:
        L20_ah = L20_ah - CustomerDetail.objects.filter(Cell_Type='LifoPO4 20Ah').aggregate(Sum('Cell_qty'))[
            'Cell_qty__sum']
    if CustomerDetail.objects.filter(Cell_Type1='LifoPO4 20Ah').aggregate(Sum('Cell_qty1'))['Cell_qty1__sum']:
        L20_ah = L20_ah - CustomerDetail.objects.filter(Cell_Type1='LifoPO4 20Ah').aggregate(Sum('Cell_qty1'))[
            'Cell_qty1__sum']
    if CustomerDetail.objects.filter(Cell_Type2='LifoPO4 20Ah').aggregate(Sum('Cell_qty2'))['Cell_qty2__sum']:
        L20_ah = L20_ah - CustomerDetail.objects.filter(Cell_Type2='LifoPO4 20Ah').aggregate(Sum('Cell_qty2'))[
            'Cell_qty2__sum']
    if CustomerDetail.objects.filter(Cell_Type3='LifoPO4 20Ah').aggregate(Sum('Cell_qty3'))['Cell_qty3__sum']:
        L20_ah = L20_ah - CustomerDetail.objects.filter(Cell_Type3='LifoPO4 20Ah').aggregate(Sum('Cell_qty3'))[
            'Cell_qty3__sum']
    if CustomerDetail.objects.filter(Cell_Type4='LifoPO4 20Ah').aggregate(Sum('Cell_qty4'))['Cell_qty4__sum']:
        L20_ah = L20_ah - CustomerDetail.objects.filter(Cell_Type4='LifoPO4 20Ah').aggregate(Sum('Cell_qty4'))[
            'Cell_qty4__sum']
    L20_ahPrize = L20_ah * (Celldetail.objects.filter(Cell_Type='LifoPO4 20Ah').aggregate(Sum('Cell_PUP'))[
                                'Cell_PUP__sum'] / Celldetail.objects.filter(Cell_Type='LifoPO4 20Ah').count())
    L20_ahPUP = L20_ahPrize/L20_ah if L20_ah else 0

    L25_ah = Celldetail.objects.filter(Cell_Type='LifoPO4 25Ah').aggregate(Sum('Cell_qty'))['Cell_qty__sum']
    if CustomerDetail.objects.filter(Cell_Type='LifoPO4 25Ah').aggregate(Sum('Cell_qty'))['Cell_qty__sum']:
        L25_ah = L25_ah - CustomerDetail.objects.filter(Cell_Type='LifoPO4 25Ah').aggregate(Sum('Cell_qty'))[
            'Cell_qty__sum']
    if CustomerDetail.objects.filter(Cell_Type1='LifoPO4 25Ah').aggregate(Sum('Cell_qty1'))['Cell_qty1__sum']:
        L25_ah = L25_ah - CustomerDetail.objects.filter(Cell_Type1='LifoPO4 25Ah').aggregate(Sum('Cell_qty1'))[
            'Cell_qty1__sum']
    if CustomerDetail.objects.filter(Cell_Type2='LifoPO4 25Ah').aggregate(Sum('Cell_qty2'))['Cell_qty2__sum']:
        L25_ah = L25_ah - CustomerDetail.objects.filter(Cell_Type2='LifoPO4 25Ah').aggregate(Sum('Cell_qty2'))[
            'Cell_qty2__sum']
    if CustomerDetail.objects.filter(Cell_Type3='LifoPO4 25Ah').aggregate(Sum('Cell_qty3'))['Cell_qty3__sum']:
        L25_ah = L25_ah - CustomerDetail.objects.filter(Cell_Type3='LifoPO4 25Ah').aggregate(Sum('Cell_qty3'))[
            'Cell_qty3__sum']
    if CustomerDetail.objects.filter(Cell_Type4='LifoPO4 25Ah').aggregate(Sum('Cell_qty4'))['Cell_qty4__sum']:
        L25_ah = L25_ah - CustomerDetail.objects.filter(Cell_Type4='LifoPO4 25Ah').aggregate(Sum('Cell_qty4'))[
            'Cell_qty4__sum']
    L25_ahPrize = L25_ah * (Celldetail.objects.filter(Cell_Type='LifoPO4 25Ah').aggregate(Sum('Cell_PUP'))[
                                'Cell_PUP__sum'] / Celldetail.objects.filter(Cell_Type='LifoPO4 25Ah').count())
    L25_ahPUP = L25_ahPrize/L25_ah if L25_ah else 0

    L40_ah = Celldetail.objects.filter(Cell_Type='LifoPO4 40Ah').aggregate(Sum('Cell_qty'))['Cell_qty__sum']
    if CustomerDetail.objects.filter(Cell_Type='LifoPO4 40Ah').aggregate(Sum('Cell_qty'))['Cell_qty__sum']:
        L40_ah = L40_ah - CustomerDetail.objects.filter(Cell_Type='LifoPO4 40Ah').aggregate(Sum('Cell_qty'))[
            'Cell_qty__sum']
    if CustomerDetail.objects.filter(Cell_Type1='LifoPO4 40Ah').aggregate(Sum('Cell_qty1'))['Cell_qty1__sum']:
        L40_ah = L40_ah - CustomerDetail.objects.filter(Cell_Type1='LifoPO4 40Ah').aggregate(Sum('Cell_qty1'))[
            'Cell_qty1__sum']
    if CustomerDetail.objects.filter(Cell_Type2='LifoPO4 40Ah').aggregate(Sum('Cell_qty2'))['Cell_qty2__sum']:
        L40_ah = L40_ah - CustomerDetail.objects.filter(Cell_Type2='LifoPO4 40Ah').aggregate(Sum('Cell_qty2'))[
            'Cell_qty2__sum']
    if CustomerDetail.objects.filter(Cell_Type3='LifoPO4 40Ah').aggregate(Sum('Cell_qty3'))['Cell_qty3__sum']:
        L40_ah = L40_ah - CustomerDetail.objects.filter(Cell_Type3='LifoPO4 40Ah').aggregate(Sum('Cell_qty3'))[
            'Cell_qty3__sum']
    if CustomerDetail.objects.filter(Cell_Type4='LifoPO4 40Ah').aggregate(Sum('Cell_qty4'))['Cell_qty4__sum']:
        L40_ah = L40_ah - CustomerDetail.objects.filter(Cell_Type4='LifoPO4 40Ah').aggregate(Sum('Cell_qty4'))[
            'Cell_qty4__sum']
    L40_ahPrize = L40_ah * (Celldetail.objects.filter(Cell_Type='LifoPO4 40Ah').aggregate(Sum('Cell_PUP'))[
                                'Cell_PUP__sum'] / Celldetail.objects.filter(Cell_Type='LifoPO4 40Ah').count())
    L40_ahPUP = L40_ahPrize/L40_ah if L40_ah else 0

    L50_ah = Celldetail.objects.filter(Cell_Type='LifoPO4 50Ah').aggregate(Sum('Cell_qty'))['Cell_qty__sum']
    if CustomerDetail.objects.filter(Cell_Type='LifoPO4 50Ah').aggregate(Sum('Cell_qty'))['Cell_qty__sum']:
        L50_ah = L50_ah - CustomerDetail.objects.filter(Cell_Type='LifoPO4 50Ah').aggregate(Sum('Cell_qty'))[
            'Cell_qty__sum']
    if CustomerDetail.objects.filter(Cell_Type1='LifoPO4 50Ah').aggregate(Sum('Cell_qty1'))['Cell_qty1__sum']:
        L50_ah = L50_ah - CustomerDetail.objects.filter(Cell_Type1='LifoPO4 50Ah').aggregate(Sum('Cell_qty1'))[
            'Cell_qty1__sum']
    if CustomerDetail.objects.filter(Cell_Type2='LifoPO4 50Ah').aggregate(Sum('Cell_qty2'))['Cell_qty2__sum']:
        L50_ah = L50_ah - CustomerDetail.objects.filter(Cell_Type2='LifoPO4 50Ah').aggregate(Sum('Cell_qty2'))[
            'Cell_qty2__sum']
    if CustomerDetail.objects.filter(Cell_Type3='LifoPO4 50Ah').aggregate(Sum('Cell_qty3'))['Cell_qty3__sum']:
        L50_ah = L50_ah - CustomerDetail.objects.filter(Cell_Type3='LifoPO4 50Ah').aggregate(Sum('Cell_qty3'))[
            'Cell_qty3__sum']
    if CustomerDetail.objects.filter(Cell_Type4='LifoPO4 50Ah').aggregate(Sum('Cell_qty4'))['Cell_qty4__sum']:
        L50_ah = L50_ah - CustomerDetail.objects.filter(Cell_Type4='LifoPO4 50Ah').aggregate(Sum('Cell_qty4'))[
            'Cell_qty4__sum']
    L50_ahPrize = L50_ah * (Celldetail.objects.filter(Cell_Type='LifoPO4 50Ah').aggregate(Sum('Cell_PUP'))[
                                'Cell_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 4S 20A').count())
    L50_ahPUP = L50_ahPrize/L50_ah if L50_ah else 0

    L105_ah = Celldetail.objects.filter(Cell_Type='LifoPO4 105Ah').aggregate(Sum('Cell_qty'))['Cell_qty__sum']
    if CustomerDetail.objects.filter(Cell_Type='LifoPO4 105Ah').aggregate(Sum('Cell_qty'))['Cell_qty__sum']:
        L105_ah = L105_ah - CustomerDetail.objects.filter(Cell_Type='LifoPO4 105Ah').aggregate(Sum('Cell_qty'))[
            'Cell_qty__sum']
    if CustomerDetail.objects.filter(Cell_Type1='LifoPO4 105Ah').aggregate(Sum('Cell_qty1'))['Cell_qty1__sum']:
        L105_ah = L105_ah - CustomerDetail.objects.filter(Cell_Type1='LifoPO4 105Ah').aggregate(Sum('Cell_qty1'))[
            'Cell_qty1__sum']
    if CustomerDetail.objects.filter(Cell_Type2='LifoPO4 105Ah').aggregate(Sum('Cell_qty2'))['Cell_qty2__sum']:
        L105_ah = L105_ah - CustomerDetail.objects.filter(Cell_Type2='LifoPO4 105Ah').aggregate(Sum('Cell_qty2'))[
            'Cell_qty2__sum']
    if CustomerDetail.objects.filter(Cell_Type3='LifoPO4 105Ah').aggregate(Sum('Cell_qty3'))['Cell_qty3__sum']:
        L105_ah = L105_ah - CustomerDetail.objects.filter(Cell_Type3='LifoPO4 105Ah').aggregate(Sum('Cell_qty3'))[
            'Cell_qty3__sum']
    if CustomerDetail.objects.filter(Cell_Type4='LifoPO4 105Ah').aggregate(Sum('Cell_qty4'))['Cell_qty4__sum']:
        L105_ah = L105_ah - CustomerDetail.objects.filter(Cell_Type4='LifoPO4 105Ah').aggregate(Sum('Cell_qty4'))[
            'Cell_qty4__sum']
    L105_ahPrize = L105_ah * (Celldetail.objects.filter(Cell_Type='LifoPO4 105Ah').aggregate(Sum('Cell_PUP'))[
                                  'Cell_PUP__sum'] / Celldetail.objects.filter(Cell_Type='LifoPO4 105Ah').count())
    L105_ahPUP = L105_ahPrize/L105_ah if L105_ah else 0

    L205_ah = Celldetail.objects.filter(Cell_Type='LifoPO4 205Ah').aggregate(Sum('Cell_qty'))['Cell_qty__sum']
    if CustomerDetail.objects.filter(Cell_Type='LifoPO4 205Ah').aggregate(Sum('Cell_qty'))['Cell_qty__sum']:
        L205_ah = L205_ah - CustomerDetail.objects.filter(Cell_Type='LifoPO4 205Ah').aggregate(Sum('Cell_qty'))[
            'Cell_qty__sum']
    if CustomerDetail.objects.filter(Cell_Type1='LifoPO4 205Ah').aggregate(Sum('Cell_qty1'))['Cell_qty1__sum']:
        L205_ah = L205_ah - CustomerDetail.objects.filter(Cell_Type1='LifoPO4 205Ah').aggregate(Sum('Cell_qty1'))[
            'Cell_qty2__sum']
    if CustomerDetail.objects.filter(Cell_Type2='LifoPO4 205Ah').aggregate(Sum('Cell_qty2'))['Cell_qty2__sum']:
        L205_ah = L205_ah - CustomerDetail.objects.filter(Cell_Type2='LifoPO4 205Ah').aggregate(Sum('Cell_qty2'))[
            'Cell_qty2__sum']
    if CustomerDetail.objects.filter(Cell_Type3='LifoPO4 205Ah').aggregate(Sum('Cell_qty3'))['Cell_qty3__sum']:
        L205_ah = L205_ah - CustomerDetail.objects.filter(Cell_Type3='LifoPO4 205Ah').aggregate(Sum('Cell_qty3'))[
            'Cell_qty3__sum']
    if CustomerDetail.objects.filter(Cell_Type4='LifoPO4 205Ah').aggregate(Sum('Cell_qty4'))['Cell_qty4__sum']:
        L205_ah = L205_ah - CustomerDetail.objects.filter(Cell_Type4='LifoPO4 205Ah').aggregate(Sum('Cell_qty4'))[
            'Cell_qty4__sum']
    L205_ahPrize = L205_ah * (Celldetail.objects.filter(Cell_Type='LifoPO4 205Ah').aggregate(Sum('Cell_PUP'))[
                                  'Cell_PUP__sum'] / Celldetail.objects.filter(Cell_Type='LifoPO4 205Ah').count())
    L205_ahPUP = L205_ahPrize/L205_ah if L205_ah else 0

    # BMS
    S4_20ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 4S 20A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 4S 20A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']:
        S4_20ah = S4_20ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 4S 20A').aggregate(Sum('BMS_qty'))[
            'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 4S 20A').aggregate(Sum('BMS_qty1'))['BMS_qty1__sum']:
        S4_20ah = S4_20ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 4S 20A').aggregate(Sum('BMS_qty1'))[
            'BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 4S 20A').aggregate(Sum('BMS_qty2'))['BMS_qty2__sum']:
        S4_20ah = S4_20ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 4S 20A').aggregate(Sum('BMS_qty2'))[
            'BMS_qty2__sum']
    S4_20ahPrize = S4_20ah * (BMSdetail.objects.filter(BMS_Type='LifoPO4 4S 20A').aggregate(Sum('BMS_PUP'))[
                                  'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 4S 20A').count())
    S4_20ahPUP = S4_20ahPrize/S4_20ah if S4_20ah else 0

    S4_50ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 4S 50A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 4S 50A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']:
        S4_50ah = S4_50ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 4S 50A').aggregate(Sum('BMS_qty'))[
            'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 4S 50A').aggregate(Sum('BMS_qty1'))['BMS_qty1__sum']:
        S4_50ah = S4_50ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 4S 50A').aggregate(Sum('BMS_qty1'))[
            'BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 4S 50A').aggregate(Sum('BMS_qty2'))['BMS_qty2__sum']:
        S4_50ah = S4_50ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 4S 50A').aggregate(Sum('BMS_qty2'))[
            'BMS_qty2__sum']
    S4_50ahPrize = S4_50ah * (BMSdetail.objects.filter(BMS_Type='LifoPO4 4S 50A').aggregate(Sum('BMS_PUP'))[
                                  'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 4S 50A').count())
    S4_50ahPUP = S4_50ahPrize/S4_50ah if S4_50ah else 0

    S4_100ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 4S 100A', BMSType='Simple').aggregate(Sum('BMS_qty'))[
        'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 4S 100A', BMSType='Simple').aggregate(Sum('BMS_qty'))[
        'BMS_qty__sum']:
        S4_100ah = S4_100ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 4S 100A', BMSType='Simple').aggregate(
            Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 4S 100A', BMSType1='Simple').aggregate(Sum('BMS_qty1'))[
        'BMS_qty1__sum']:
        S4_100ah = S4_100ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 4S 100A', BMSType1='Simple').aggregate(
            Sum('BMS_qty1'))['BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 4S 100A', BMSType2='Simple').aggregate(Sum('BMS_qty2'))[
        'BMS_qty2__sum']:
        S4_100ah = S4_100ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 4S 100A', BMSType2='Simple').aggregate(
            Sum('BMS_qty2'))['BMS_qty2__sum']
    S4_100ahPrize = S4_100ah * (
            BMSdetail.objects.filter(BMS_Type='LifoPO4 4S 100A', BMSType='Simple').aggregate(Sum('BMS_PUP'))[
                'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 4S 100A', BMSType='Simple').count())
    S4_100ahPUP = S4_100ahPrize/S4_100ah if S4_100ah else 0

    S4_200ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 4S 200A', BMSType='Simple').aggregate(Sum('BMS_qty'))[
        'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 4S 200A', BMSType='Simple').aggregate(Sum('BMS_qty'))[
        'BMS_qty__sum']:
        S4_200ah = S4_200ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 4S 200A', BMSType='Simple').aggregate(
            Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 4S 200A', BMSType1='Simple').aggregate(Sum('BMS_qty1'))[
        'BMS_qty1__sum']:
        S4_200ah = S4_200ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 4S 200A', BMSType1='Simple').aggregate(
            Sum('BMS_qty1'))['BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 4S 200A', BMSType2='Simple').aggregate(Sum('BMS_qty2'))[
        'BMS_qty2__sum']:
        S4_200ah = S4_200ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 4S 200A', BMSType2='Simple').aggregate(
            Sum('BMS_qty2'))['BMS_qty2__sum']
    S4_200ahPrize = S4_200ah * (
            BMSdetail.objects.filter(BMS_Type='LifoPO4 4S 200A', BMSType='Simple').aggregate(Sum('BMS_PUP'))[
                'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 4S 200A', BMSType='Simple').count())
    S4_200ahPUP = S4_200ahPrize/S4_200ah if S4_200ah else 0

    S4_S100ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 4S 100A', BMSType='Smart').aggregate(Sum('BMS_qty'))[
        'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 4S 100A', BMSType='Smart').aggregate(Sum('BMS_qty'))[
        'BMS_qty__sum']:
        S4_S100ah = S4_S100ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 4S 100A', BMSType='Smart').aggregate(
            Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 4S 100A', BMSType1='Smart').aggregate(Sum('BMS_qty1'))[
        'BMS_qty1__sum']:
        S4_S100ah = S4_S100ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 4S 100A', BMSType1='Smart').aggregate(
            Sum('BMS_qty1'))['BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 4S 100A', BMSType2='Smart').aggregate(Sum('BMS_qty2'))[
        'BMS_qty2__sum']:
        S4_S100ah = S4_S100ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 4S 100A', BMSType2='Smart').aggregate(
            Sum('BMS_qty2'))['BMS_qty2__sum']
    S4_S100ahPrize = S4_S100ah * (
            BMSdetail.objects.filter(BMS_Type='LifoPO4 4S 100A', BMSType='Smart').aggregate(Sum('BMS_PUP'))[
                'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 4S 100A', BMSType='Smart').count())
    S4_S100ahPUP = S4_S100ahPrize/S4_S100ah if S4_S100ah else 0

    S4_S200ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 4S 200A', BMSType='Smart').aggregate(Sum('BMS_qty'))[
        'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 4S 200A', BMSType='Smart').aggregate(Sum('BMS_qty'))[
        'BMS_qty__sum']:
        S4_S200ah = S4_S200ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 4S 200A', BMSType='Smart').aggregate(
            Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 4S 200A', BMSType1='Smart').aggregate(Sum('BMS_qty1'))[
        'BMS_qty1__sum']:
        S4_S200ah = S4_S200ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 4S 200A', BMSType1='Smart').aggregate(
            Sum('BMS_qty1'))['BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 4S 200A', BMSType2='Smart').aggregate(Sum('BMS_qty2'))[
        'BMS_qty2__sum']:
        S4_S200ah = S4_S200ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 4S 200A', BMSType2='Smart').aggregate(
            Sum('BMS_qty2'))['BMS_qty2__sum']
    S4_S200ahPrize = S4_S200ah * (
            BMSdetail.objects.filter(BMS_Type='LifoPO4 4S 200A', BMSType='Smart').aggregate(Sum('BMS_PUP'))[
                'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 4S 200A', BMSType='Smart').count())
    S4_S200ahPUP = S4_S200ahPrize/S4_S200ah if S4_S200ah else 0

    S8_50ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 8S 50A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 8S 50A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']:
        S8_50ah = S8_50ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 8S 50A').aggregate(Sum('BMS_qty'))[
            'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 8S 50A').aggregate(Sum('BMS_qty1'))['BMS_qty1__sum']:
        S8_50ah = S8_50ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 8S 50A').aggregate(Sum('BMS_qty1'))[
            'BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 8S 50A').aggregate(Sum('BMS_qty2'))['BMS_qty2__sum']:
        S8_50ah = S8_50ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 8S 50A').aggregate(Sum('BMS_qty2'))[
            'BMS_qty2__sum']
    S8_50ahPrize = S8_50ah * (BMSdetail.objects.filter(BMS_Type='LifoPO4 8S 50A').aggregate(Sum('BMS_PUP'))[
                                  'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 8S 50A').count())
    S8_50ahPUP = S8_50ahPrize/S8_50ah if S8_50ah else 0

    S8_100ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 8S 100A', BMSType='Simple').aggregate(Sum('BMS_qty'))[
        'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 8S 100A', BMSType='Simple').aggregate(Sum('BMS_qty'))[
        'BMS_qty__sum']:
        S8_100ah = S8_100ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 8S 100A', BMSType='Simple').aggregate(
            Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 8S 100A', BMSType1='Simple').aggregate(Sum('BMS_qty1'))[
        'BMS_qty1__sum']:
        S8_100ah = S8_100ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 8S 100A', BMSType1='Simple').aggregate(
            Sum('BMS_qty1'))['BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 8S 100A', BMSType2='Simple').aggregate(Sum('BMS_qty2'))[
        'BMS_qty2__sum']:
        S8_100ah = S8_100ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 8S 100A', BMSType2='Simple').aggregate(
            Sum('BMS_qty2'))['BMS_qty2__sum']
    S8_100ahPrize = S8_100ah * (
            BMSdetail.objects.filter(BMS_Type='LifoPO4 8S 100A', BMSType='Simple').aggregate(Sum('BMS_PUP'))[
                'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 8S 100A', BMSType='Simple').count())
    S8_100ahPUP = S8_100ahPrize/S8_100ah if S8_100ah else 0

    S8_S100ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 8S 100A', BMSType='Smart').aggregate(Sum('BMS_qty'))[
        'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 8S 100A', BMSType='Smart').aggregate(Sum('BMS_qty'))[
        'BMS_qty__sum']:
        S8_S100ah = S8_S100ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 8S 100A', BMSType='Smart').aggregate(
            Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 8S 100A', BMSType1='Smart').aggregate(Sum('BMS_qty1'))[
        'BMS_qty1__sum']:
        S8_S100ah = S8_S100ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 8S 100A', BMSType1='Smart').aggregate(
            Sum('BMS_qty1'))['BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 8S 100A', BMSType2='Smart').aggregate(Sum('BMS_qty2'))[
        'BMS_qty2__sum']:
        S8_S100ah = S8_S100ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 8S 100A', BMSType2='Smart').aggregate(
            Sum('BMS_qty2'))['BMS_qty2__sum']
    S8_S100ahPrize = S8_S100ah * (
            BMSdetail.objects.filter(BMS_Type='LifoPO4 8S 100A', BMSType='Smart').aggregate(Sum('BMS_PUP'))[
                'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 8S 100A', BMSType='Smart').count())
    S8_S100ahPUP = S8_S100ahPrize/S8_S100ah if S8_S100ah else 0

    S8_200ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 8S 200A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 8S 200A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']:
        S8_200ah = S8_200ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 8S 200A').aggregate(Sum('BMS_qty'))[
            'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 8S 200A').aggregate(Sum('BMS_qty1'))['BMS_qty1__sum']:
        S8_200ah = S8_200ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 8S 200A').aggregate(Sum('BMS_qty1'))[
            'BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 8S 200A').aggregate(Sum('BMS_qty2'))['BMS_qty2__sum']:
        S8_200ah = S8_200ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 8S 200A').aggregate(Sum('BMS_qty2'))[
            'BMS_qty2__sum']
    S8_200ahPrize = S8_200ah * (BMSdetail.objects.filter(BMS_Type='LifoPO4 8S 200A').aggregate(Sum('BMS_PUP'))[
                                    'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 8S 200A').count())
    S8_200ahPUP = S8_200ahPrize/S8_200ah if S8_200ah else 0

    S15_50ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 15S 50A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 15S 50A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']:
        S15_50ah = S15_50ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 15S 50A').aggregate(Sum('BMS_qty'))[
            'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 15S 50A').aggregate(Sum('BMS_qty1'))['BMS_qty1__sum']:
        S15_50ah = S15_50ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 15S 50A').aggregate(Sum('BMS_qty1'))[
            'BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 15S 50A').aggregate(Sum('BMS_qty2'))['BMS_qty2__sum']:
        S15_50ah = S15_50ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 15S 50A').aggregate(Sum('BMS_qty2'))[
            'BMS_qty2__sum']
    S15_50ahPrize = S4_50ah * (BMSdetail.objects.filter(BMS_Type='LifoPO4 15S 50A').aggregate(Sum('BMS_PUP'))[
                                   'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 15S 50A').count())
    S15_50ahPUP = S15_50ahPrize/S15_50ah if S15_50ah else 0

    S15_100ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 15S 100A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 15S 100A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']:
        S15_100ah = S15_100ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 15S 100A').aggregate(Sum('BMS_qty'))[
            'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 15S 100A').aggregate(Sum('BMS_qty1'))['BMS_qty1__sum']:
        S15_100ah = S15_100ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 15S 100A').aggregate(Sum('BMS_qty1'))[
            'BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 15S 100A').aggregate(Sum('BMS_qty2'))['BMS_qty2__sum']:
        S15_100ah = S15_100ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 15S 100A').aggregate(Sum('BMS_qty2'))[
            'BMS_qty2__sum']
    S15_100ahPrize = S15_100ah * (BMSdetail.objects.filter(BMS_Type='LifoPO4 15S 100A').aggregate(Sum('BMS_PUP'))[
                                      'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 15S 100A').count())
    S15_100ahPUP = S15_100ahPrize/S15_100ah if S15_100ah else 0

    S15_200ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 15S 200A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 15S 200A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']:
        S15_200ah = S15_200ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 15S 200A').aggregate(Sum('BMS_qty'))[
            'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 15S 200A').aggregate(Sum('BMS_qty1'))['BMS_qty1__sum']:
        S15_200ah = S15_200ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 15S 200A').aggregate(Sum('BMS_qty1'))[
            'BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 15S 200A').aggregate(Sum('BMS_qty2'))['BMS_qty2__sum']:
        S15_200ah = S15_200ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 15S 200A').aggregate(Sum('BMS_qty2'))[
            'BMS_qty2__sum']
    S15_200ahPrize = S15_200ah * (BMSdetail.objects.filter(BMS_Type='LifoPO4 15S 200A').aggregate(Sum('BMS_PUP'))[
                                      'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 15S 200A').count())
    S15_200ahPUP = S15_200ahPrize/S15_200ah if S15_200ah else 0

    S16_50ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 16S 50A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 16S 50A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']:
        S16_50ah = S16_50ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 16S 50A').aggregate(Sum('BMS_qty'))[
            'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 16S 50A').aggregate(Sum('BMS_qty1'))['BMS_qty1__sum']:
        S16_50ah = S16_50ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 16S 50A').aggregate(Sum('BMS_qty1'))[
            'BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 16S 50A').aggregate(Sum('BMS_qty2'))['BMS_qty2__sum']:
        S16_50ah = S16_50ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 16S 50A').aggregate(Sum('BMS_qty2'))[
            'BMS_qty2__sum']
    S16_50ahPrize = S16_50ah * (BMSdetail.objects.filter(BMS_Type='LifoPO4 16S 50A').aggregate(Sum('BMS_PUP'))[
                                    'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 16S 50A').count())
    S16_50ahPUP = S16_50ahPrize/S16_50ah if S16_50ah else 0

    S16_100ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 16S 100A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 16S 100A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']:
        S16_100ah = S16_100ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 16S 100A').aggregate(Sum('BMS_qty'))[
            'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 16S 100A').aggregate(Sum('BMS_qty1'))['BMS_qty1__sum']:
        S16_100ah = S16_100ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 16S 100A').aggregate(Sum('BMS_qty1'))[
            'BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 16S 100A').aggregate(Sum('BMS_qty2'))['BMS_qty2__sum']:
        S16_100ah = S16_100ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 16S 100A').aggregate(Sum('BMS_qty2'))[
            'BMS_qty2__sum']
    S16_100ahPrize = S16_100ah * (BMSdetail.objects.filter(BMS_Type='LifoPO4 16S 100A').aggregate(Sum('BMS_PUP'))[
                                      'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 16S 100A').count())
    S16_100ahPUP = S16_100ahPrize/S16_100ah if S16_100ah else 0

    S16_200ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 16S 200A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 16S 200AA').aggregate(Sum('BMS_qty'))['BMS_qty__sum']:
        S16_200ah = S16_200ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 16S 200A').aggregate(Sum('BMS_qty'))[
            'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 16S 200AA').aggregate(Sum('BMS_qty1'))['BMS_qty1__sum']:
        S16_200ah = S16_200ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 16S 200A').aggregate(Sum('BMS_qty1'))[
            'BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 16S 200AA').aggregate(Sum('BMS_qty2'))['BMS_qty2__sum']:
        S16_200ah = S16_200ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 16S 200A').aggregate(Sum('BMS_qty2'))[
            'BMS_qty2__sum']
    S16_200ahPrize = S16_200ah * (BMSdetail.objects.filter(BMS_Type='LifoPO4 16S 200A').aggregate(Sum('BMS_PUP'))[
                                      'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 16S 200A').count())
    S16_200ahPUP = S16_200ahPrize/S16_200ah if S16_200ah else 0

    S19_60ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 19S 60A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 19S 60A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']:
        S19_60ah = S19_60ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 19S 60A').aggregate(Sum('BMS_qty'))[
            'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 19S 60A').aggregate(Sum('BMS_qty1'))['BMS_qty1__sum']:
        S19_60ah = S19_60ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 19S 60A').aggregate(Sum('BMS_qty1'))[
            'BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 19S 60A').aggregate(Sum('BMS_qty2'))['BMS_qty2__sum']:
        S19_60ah = S19_60ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 19S 60A').aggregate(Sum('BMS_qty2'))[
            'BMS_qty2__sum']
    S19_60ahPrize = S19_60ah * (BMSdetail.objects.filter(BMS_Type='LifoPO4 19S 60A').aggregate(Sum('BMS_PUP'))[
                                    'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 19S 60A').count())
    S19_60ahPUP = S19_60ahPrize/S19_60ah if S19_60ah else 0

    S19_100ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 19S 100A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 19S 100A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']:
        S19_100ah = S19_100ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 19S 100A').aggregate(Sum('BMS_qty'))[
            'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 19S 100A').aggregate(Sum('BMS_qty1'))['BMS_qty1__sum']:
        S19_100ah = S19_100ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 19S 100A').aggregate(Sum('BMS_qty1'))[
            'BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 19S 100A').aggregate(Sum('BMS_qty2'))['BMS_qty2__sum']:
        S19_100ah = S19_100ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 19S 100A').aggregate(Sum('BMS_qty2'))[
            'BMS_qty2__sum']
    S19_100ahPrize = S19_100ah * (BMSdetail.objects.filter(BMS_Type='LifoPO4 19S 100A').aggregate(Sum('BMS_PUP'))[
                                      'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 19S 100A').count())
    S19_100ahPUP = S19_100ahPrize/S19_100ah if S19_100ah else 0

    S20_60ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 20S 60A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 20S 60A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']:
        S20_60ah = S20_60ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 20S 60A').aggregate(Sum('BMS_qty'))[
            'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 20S 60A').aggregate(Sum('BMS_qty1'))['BMS_qty1__sum']:
        S20_60ah = S20_60ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 20S 60A').aggregate(Sum('BMS_qty1'))[
            'BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 20S 60A').aggregate(Sum('BMS_qty2'))['BMS_qty2__sum']:
        S20_60ah = S20_60ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 20S 60A').aggregate(Sum('BMS_qty2'))[
            'BMS_qty2__sum']
    S20_60ahPrize = S20_60ah * (BMSdetail.objects.filter(BMS_Type='LifoPO4 20S 60A').aggregate(Sum('BMS_PUP'))[
                                    'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 20S 60A').count())
    S20_60ahPUP = S20_60ahPrize/S20_60ah if S20_60ah else 0

    S20_100ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 20S 100A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 20S 100A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']:
        S20_100ah = S20_100ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 20S 100A').aggregate(Sum('BMS_qty'))[
            'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 20S 100A').aggregate(Sum('BMS_qty1'))['BMS_qty1__sum']:
        S20_100ah = S20_100ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 20S 100A').aggregate(Sum('BMS_qty1'))[
            'BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 20S 100A').aggregate(Sum('BMS_qty2'))['BMS_qty2__sum']:
        S20_100ah = S20_100ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 20S 100A').aggregate(Sum('BMS_qty2'))[
            'BMS_qty2__sum']
    S20_100ahPrize = S20_100ah * (BMSdetail.objects.filter(BMS_Type='LifoPO4 20S 100A').aggregate(Sum('BMS_PUP'))[
                                      'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 20S 100A').count())
    S20_100ahPUP = S20_100ahPrize/S20_100ah if S20_100ah else 0

    S23_50ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 23S 50A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 23S 50A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']:
        S23_50ah = S23_50ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 23S 50A').aggregate(Sum('BMS_qty'))[
            'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 23S 50A').aggregate(Sum('BMS_qty1'))['BMS_qty1__sum']:
        S23_50ah = S23_50ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 23S 50A').aggregate(Sum('BMS_qty1'))[
            'BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 23S 50A').aggregate(Sum('BMS_qty2'))['BMS_qty2__sum']:
        S23_50ah = S23_50ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 23S 50A').aggregate(Sum('BMS_qty2'))[
            'BMS_qty2__sum']
    S23_50ahPrize = S23_50ah * (BMSdetail.objects.filter(BMS_Type='LifoPO4 23S 50A').aggregate(Sum('BMS_PUP'))[
                                    'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 23S 50A').count())
    S23_50ahPUP = S23_50ahPrize/S23_50ah if S23_50ah else 0

    S23_100ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 23S 100A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 23S 100A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']:
        S23_100ah = S23_100ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 23S 100A').aggregate(Sum('BMS_qty'))[
            'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 23S 100A').aggregate(Sum('BMS_qty1'))['BMS_qty1__sum']:
        S23_100ah = S23_100ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 23S 100A').aggregate(Sum('BMS_qty1'))[
            'BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 23S 100A').aggregate(Sum('BMS_qty2'))['BMS_qty2__sum']:
        S23_100ah = S23_100ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 23S 100A').aggregate(Sum('BMS_qty2'))[
            'BMS_qty2__sum']
    S23_100ahPrize = S23_100ah * (BMSdetail.objects.filter(BMS_Type='LifoPO4 23S 100A').aggregate(Sum('BMS_PUP'))[
                                      'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 23S 100A').count())
    S23_100ahPUP = S23_100ahPrize/S23_100ah if S23_100ah else 0

    S24_50ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 24S 50A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 24S 50A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']:
        S24_50ah = S24_50ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 24S 50A').aggregate(Sum('BMS_qty'))[
            'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 24S 50A').aggregate(Sum('BMS_qty1'))['BMS_qty1__sum']:
        S24_50ah = S24_50ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 24S 50A').aggregate(Sum('BMS_qty1'))[
            'BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 24S 50A').aggregate(Sum('BMS_qty2'))['BMS_qty2__sum']:
        S24_50ah = S24_50ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 24S 50A').aggregate(Sum('BMS_qty2'))[
            'BMS_qty2__sum']
    S24_50ahPrize = S24_50ah * (BMSdetail.objects.filter(BMS_Type='LifoPO4 24S 50A').aggregate(Sum('BMS_PUP'))[
                                    'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 24S 50A').count())
    S24_50ahPUP = S24_50ahPrize/S24_50ah if S24_50ah else 0

    S24_100ah = BMSdetail.objects.filter(BMS_Type='LifoPO4 24S 100A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type='LifoPO4 24S 100A').aggregate(Sum('BMS_qty'))['BMS_qty__sum']:
        S24_100ah = S24_100ah - CustomerDetail.objects.filter(BMS_Type='LifoPO4 24S 100A').aggregate(Sum('BMS_qty'))[
            'BMS_qty__sum']
    if CustomerDetail.objects.filter(BMS_Type1='LifoPO4 24S 100A').aggregate(Sum('BMS_qty1'))['BMS_qty1__sum']:
        S24_100ah = S24_100ah - CustomerDetail.objects.filter(BMS_Type1='LifoPO4 24S 100A').aggregate(Sum('BMS_qty1'))[
            'BMS_qty1__sum']
    if CustomerDetail.objects.filter(BMS_Type2='LifoPO4 24S 100A').aggregate(Sum('BMS_qty2'))['BMS_qty2__sum']:
        S24_100ah = S24_100ah - CustomerDetail.objects.filter(BMS_Type2='LifoPO4 24S 100A').aggregate(Sum('BMS_qty2'))[
            'BMS_qty2__sum']
    S24_100ahPrize = S24_100ah * (BMSdetail.objects.filter(BMS_Type='LifoPO4 24S 100A').aggregate(Sum('BMS_PUP'))[
                                      'BMS_PUP__sum'] / BMSdetail.objects.filter(BMS_Type='LifoPO4 24S 100A').count())
    S24_100ahPUP = S24_100ahPrize/S24_100ah if S24_100ah else 0

    # Battery Pack
    V12_25ah = BatteryPackdetail.objects.filter(Battery_pack='12V 25Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='12V 25Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V12_25ah = V12_25ah - CustomerDetail.objects.filter(Battery_pack='12V 25Ah').aggregate(Sum('Battery_pack_qty'))[
            'Battery_pack_qty__sum']
    V12_25ahPrize = V12_25ah * (
            BatteryPackdetail.objects.filter(Battery_pack='12V 25Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='12V 25Ah').count())
    V12_25ahPUP = V12_25ahPrize/V12_25ah if V12_25ah else 0

    V12_40ah = BatteryPackdetail.objects.filter(Battery_pack='12V 40Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='12V 40Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V12_40ah = V12_40ah - CustomerDetail.objects.filter(Battery_pack='12V 40Ah').aggregate(Sum('Battery_pack_qty'))[
            'Battery_pack_qty__sum']
    V12_40ahPrize = V12_40ah * (
            BatteryPackdetail.objects.filter(Battery_pack='12V 40Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='12V 40Ah').count())
    V12_40ahPUP = V12_40ahPrize/V12_40ah if V12_40ah else 0

    V12_50ah = BatteryPackdetail.objects.filter(Battery_pack='12V 50Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='12V 50Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V12_50ah = V12_50ah - CustomerDetail.objects.filter(Battery_pack='12V 50Ah').aggregate(Sum('Battery_pack_qty'))[
            'Battery_pack_qty__sum']
    V12_50ahPrize = V12_50ah * (
            BatteryPackdetail.objects.filter(Battery_pack='12V 50Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='12V 50Ah').count())
    V12_50ahPUP = V12_50ahPrize/V12_50ah if V12_50ah else 0

    V12_100ah = BatteryPackdetail.objects.filter(Battery_pack='12V 100Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='12V 100Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V12_100ah = V12_100ah - \
                    CustomerDetail.objects.filter(Battery_pack='12V 100Ah').aggregate(Sum('Battery_pack_qty'))[
                        'Battery_pack_qty__sum']
    V12_100ahPrize = V12_100ah * (
            BatteryPackdetail.objects.filter(Battery_pack='12V 100Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='12V 100Ah').count())
    V12_100ahPUP = V12_100ahPrize/V12_100ah if V12_100ah else 0

    V12_200ah = BatteryPackdetail.objects.filter(Battery_pack='12V 200Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='12V 200Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V12_200ah = V12_200ah - \
                    CustomerDetail.objects.filter(Battery_pack='12V 200Ah').aggregate(Sum('Battery_pack_qty'))[
                        'Battery_pack_qty__sum']
    V12_200ahPrize = V12_200ah * (
            BatteryPackdetail.objects.filter(Battery_pack='12V 200Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='12V 200Ah').count())
    V12_200ahPUP = V12_200ahPrize/V12_200ah if V12_200ah else 0

    V24_50ah = BatteryPackdetail.objects.filter(Battery_pack='24V 50Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='24V 50Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V24_50ah = V24_50ah - CustomerDetail.objects.filter(Battery_pack='24V 50Ah').aggregate(Sum('Battery_pack_qty'))[
            'Battery_pack_qty__sum']
    V24_50ahPrize = V24_50ah * (
            BatteryPackdetail.objects.filter(Battery_pack='24V 50Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='24V 50Ah').count())
    V24_50ahPUP = V24_50ahPrize/V24_50ah if V24_50ah else 0

    V24_100ah = BatteryPackdetail.objects.filter(Battery_pack='24V 100Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='24V 100Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V24_100ah = V24_100ah - \
                    CustomerDetail.objects.filter(Battery_pack='24V 100Ah').aggregate(Sum('Battery_pack_qty'))[
                        'Battery_pack_qty__sum']
    V24_100ahPrize = V24_100ah * (
            BatteryPackdetail.objects.filter(Battery_pack='24V 100Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='24V 100Ah').count())
    V24_100ahPUP = V24_100ahPrize/V24_100ah if V24_100ah else 0

    V24_200ah = BatteryPackdetail.objects.filter(Battery_pack='24V 200Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='24V 200Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V24_200ah = V24_200ah - \
                    CustomerDetail.objects.filter(Battery_pack='24V 200Ah').aggregate(Sum('Battery_pack_qty'))[
                        'Battery_pack_qty__sum']
    V24_200ahPrize = V24_200ah * (
            BatteryPackdetail.objects.filter(Battery_pack='24V 200Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='24V 200Ah').count())
    V24_200ahPUP = V24_200ahPrize/V24_200ah if V24_200ah else 0

    V48_25ah = BatteryPackdetail.objects.filter(Battery_pack='48V 25Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='48V 25Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V48_25ah = V48_25ah - CustomerDetail.objects.filter(Battery_pack='48V 25Ah').aggregate(Sum('Battery_pack_qty'))[
            'Battery_pack_qty__sum']
    V48_25ahPrize = V48_25ah * (
            BatteryPackdetail.objects.filter(Battery_pack='48V 25Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='48V 25Ah').count())
    V48_25ahPUP = V48_25ahPrize/V48_25ah if V48_25ah else 0

    V48_40ah = BatteryPackdetail.objects.filter(Battery_pack='48V 40Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='48V 40Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V48_40ah = V48_40ah - CustomerDetail.objects.filter(Battery_pack='48V 40Ah').aggregate(Sum('Battery_pack_qty'))[
            'Battery_pack_qty__sum']
    V48_40ahPrize = V48_40ah * (
            BatteryPackdetail.objects.filter(Battery_pack='48V 40Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='48V 40Ah').count())
    V48_40ahPUP = V48_40ahPrize/V48_40ah if V48_40ah else 0

    V48_50ah = BatteryPackdetail.objects.filter(Battery_pack='48V 50Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='48V 50Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V48_50ah = V48_50ah - CustomerDetail.objects.filter(Battery_pack='48V 50Ah').aggregate(Sum('Battery_pack_qty'))[
            'Battery_pack_qty__sum']
    V48_50ahPrize = V48_50ah * (
            BatteryPackdetail.objects.filter(Battery_pack='48V 50Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='48V 50Ah').count())
    V48_50ahPUP = V48_50ahPrize/V48_50ah if V48_50ah else 0

    V48_100ah = BatteryPackdetail.objects.filter(Battery_pack='48V 100Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='48V 100Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V48_100ah = V48_100ah - \
                    CustomerDetail.objects.filter(Battery_pack='48V 100Ah').aggregate(Sum('Battery_pack_qty'))[
                        'Battery_pack_qty__sum']
    V48_100ahPrize = V48_100ah * (
            BatteryPackdetail.objects.filter(Battery_pack='48V 100Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='48V 100Ah').count())
    V48_100ahPUP = V48_100ahPrize/V48_100ah if V48_100ah else 0

    V48_200ah = BatteryPackdetail.objects.filter(Battery_pack='48V 200Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='48V 200Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V48_200ah = V48_200ah - \
                    CustomerDetail.objects.filter(Battery_pack='48V 200Ah').aggregate(Sum('Battery_pack_qty'))[
                        'Battery_pack_qty__sum']
    V48_200ahPrize = V48_200ah * (
            BatteryPackdetail.objects.filter(Battery_pack='48V 200Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='48V 200Ah').count())
    V48_200ahPUP = V48_200ahPrize/V48_200ah if V48_200ah else 0

    V60_25ah = BatteryPackdetail.objects.filter(Battery_pack='60V 25Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='60V 25Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V60_25ah = V60_25ah - CustomerDetail.objects.filter(Battery_pack='60V 25Ah').aggregate(Sum('Battery_pack_qty'))[
            'Battery_pack_qty__sum']
    V60_25ahPrize = V60_25ah * (
            BatteryPackdetail.objects.filter(Battery_pack='60V 25Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='60V 25Ah').count())
    V60_25ahPUP = V60_25ahPrize/V60_25ah if V60_25ah else 0

    V60_40ah = BatteryPackdetail.objects.filter(Battery_pack='60V 40Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='60V 40Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V60_40ah = V60_40ah - CustomerDetail.objects.filter(Battery_pack='60V 40Ah').aggregate(Sum('Battery_pack_qty'))[
            'Battery_pack_qty__sum']
    V60_40ahPrize = V60_40ah * (
            BatteryPackdetail.objects.filter(Battery_pack='60V 40Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='60V 40Ah').count())
    V60_40ahPUP = V60_40ahPrize/V60_40ah if V60_40ah else 0

    V60_50ah = BatteryPackdetail.objects.filter(Battery_pack='60V 50Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='60V 50Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V60_50ah = V60_50ah - CustomerDetail.objects.filter(Battery_pack='60V 50Ah').aggregate(Sum('Battery_pack_qty'))[
            'Battery_pack_qty__sum']
    V60_50ahPrize = V60_50ah * (
            BatteryPackdetail.objects.filter(Battery_pack='60V 50Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='60V 50Ah').count())
    V60_50ahPUP = V60_50ahPrize/V60_50ah if V60_50ah else 0

    V60_100ah = BatteryPackdetail.objects.filter(Battery_pack='60V 100Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='60V 100Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V60_100ah = V60_100ah - \
                    CustomerDetail.objects.filter(Battery_pack='60V 100Ah').aggregate(Sum('Battery_pack_qty'))[
                        'Battery_pack_qty__sum']
    V60_100ahPrize = V60_100ah * (
            BatteryPackdetail.objects.filter(Battery_pack='60V 100Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='60V 100Ah').count())
    V60_100ahPUP = V60_100ahPrize/V60_100ah if V60_100ah else 0

    V72_25ah = BatteryPackdetail.objects.filter(Battery_pack='72V 25Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='72V 25Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V72_25ah = V72_25ah - CustomerDetail.objects.filter(Battery_pack='72V 25Ah').aggregate(Sum('Battery_pack_qty'))[
            'Battery_pack_qty__sum']
    V72_25ahPrize = V72_25ah * (
            BatteryPackdetail.objects.filter(Battery_pack='72V 25Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='72V 25Ah').count())
    V72_25ahPUP = V72_25ahPrize/V72_25ah if V72_25ah else 0

    V72_40ah = BatteryPackdetail.objects.filter(Battery_pack='72V 40Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='72V 40Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V72_40ah = V72_40ah - CustomerDetail.objects.filter(Battery_pack='72V 40Ah').aggregate(Sum('Battery_pack_qty'))[
            'Battery_pack_qty__sum']
    V72_40ahPrize = V72_40ah * (
            BatteryPackdetail.objects.filter(Battery_pack='72V 40Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='72V 40Ah').count())
    V72_40ahPUP = V72_40ahPrize/V72_40ah if V72_40ah else 0

    V72_50ah = BatteryPackdetail.objects.filter(Battery_pack='72V 50Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='72V 50Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V72_50ah = V72_50ah - CustomerDetail.objects.filter(Battery_pack='72V 50Ah').aggregate(Sum('Battery_pack_qty'))[
            'Battery_pack_qty__sum']
    V72_50ahPrize = V72_50ah * (
            BatteryPackdetail.objects.filter(Battery_pack='72V 50Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='72V 50Ah').count())
    V72_50ahPUP = V72_50ahPrize/V72_50ah if V72_50ah else 0

    V72_100ah = BatteryPackdetail.objects.filter(Battery_pack='72V 100Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='72V 100Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V72_100ah = V72_100ah - \
                    CustomerDetail.objects.filter(Battery_pack='72V 100Ah').aggregate(Sum('Battery_pack_qty'))[
                        'Battery_pack_qty__sum']
    V72_100ahPrize = V72_100ah * (
            BatteryPackdetail.objects.filter(Battery_pack='72V 100Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='72V 100Ah').count())
    V72_100ahPUP = V72_100ahPrize/V72_100ah if V72_100ah else 0

    V72_200ah = BatteryPackdetail.objects.filter(Battery_pack='72V 200Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']
    if CustomerDetail.objects.filter(Battery_pack='72V 200Ah').aggregate(Sum('Battery_pack_qty'))[
        'Battery_pack_qty__sum']:
        V72_200ah = V72_200ah - \
                    CustomerDetail.objects.filter(Battery_pack='72V 200Ah').aggregate(Sum('Battery_pack_qty'))[
                        'Battery_pack_qty__sum']
    V72_200ahPrize = V72_200ah * (
            BatteryPackdetail.objects.filter(Battery_pack='72V 200Ah').aggregate(Sum('Battery_pack_PUP'))[
                'Battery_pack_PUP__sum'] / BatteryPackdetail.objects.filter(Battery_pack='72V 200Ah').count())
    V72_200ahPUP = V72_200ahPrize/V72_200ah if V72_200ah else 0

    # Bike Pack
    bike1 = BikePackdetail.objects.filter(Bike_pack='Bike 1').aggregate(Sum('Bike_pack_qty'))['Bike_pack_qty__sum']
    if CustomerDetail.objects.filter(Bike_pack='Bike 1').aggregate(Sum('Bike_pack_qty'))['Bike_pack_qty__sum']:
        bike1 = bike1 - CustomerDetail.objects.filter(Bike_pack='Bike 1').aggregate(Sum('Bike_pack_qty'))[
            'Bike_pack_qty__sum']
    bike1Prize = bike1 * (
            BikePackdetail.objects.filter(Bike_pack='Bike 1').aggregate(Sum('Bike_pack_PUP'))[
                'Bike_pack_PUP__sum'] / BikePackdetail.objects.filter(Bike_pack='Bike 1').count())
    bike1PUP = bike1Prize/bike1 if bike1 else 0

    bike2 = BikePackdetail.objects.filter(Bike_pack='Bike 2').aggregate(Sum('Bike_pack_qty'))['Bike_pack_qty__sum']
    if CustomerDetail.objects.filter(Bike_pack='Bike 2').aggregate(Sum('Bike_pack_qty'))['Bike_pack_qty__sum']:
        bike2 = bike2 - CustomerDetail.objects.filter(Bike_pack='Bike 2').aggregate(Sum('Bike_pack_qty'))[
            'Bike_pack_qty__sum']
    bike2Prize = bike2 * (
            BikePackdetail.objects.filter(Bike_pack='Bike 2').aggregate(Sum('Bike_pack_PUP'))[
                'Bike_pack_PUP__sum'] / BikePackdetail.objects.filter(Bike_pack='Bike 2').count())
    bike2PUP = bike2Prize/bike2 if bike2 else 0

    bike3 = BikePackdetail.objects.filter(Bike_pack='Bike 3').aggregate(Sum('Bike_pack_qty'))['Bike_pack_qty__sum']
    if CustomerDetail.objects.filter(Bike_pack='Bike 3').aggregate(Sum('Bike_pack_qty'))['Bike_pack_qty__sum']:
        bike3 = bike3 - CustomerDetail.objects.filter(Bike_pack='Bike 3').aggregate(Sum('Bike_pack_qty'))[
            'Bike_pack_qty__sum']
    bike3Prize = bike3 * (
            BikePackdetail.objects.filter(Bike_pack='Bike 3').aggregate(Sum('Bike_pack_PUP'))[
                'Bike_pack_PUP__sum'] / BikePackdetail.objects.filter(Bike_pack='Bike 3').count())
    bike3PUP = bike3Prize/bike3 if bike3 else 0

    bike4 = BikePackdetail.objects.filter(Bike_pack='Bike 4').aggregate(Sum('Bike_pack_qty'))['Bike_pack_qty__sum']
    if CustomerDetail.objects.filter(Bike_pack='Bike 4').aggregate(Sum('Bike_pack_qty'))['Bike_pack_qty__sum']:
        bike4 = bike4 - CustomerDetail.objects.filter(Bike_pack='Bike 4').aggregate(Sum('Bike_pack_qty'))[
            'Bike_pack_qty__sum']
    bike4Prize = bike4 * (
            BikePackdetail.objects.filter(Bike_pack='Bike 4').aggregate(Sum('Bike_pack_PUP'))[
                'Bike_pack_PUP__sum'] / BikePackdetail.objects.filter(Bike_pack='Bike 4').count())
    bike4PUP = bike4Prize/bike4 if bike4 else 0

    # Bike Accessories
    motor1 = BikeAccessorydetail.objects.filter(motor_type='Motor 1').aggregate(Sum('motor_qty'))['motor_qty__sum']
    if CustomerDetail.objects.filter(motor_type='Motor 1').aggregate(Sum('motor_qty'))['motor_qty__sum']:
        motor1 = motor1 - CustomerDetail.objects.filter(motor_type='Motor 1').aggregate(Sum('motor_qty'))[
            'motor_qty__sum']
    motor1Prize = motor1 * (
            BikeAccessorydetail.objects.filter(motor_type='Motor 1').aggregate(Sum('motor_PUP'))[
                'motor_PUP__sum'] / BikeAccessorydetail.objects.filter(motor_type='Motor 1').count())
    motor1PUP = motor1Prize/motor1 if motor1 else 0

    motor2 = BikeAccessorydetail.objects.filter(motor_type='Motor 2').aggregate(Sum('motor_qty'))['motor_qty__sum']
    if CustomerDetail.objects.filter(motor_type='Motor 2').aggregate(Sum('motor_qty'))['motor_qty__sum']:
        motor2 = motor2 - CustomerDetail.objects.filter(motor_type='Motor 2').aggregate(Sum('motor_qty'))[
            'motor_qty__sum']
    motor2Prize = motor2 * (
            BikeAccessorydetail.objects.filter(motor_type='Motor 2').aggregate(Sum('motor_PUP'))[
                'motor_PUP__sum'] / BikeAccessorydetail.objects.filter(motor_type='Motor 2').count())
    motor2PUP = motor2Prize/motor2 if motor2 else 0

    motor3 = BikeAccessorydetail.objects.filter(motor_type='Motor 3').aggregate(Sum('motor_qty'))['motor_qty__sum']
    if CustomerDetail.objects.filter(motor_type='Motor 3').aggregate(Sum('motor_qty'))['motor_qty__sum']:
        motor3 = motor3 - CustomerDetail.objects.filter(motor_type='Motor 3').aggregate(Sum('motor_qty'))[
            'motor_qty__sum']
    motor3Prize = motor3 * (
            BikeAccessorydetail.objects.filter(motor_type='Motor 3').aggregate(Sum('motor_PUP'))[
                'motor_PUP__sum'] / BikeAccessorydetail.objects.filter(motor_type='Motor 3').count())
    motor3PUP = motor3Prize/motor3 if motor3 else 0

    motor4 = BikeAccessorydetail.objects.filter(motor_type='Motor 4').aggregate(Sum('motor_qty'))['motor_qty__sum']
    if CustomerDetail.objects.filter(motor_type='Motor 4').aggregate(Sum('motor_qty'))['motor_qty__sum']:
        motor4 = motor4 - CustomerDetail.objects.filter(motor_type='Motor 4').aggregate(Sum('motor_qty'))[
            'motor_qty__sum']
    motor4Prize = motor4 * (
            BikeAccessorydetail.objects.filter(motor_type='Motor 4').aggregate(Sum('motor_PUP'))[
                'motor_PUP__sum'] / BikeAccessorydetail.objects.filter(motor_type='Motor 4').count())
    motor4PUP = motor4Prize/motor4 if motor4 else 0

    controller1 = BikeAccessorydetail.objects.filter(controller_type='Controller 1').aggregate(Sum('controller_qty'))[
        'controller_qty__sum']
    if CustomerDetail.objects.filter(controller_type='Controller 1').aggregate(Sum('controller_qty'))[
        'controller_qty__sum']:
        controller1 = controller1 - \
                      CustomerDetail.objects.filter(controller_type='Controller 1').aggregate(Sum('controller_qty'))[
                          'controller_qty__sum']
    controller1Prize = controller1 * (
            BikeAccessorydetail.objects.filter(controller_type='Controller 1').aggregate(Sum('controller_PUP'))[
                'controller_PUP__sum'] / BikeAccessorydetail.objects.filter(controller_type='Controller 1').count())
    controller1PUP = controller1Prize/controller1 if controller1 else 0

    controller2 = BikeAccessorydetail.objects.filter(controller_type='Controller 2').aggregate(Sum('controller_qty'))[
        'controller_qty__sum']
    if CustomerDetail.objects.filter(controller_type='Controller 2').aggregate(Sum('controller_qty'))[
        'controller_qty__sum']:
        controller2 = controller2 - \
                      CustomerDetail.objects.filter(controller_type='Controller 2').aggregate(Sum('controller_qty'))[
                          'controller_qty__sum']
    controller2Prize = controller2 * (
            BikeAccessorydetail.objects.filter(controller_type='Controller 2').aggregate(Sum('controller_PUP'))[
                'controller_PUP__sum'] / BikeAccessorydetail.objects.filter(controller_type='Controller 2').count())
    controller2PUP = controller2Prize/controller2 if controller2 else 0

    controller3 = BikeAccessorydetail.objects.filter(controller_type='Controller 3').aggregate(Sum('controller_qty'))[
        'controller_qty__sum']
    if CustomerDetail.objects.filter(controller_type='Controller 3').aggregate(Sum('controller_qty'))[
        'controller_qty__sum']:
        controller3 = controller3 - \
                      CustomerDetail.objects.filter(controller_type='Controller 3').aggregate(Sum('controller_qty'))[
                          'controller_qty__sum']
    controller3Prize = controller3 * (
            BikeAccessorydetail.objects.filter(controller_type='Controller 3').aggregate(Sum('controller_PUP'))[
                'controller_PUP__sum'] / BikeAccessorydetail.objects.filter(controller_type='Controller 3').count())
    controller3PUP = controller3Prize/controller3 if controller3 else 0

    controller4 = BikeAccessorydetail.objects.filter(controller_type='Controller 4').aggregate(Sum('controller_qty'))[
        'controller_qty__sum']
    if CustomerDetail.objects.filter(controller_type='Controller 4').aggregate(Sum('controller_qty'))[
        'controller_qty__sum']:
        controller4 = controller4 - \
                      CustomerDetail.objects.filter(controller_type='Controller 4').aggregate(Sum('controller_qty'))[
                          'controller_qty__sum']
    controller4Prize = controller4 * (
            BikeAccessorydetail.objects.filter(controller_type='Controller 4').aggregate(Sum('controller_PUP'))[
                'controller_PUP__sum'] / BikeAccessorydetail.objects.filter(controller_type='Controller 4').count())
    controller4PUP = controller4Prize/controller4 if controller4 else 0

    throttle = BikeAccessorydetail.objects.aggregate(Sum('throttle'))['throttle__sum']
    if CustomerDetail.objects.aggregate(Sum('throttle'))['throttle__sum']:
        throttle = throttle - CustomerDetail.objects.aggregate(Sum('throttle'))['throttle__sum']
    throttlePrize = throttle * (BikeAccessorydetail.objects.aggregate(Sum('throttle_PUP'))[
                                    'throttle_PUP__sum'] / BikeAccessorydetail.objects.filter(
        throttle__isnull=False).count())
    throttlePUP = throttlePrize/throttle if throttle else 0

    brake = BikeAccessorydetail.objects.aggregate(Sum('brake'))['brake__sum']
    if CustomerDetail.objects.aggregate(Sum('brake'))['brake__sum']:
        brake = brake - CustomerDetail.objects.aggregate(Sum('brake'))['brake__sum']
    brakePrize = brake * (BikeAccessorydetail.objects.aggregate(Sum('brake_PUP'))[
                              'brake_PUP__sum'] / BikeAccessorydetail.objects.filter(brake__isnull=False).count())
    brakePUP = brakePrize/brake if brake else 0

    spokes = BikeAccessorydetail.objects.aggregate(Sum('spokes'))['spokes__sum']
    if CustomerDetail.objects.aggregate(Sum('spokes'))['spokes__sum']:
        spokes = spokes - CustomerDetail.objects.aggregate(Sum('spokes'))['spokes__sum']
    spokesPrize = spokes * (BikeAccessorydetail.objects.aggregate(Sum('spokes_PUP'))[
                                'spokes_PUP__sum'] / BikeAccessorydetail.objects.filter(spokes__isnull=False).count())
    spokesPUP = spokesPrize/spokes if spokes else 0

    # Battery Accessories
    enclosure = BatteryAccessorydetail.objects.aggregate(Sum('enclosure'))['enclosure__sum']
    if CustomerDetail.objects.aggregate(Sum('enclosure'))['enclosure__sum']:
        enclosure = enclosure - CustomerDetail.objects.aggregate(Sum('enclosure'))['enclosure__sum']
    enclosurePrize = enclosure * (BatteryAccessorydetail.objects.aggregate(Sum('enclosure_PUP'))[
                                      'enclosure_PUP__sum'] / BatteryAccessorydetail.objects.filter(
        enclosure__isnull=False).count())
    enclosurePUP = enclosurePrize/enclosure if enclosure else 0

    breaker = BatteryAccessorydetail.objects.aggregate(Sum('breaker'))['breaker__sum']
    if CustomerDetail.objects.aggregate(Sum('breaker'))['breaker__sum']:
        breaker = breaker - CustomerDetail.objects.aggregate(Sum('breaker'))['breaker__sum']
    breakerPrize = breaker * (BatteryAccessorydetail.objects.aggregate(Sum('breaker_PUP'))[
                                  'breaker_PUP__sum'] / BatteryAccessorydetail.objects.filter(
        breaker__isnull=False).count())
    breakerPUP = breakerPrize/breaker if breaker else 0

    display = BatteryAccessorydetail.objects.aggregate(Sum('display'))['display__sum']
    if CustomerDetail.objects.aggregate(Sum('display'))['display__sum']:
        display = display - CustomerDetail.objects.aggregate(Sum('display'))['display__sum']
    displayPrize = display * (BatteryAccessorydetail.objects.aggregate(Sum('display_PUP'))[
                                  'display_PUP__sum'] / BatteryAccessorydetail.objects.filter(
        display__isnull=False).count())
    displayPUP = displayPrize/display if display else 0

    B_Connector = BatteryAccessorydetail.objects.aggregate(Sum('B_Connector'))['B_Connector__sum']
    if CustomerDetail.objects.aggregate(Sum('B_Connector'))['B_Connector__sum']:
        B_Connector = B_Connector - CustomerDetail.objects.aggregate(Sum('B_Connector'))['B_Connector__sum']
    B_ConnectorPrize = enclosure * (BatteryAccessorydetail.objects.aggregate(Sum('B_Connector_PUP'))[
                                        'B_Connector_PUP__sum'] / BatteryAccessorydetail.objects.filter(
        B_Connector__isnull=False).count())
    B_ConnectorPUP = B_ConnectorPrize/B_Connector if B_Connector else 0

    wire = BatteryAccessorydetail.objects.aggregate(Sum('wire'))['wire__sum']
    if CustomerDetail.objects.aggregate(Sum('wire'))['wire__sum']:
        wire = wire - CustomerDetail.objects.aggregate(Sum('wire'))['wire__sum']
    wirePrize = wire * (BatteryAccessorydetail.objects.aggregate(Sum('wire_PUP'))[
                            'wire_PUP__sum'] / BatteryAccessorydetail.objects.filter(wire__isnull=False).count())
    wirePUP = wirePrize/wire if wire else 0

    thimble = BatteryAccessorydetail.objects.aggregate(Sum('thimble'))['thimble__sum']
    if CustomerDetail.objects.aggregate(Sum('thimble'))['thimble__sum']:
        thimble = thimble - CustomerDetail.objects.aggregate(Sum('thimble'))['thimble__sum']
    thimblePrize = thimble * (BatteryAccessorydetail.objects.aggregate(Sum('thimble_PUP'))[
                                  'thimble_PUP__sum'] / BatteryAccessorydetail.objects.filter(
        thimble__isnull=False).count())
    thimblePUP = thimblePrize/thimble if thimble else 0

    context = {
        'L6_ah': L6_ah, 'L6_ahPrize': L6_ahPrize, 'L6_ahPUP': L6_ahPUP,
        'L20_ah': L20_ah, 'L20_ahPrize': L20_ahPrize, 'L20_ahPUP': L20_ahPUP,
        'L25_ah': L25_ah, 'L25_ahPrize': L25_ahPrize, 'L25_ahPUP': L25_ahPUP,
        'L40_ah': L40_ah, 'L40_ahPrize': L40_ahPrize, 'L40_ahPUP': L40_ahPUP,
        'L50_ah': L50_ah, 'L50_ahPrize': L50_ahPrize, 'L50_ahPUP': L50_ahPUP,
        'L105_ah': L105_ah, 'L105_ahPrize': L105_ahPrize, 'L105_ahPUP': L105_ahPUP,
        'L205_ah': L205_ah, 'L205_ahPrize': L205_ahPrize, 'L205_ahPUP': L205_ahPUP,

        'S4_20ah': S4_20ah, 'S4_20ahPrize': S4_20ahPrize, 'S4_20ahPUP': S4_20ahPUP,
        'S4_50ah': S4_50ah, 'S4_50ahPrize': S4_50ahPrize, 'S4_50ahPUP': S4_50ahPUP,
        'S4_100ah': S4_100ah, 'S4_100ahPrize': S4_100ahPrize, 'S4_100ahPUP': S4_100ahPUP,
        'S4_200ah': S4_200ah, 'S4_200ahPrize': S4_200ahPrize, 'S4_200ahPUP': S4_200ahPUP,
        'S4_S100ah': S4_S100ah, 'S4_S100ahPrize': S4_S100ahPrize, 'S4_S100ahPUP': S4_S100ahPUP,
        'S4_S200ah': S4_S200ah, 'S4_S200ahPrize': S4_S200ahPrize, 'S4_S200ahPUP': S4_S200ahPUP,
        'S8_50ah': S8_50ah, 'S8_50ahPrize': S8_50ahPrize, 'S8_50ahPUP': S8_50ahPUP,
        'S8_100ah': S8_100ah, 'S8_100ahPrize': S8_100ahPrize, 'S8_100ahPUP': S8_100ahPUP,
        'S8_S100ah': S8_S100ah, 'S8_S100ahPrize': S8_S100ahPrize, 'S8_S100ahPUP': S8_S100ahPUP,
        'S8_200ah': S8_200ah, 'S8_200ahPrize': S8_200ahPrize, 'S8_200ahPUP': S8_200ahPUP,
        'S15_50ah': S15_50ah, 'S15_50ahPrize': S15_50ahPrize, 'S15_50ahPUP': S15_50ahPUP,
        'S15_100ah': S15_100ah, 'S15_100ahPrize': S15_100ahPrize, 'S15_100ahPUP': S15_100ahPUP,
        'S15_200ah': S15_200ah, 'S15_200ahPrize': S15_200ahPrize, 'S15_200ahPUP': S15_200ahPUP,
        'S16_50ah': S16_50ah, 'S16_50ahPrize': S16_50ahPrize, 'S16_50ahPUP': S16_50ahPUP,
        'S16_100ah': S16_100ah, 'S16_100ahPrize': S16_100ahPrize, 'S16_100ahPUP': S16_100ahPUP,
        'S16_200ah': S16_200ah, 'S16_200ahPrize': S16_200ahPrize, 'S16_200ahPUP': S16_200ahPUP,
        'S19_60ah': S19_60ah, 'S19_60ahPrize': S19_60ahPrize, 'S19_60ahPUP': S19_60ahPUP,
        'S19_100ah': S19_100ah, 'S19_100ahPrize': S19_100ahPrize, 'S19_100ahPUP': S19_100ahPUP,
        'S20_60ah': S20_60ah, 'S20_60ahPrize': S20_60ahPrize, 'S20_60ahPUP': S20_60ahPUP,
        'S20_100ah': S20_100ah, 'S20_100ahPrize': S20_100ahPrize, 'S20_100ahPUP': S20_100ahPUP,
        'S23_50ah': S23_50ah, 'S23_50ahPrize': S23_50ahPrize, 'S23_50ahPUP': S23_50ahPUP,
        'S23_100ah': S23_100ah, 'S23_100ahPrize': S23_100ahPrize, 'S23_100ahPUP': S23_100ahPUP,
        'S24_50ah': S24_50ah, 'S24_50ahPrize': S24_50ahPrize, 'S24_50ahPUP': S24_50ahPUP,
        'S24_100ah': S24_100ah, 'S24_100ahPrize': S24_100ahPrize, 'S24_100ahPUP': S24_100ahPUP,

        'V12_25ah': V12_25ah, 'V12_25ahPrize': V12_25ahPrize, 'V12_25ahPUP': V12_25ahPUP,
        'V12_40ah': V12_40ah, 'V12_40ahPrize': V12_40ahPrize, 'V12_40ahPUP': V12_40ahPUP,
        'V12_50ah': V12_50ah, 'V12_50ahPrize': V12_50ahPrize, 'V12_50ahPUP': V12_50ahPUP,
        'V12_100ah': V12_100ah, 'V12_100ahPrize': V12_100ahPrize, 'V12_100ahPUP': V12_100ahPUP,
        'V12_200ah': V12_200ah, 'V12_200ahPrize': V12_200ahPrize, 'V12_200ahPUP': V12_200ahPUP,
        'V24_50ah': V24_50ah, 'V24_50ahPrize': V24_50ahPrize, 'V24_50ahPUP': V24_50ahPUP,
        'V24_100ah': V24_100ah, 'V24_100ahPrize': V24_100ahPrize, 'V24_100ahPUP': V24_100ahPUP,
        'V24_200ah': V24_200ah, 'V24_200ahPrize': V24_200ahPrize, 'V24_200ahPUP': V24_200ahPUP,
        'V48_25ah': V48_25ah, 'V48_25ahPrize': V48_25ahPrize, 'V48_25ahPUP': V48_25ahPUP,
        'V48_40ah': V48_40ah, 'V48_40ahPrize': V48_40ahPrize, 'V48_40ahPUP': V48_40ahPUP,
        'V48_50ah': V48_50ah, 'V48_50ahPrize': V48_50ahPrize, 'V48_50ahPUP': V48_50ahPUP,
        'V48_100ah': V48_100ah, 'V48_100ahPrize': V48_100ahPrize, 'V48_100ahPUP': V48_100ahPUP,
        'V48_200ah': V48_200ah, 'V48_200ahPrize': V48_200ahPrize, 'V48_200ahPUP': V48_200ahPUP,
        'V60_25ah': V60_25ah, 'V60_25ahPrize': V60_25ahPrize, 'V60_25ahPUP': V60_25ahPUP,
        'V60_40ah': V60_40ah, 'V60_40ahPrize': V60_40ahPrize, 'V60_40ahPUP': V60_40ahPUP,
        'V60_50ah': V60_50ah, 'V60_50ahPrize': V60_50ahPrize, 'V60_50ahPUP': V60_50ahPUP,
        'V60_100ah': V60_100ah, 'V60_100ahPrize': V60_100ahPrize, 'V60_100ahPUP': V60_100ahPUP,
        'V72_25ah': V72_25ah, 'V72_25ahPrize': V72_25ahPrize, 'V72_25ahPUP': V72_25ahPUP,
        'V72_40ah': V72_40ah, 'V72_40ahPrize': V72_40ahPrize, 'V72_40ahPUP': V72_40ahPUP,
        'V72_50ah': V72_50ah, 'V72_50ahPrize': V72_50ahPrize, 'V72_50ahPUP': V72_50ahPUP,
        'V72_100ah': V72_100ah, 'V72_100ahPrize': V72_100ahPrize, 'V72_100ahPUP': V72_100ahPUP,
        'V72_200ah': V72_200ah, 'V72_200ahPrize': V72_200ahPrize, 'V72_200ahPUP': V72_200ahPUP,

        'bike1': bike1, 'bike1Prize': bike1Prize, 'bike1PUP': bike1PUP,
        'bike2': bike2, 'bike2Prize': bike2Prize, 'bike2PUP': bike2PUP,
        'bike3': bike3, 'bike3Prize': bike3Prize, 'bike3PUP': bike3PUP,
        'bike4': bike4, 'bike4Prize': bike4Prize, 'bike4PUP': bike4PUP,

        'motor1': motor1, 'motor1Prize': motor1Prize, 'motor1PUP': motor1PUP,
        'motor2': motor2, 'motor2Prize': motor2Prize, 'motor2PUP': motor2PUP,
        'motor3': motor3, 'motor3Prize': motor3Prize, 'motor3PUP': motor3PUP,
        'motor4': motor4, 'motor4Prize': motor4Prize, 'motor4PUP': motor4PUP,
        'controller1': controller1, 'controller1Prize': controller1Prize, 'controller1PUP': controller1PUP,
        'controller2': controller2, 'controller2Prize': controller2Prize, 'controller2PUP': controller2PUP,
        'controller3': controller3, 'controller3Prize': controller3Prize, 'controller3PUP': controller3PUP,
        'controller4': controller4, 'controller4Prize': controller4Prize, 'controller4PUP': controller4PUP,
        'throttle': throttle, 'throttlePrize': throttlePrize, 'throttlePUP': throttlePUP,
        'brake': brake, 'brakePrize': brakePrize, 'brakePUP': brakePUP,
        'spokes': spokes, 'spokesPrize': spokesPrize, 'spokesPUP': spokesPUP,

        'enclosure': enclosure, 'enclosurePrize': enclosurePrize, 'enclosurePUP': enclosurePUP,
        'breaker': breaker, 'breakerPrize': breakerPrize, 'breakerPUP': breakerPUP,
        'display': display, 'displayPrize': displayPrize, 'displayPUP': displayPUP,
        'B_Connector': B_Connector, 'B_ConnectorPrize': B_ConnectorPrize, 'B_ConnectorPUP': B_ConnectorPUP,
        'wire': wire, 'wirePrize': wirePrize, 'wirePUP': wirePUP,
        'thimble': thimble, 'thimblePrize': thimblePrize, 'thimblePUP': thimblePUP,
    }
    return render(request, "storedetail.html", context)


def device_data_view(request, deivce_data=''):
    if request.method == 'POST':
        port = request.POST['port']
        port = port.split().pop(0)
        baud_rate = request.POST['baud_rate']
        ser = serial.Serial(port, baud_rate)
        time.sleep(1)
        # serial.write(str1.encode())
        if ser.isOpen():
            ser.close()
        ser.open()
        ser.isOpen()
        # time.sleep(1)
        while 1:
            try:
                str2 = "getdata"
                ser.write(str2.encode())
                deivce_data = ser.readline()
                deivce_data = deivce_data.decode('utf-8')
                deivce_data = deivce_data.split('#')
                time.sleep(1)
                if ser.isOpen():
                    ser.close()
                    break
            except:
                break
        ser.close()

    context = {
        'ports': ports,
        'deivce_data': deivce_data,
        'battery': batt
    }
    return render(request, "devicedata.html", context)


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect("index")
        elif request.user.is_authenticated:
            messages.info(request, 'User already logged in. Logout First!')
            return redirect("login")
        else:
            messages.error(request, 'Credential does not match. Please try again!')
            return redirect("login")

    return render(request, "login.html")


# @login_required()
def logout(request):
    django_logout(request)
    return redirect("index")


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]
        if User.objects.filter(username=username):
            messages.warning(request, "User Name already exists. Please Try Again!")
            return redirect("register")
        elif User.objects.filter(email=email):
            messages.warning(request, "Email already exists. Please Try Again!")
            return redirect("register")
        elif pass1 != pass2:
            messages.warning(request, "Your Password does not Match. Please Try Again!")
            return redirect("register")
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Your Account Created Successfully")

        ''' subject = "Confirmation Message"
        message = "Hello"+myuser.first_name+"\n Your account has been successfully created and this is confirmation message to you"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True) '''

        return redirect("login")

    return render(request, "register.html")


def forgotpassword_view(request):
    return render(request, "forgot-password.html")


def warning_view(request):
    context = {'btinfo': btinfo}
    for bat1 in btinfo:
        info = "Your volatge is %s than %s volts against id = %s. For detail <a href='/battery/%s/'>Click Here</a>"
        if 30 >= bat1.MinVolt > 20:
            messages.info(request, mark_safe(info % ("less", 30, bat1.id, bat1.id)))
        elif 20 >= bat1.MinVolt > 10:
            messages.info(request, mark_safe(info % ("less", 20, bat1.id, bat1.id)))
        elif 10 >= bat1.MinVolt > 5:
            messages.info(request, mark_safe(info % ("less", 10, bat1.id, bat1.id)))
        elif 5 >= bat1.MinVolt >= 0:
            messages.info(request, mark_safe(info % ("less", 5, bat1.id, bat1.id)))
        elif bat1.MaxVolt > 250:
            messages.warning(request, mark_safe(info % ("greater", 250, bat1.id, bat1.id)))
    return render(request, "warning.html", context)


# @login_required()
def addcustomer_view(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        taxamount = request.POST.getlist('taxamount')
        if taxamount == ['0.17']:
            form.instance.tax = 0.17
        else:
            form.instance.tax = 0
        form.save()

    activeuser = request.user.first_name
    if activeuser == "":
        activeuser = request.user

    context = {
        'form': form,
        'celltype': Cell_Type,
        'bmstype': BMS_Type,
        'batterypack': Battery_pack,
        'bikepack': Bike_pack,
        'motor': motor_type,
        'controller': controller_type,
        'paymenttype': payment_type,
        'activeuser': activeuser,
    }
    return render(request, "customer.html", context)


# @login_required()
def customer_view(request):
    Customer_Detail = CustomerDetail.objects.all()
    context = {
        'Customer_Detail': Customer_Detail
    }
    return render(request, "customerdetail.html", context)


# @login_required()
def customerprint_view(request, id):
    Customer = CustomerDetail.objects.get(id=id)
    if Customer.Cell_qty:
        Cell = Customer.Cell_qty * Customer.Cell_pup
    else:
        Cell = 0
    if Customer.Cell_qty1:
        Cell1 = Customer.Cell_qty1 * Customer.Cell_pup1
    else:
        Cell1 = 0
    if Customer.Cell_qty2:
        Cell2 = Customer.Cell_qty2 * Customer.Cell_pup2
    else:
        Cell2 = 0
    if Customer.Cell_qty3:
        Cell3 = Customer.Cell_qty3 * Customer.Cell_pup3
    else:
        Cell3 = 0
    if Customer.Cell_qty4:
        Cell4 = Customer.Cell_qty4 * Customer.Cell_pup4
    else:
        Cell4 = 0
    if Customer.BMS_qty:
        BMS = Customer.BMS_qty * Customer.BMS_pup
    else:
        BMS = 0
    if Customer.BMS_qty1:
        BMS1 = Customer.BMS_qty1 * Customer.BMS_pup1
    else:
        BMS1 = 0
    if Customer.BMS_qty2:
        BMS2 = Customer.BMS_qty2 * Customer.BMS_pup2
    else:
        BMS2 = 0
    if Customer.Battery_pack_qty:
        BatteryPack = Customer.Battery_pack_qty * Customer.Battery_pack_pup
    else:
        BatteryPack = 0
    if Customer.Bike_pack_qty:
        BikePack = Customer.Bike_pack_qty * Customer.Bike_pack_pup
    else:
        BikePack = 0
    if Customer.motor_qty:
        motor = Customer.motor_qty * Customer.motor_pup
    else:
        motor = 0
    if Customer.controller_qty:
        controller = Customer.controller_qty * Customer.controller_pup
    else:
        controller = 0
    if Customer.throttle:
        throttle = Customer.throttle * Customer.throttle_pup
    else:
        throttle = 0
    if Customer.brake:
        brake = Customer.brake * Customer.brake_pup
    else:
        brake = 0
    if Customer.spokes:
        spokes = Customer.spokes * Customer.spokes_pup
    else:
        spokes = 0
    if Customer.enclosure:
        enclosure = Customer.enclosure * Customer.enclosure_pup
    else:
        enclosure = 0
    if Customer.breaker:
        breaker = Customer.breaker * Customer.breaker_pup
    else:
        breaker = 0
    if Customer.display:
        display = Customer.display * Customer.display_pup
    else:
        display = 0
    if Customer.B_Connector:
        B_Connector = Customer.B_Connector * Customer.B_Connector_pup
    else:
        B_Connector = 0
    if Customer.wire:
        wire = Customer.wire * Customer.wire_pup
    else:
        wire = 0
    if Customer.thimble:
        thimble = Customer.thimble * Customer.thimble_pup
    else:
        thimble = 0

    Price = Cell + Cell1 + Cell2 + Cell3 + Cell4 + BMS + BMS1 + BMS2 + BatteryPack + BikePack + motor + controller + \
            throttle + brake + spokes + enclosure + breaker + display + B_Connector + wire + thimble

    if Customer.tax:
        Tax = Price * Customer.tax
    else:
        Tax = 0
    if Customer.otheramount:
        Other = Customer.otheramount
    else:
        Other = 0

    Total = Price + Tax + Other

    context = {
        'Customer': Customer,
        'Cell': Cell,
        'Cell1': Cell1,
        'Cell2': Cell2,
        'Cell3': Cell3,
        'Cell4': Cell4,
        'BMS': BMS,
        'BMS1': BMS1,
        'BMS2': BMS2,
        'BatteryPack': BatteryPack,
        'BikePack': BikePack,
        'Motor': motor,
        'Controller': controller,
        'Throttle': throttle,
        'Brake': brake,
        'Spokes': spokes,
        'Enclosure': enclosure,
        'Breaker': breaker,
        'Display': display,
        'B_Connector': B_Connector,
        'Wire': wire,
        'Thimble': thimble,
        'Price': Price,
        'Tax': Tax,
        'Other': Other,
        'Total': Total,
    }
    return render(request, "customerprint.html", context)


def customerupdate_view(request, id):
    customer = CustomerDetail.objects.get(id=id)

    activeuser = request.user.first_name
    if activeuser == "":
        activeuser = request.user

    context = {
        'customer': customer,
        'celltype': Cell_Type,
        'bmstype': BMS_Type,
        'batterypack': Battery_pack,
        'bikepack': Bike_pack,
        'motor': motor_type,
        'controller': controller_type,
        'paymenttype': payment_type,
        'activeuser': activeuser,
    }

    return render(request, "customerupdate.html", context)


# @login_required()
def customerupdaterecord(request, id):
    if request.method == "POST":
        customer = CustomerDetail.objects.get(id=id)
        Ship_No = request.POST['Ship_No']
        Cell_Type = request.POST['Cell_Type']
        Cell_qty = request.POST['Cell_qty']
        Cell_pup = request.POST['Cell_pup']
        if customer.Cell_qty1 or request.POST['Cell_qty1']:
            Cell_Type1 = request.POST['Cell_Type1']
            Cell_qty1 = request.POST['Cell_qty1']
            Cell_pup1 = request.POST['Cell_pup1']
        if customer.Cell_qty2 or request.POST['Cell_qty2']:
            Cell_Type2 = request.POST['Cell_Type2']
            Cell_qty2 = request.POST['Cell_qty2']
            Cell_pup2 = request.POST['Cell_pup2']
        if customer.Cell_qty3 or request.POST['Cell_qty3']:
            Cell_Type3 = request.POST['Cell_Type3']
            Cell_qty3 = request.POST['Cell_qty3']
            Cell_pup3 = request.POST['Cell_pup3']
        if customer.Cell_qty4 or request.POST['Cell_qty4']:
            Cell_Type4 = request.POST['Cell_Type4']
            Cell_qty4 = request.POST['Cell_qty4']
            Cell_pup4 = request.POST['Cell_pup4']
        BMS_Type = request.POST['BMS_Type']
        BMSType = request.POST['BMSType']
        BMS_qty = request.POST['BMS_qty']
        BMS_pup = request.POST['BMS_pup']
        if customer.BMS_qty1 or request.POST['BMS_qty1']:
            BMS_Type1 = request.POST['BMS_Type1']
            BMSType1 = request.POST['BMSType1']
            BMS_qty1 = request.POST['BMS_qty1']
            BMS_pup1 = request.POST['BMS_pup1']
        if customer.BMS_qty2 or request.POST['BMSType2']:
            BMS_Type2 = request.POST['BMS_Type2']
            BMSType2 = request.POST['BMSType2']
            BMS_qty2 = request.POST['BMS_qty2']
            BMS_pup2 = request.POST['BMS_pup2']
        Battery_pack = request.POST['Battery_pack']
        Battery_pack_qty = request.POST['Battery_pack_qty']
        Battery_pack_pup = request.POST['Battery_pack_pup']
        Bike_pack = request.POST['Bike_pack']
        Bike_pack_qty = request.POST['Bike_pack_qty']
        Bike_pack_pup = request.POST['Bike_pack_pup']
        motor_type = request.POST['motor_type']
        motor_qty = request.POST['motor_qty']
        motor_pup = request.POST['motor_pup']
        controller_type = request.POST['controller_type']
        controller_qty = request.POST['controller_qty']
        controller_pup = request.POST['controller_pup']
        throttle = request.POST['throttle']
        throttle_pup = request.POST['throttle_pup']
        brake = request.POST['brake']
        brake_pup = request.POST['brake_pup']
        spokes = request.POST['spokes']
        spokes_pup = request.POST['spokes_pup']
        enclosure = request.POST['enclosure']
        enclosure_pup = request.POST['enclosure_pup']
        breaker = request.POST['breaker']
        breaker_pup = request.POST['breaker_pup']
        display = request.POST['display']
        display_pup = request.POST['display_pup']
        B_Connector = request.POST['B_Connector']
        B_Connector_pup = request.POST['B_Connector_pup']
        wire = request.POST['wire']
        wire_pup = request.POST['wire_pup']
        thimble = request.POST['thimble']
        thimble_pup = request.POST['thimble_pup']
        customer_name = request.POST['customer_name']
        customer_number = request.POST['customer_number']
        customer_type = request.POST['customer_type']
        customer_use = request.POST['customer_use']
        customer_address = request.POST['customer_address']
        payment_type = request.POST['payment_type']
        delivery_type = request.POST['delivery_type']
        otheramount = request.POST['otheramount']
        Description = request.POST['Description']
        taxamount = request.POST.getlist('taxamount')
        if taxamount == ['0.17']:
            customer.tax = 0.17
        else:
            customer.tax = 0
        # price = Cell + BMS + BatteryPack + BikePack + motor + controller + throttlee + brakee + spokess + \
        #         enclosuree + breakerr + displayy + B_Connectorr + wiree + thimblee + otheramount

        customer.Ship_No = Ship_No
        customer.Cell_Type = Cell_Type
        customer.Cell_qty = float(Cell_qty)
        customer.Cell_pup = float(Cell_pup)
        if customer.Cell_qty1 or request.POST['Cell_qty1']:
            customer.Cell_Type1 = Cell_Type1
            customer.Cell_qty1 = float(Cell_qty1)
            customer.Cell_pup1 = float(Cell_pup1)
        if customer.Cell_qty2 or request.POST['Cell_qty2']:
            customer.Cell_Type2 = Cell_Type2
            customer.Cell_qty2 = float(Cell_qty2)
            customer.Cell_pup2 = float(Cell_pup2)
        if customer.Cell_qty3 or request.POST['Cell_qty3']:
            customer.Cell_Type3 = Cell_Type3
            customer.Cell_qty3 = float(Cell_qty3)
            customer.Cell_pup3 = float(Cell_pup3)
        if customer.Cell_qty4 or request.POST['Cell_qty4']:
            customer.Cell_Type4 = Cell_Type4
            customer.Cell_qty4 = float(Cell_qty4)
            customer.Cell_pup4 = float(Cell_pup4)
        customer.BMS_Type = BMS_Type
        customer.BMSType = BMSType
        customer.BMS_qty = float(BMS_qty)
        customer.BMS_pup = float(BMS_pup)
        if customer.BMS_qty1 or request.POST['BMS_qty1']:
            customer.BMS_Type1 = BMS_Type1
            customer.BMSType1 = BMSType1
            customer.BMS_qty1 = float(BMS_qty1)
            customer.BMS_pup1 = float(BMS_pup1)

        if customer.BMS_qty2 or request.POST['BMS_qty2']:
            customer.BMS_Type2 = BMS_Type2
            customer.BMSType2 = BMSType2
            customer.BMS_qty2 = float(BMS_qty2)
            customer.BMS_pup2 = float(BMS_pup2)
        customer.Battery_pack = Battery_pack
        customer.Battery_pack_qty = float(Battery_pack_qty)
        customer.Battery_pack_pup = float(Battery_pack_pup)
        customer.Bike_pack = Bike_pack
        customer.Bike_pack_qty = float(Bike_pack_qty)
        customer.Bike_pack_pup = float(Bike_pack_pup)
        customer.motor_type = motor_type
        customer.motor_qty = float(motor_qty)
        customer.motor_pup = float(motor_pup)
        customer.controller_type = controller_type
        customer.controller_qty = float(controller_qty)
        customer.controller_pup = float(controller_pup)
        customer.throttle = float(throttle)
        customer.throttle_pup = float(throttle_pup)
        customer.brake = float(brake)
        customer.brake_pup = float(brake_pup)
        customer.spokes = float(spokes)
        customer.spokes_pup = float(spokes_pup)
        customer.enclosure = float(enclosure)
        customer.enclosure_pup = float(enclosure_pup)
        customer.breaker = float(breaker)
        customer.breaker_pup = float(breaker_pup)
        customer.display = float(display)
        customer.display_pup = float(display_pup)
        customer.B_Connector = float(B_Connector)
        customer.B_Connector_pup = float(B_Connector_pup)
        customer.wire = float(wire)
        customer.wire_pup = float(wire_pup)
        customer.thimble = float(thimble)
        customer.thimble_pup = float(thimble_pup)
        customer.customer_name = customer_name
        customer.customer_number = customer_number
        customer.customer_type = customer_type
        customer.customer_use = customer_use
        customer.customer_address = customer_address
        if otheramount:
            customer.otheramount = float(otheramount)
        else:
            customer.otheramount = None
        customer.payment_type = payment_type
        customer.delivery_type = delivery_type
        customer.Description = Description
        customer.save()

        return redirect("customer")


def locations_view(request):
    xyz = Btdetail.objects.get(id=1)
    return render(request, "location.html", {'xyz': xyz})


def other_view(request, btinfo_id):
    try:
        btinfo = Btdetail.objects.get(pk=btinfo_id)
    except Btdetail.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'other.html', {'btinfo': btinfo})


# @login_required()
def update_view(request, id):
    battery = Btdetail.objects.get(id=id)
    context = {
        'battery': battery,
        'batteries': Battery_Type,
    }
    return render(request, 'updaterecord.html', context)


# @login_required()
def updaterecord(request, id):
    if request.method == "POST":
        member = Btdetail.objects.get(id=id)
        BatType = request.POST['BatType']
        MaxVolt = request.POST['MaxVolt']
        MinVolt = request.POST['MinVolt']
        MaxAmp = request.POST['MaxAmp']
        MinAmp = request.POST['MinAmp']
        SCMaxVolt = request.POST['SCMaxVolt']
        SCMinVolt = request.POST['SCMinVolt']
        Temp = request.POST['Temp']
        Manf_ID = request.POST['Manf_ID']
        Latitude = request.POST['Latitude']
        Longitude = request.POST['Longitude']
        member.BatType = BatType
        member.MaxVolt = MaxVolt
        member.MinVolt = MinVolt
        member.MaxAmp = MaxAmp
        member.MinAmp = MinAmp
        member.SCMaxVolt = SCMaxVolt
        member.SCMinVolt = SCMinVolt
        member.Temp = Temp
        member.Manf_ID = Manf_ID
        member.Latitude = Latitude
        member.Longitude = Longitude
        member.save()

        return redirect("charger")


# @login_required()
def updatecell_view(request, id):
    Cell = Celldetail.objects.get(id=id)
    context = {
        'Cell': Cell,
        'Cell_Typee': Cell_Type,
    }
    return render(request, 'updatecell.html', context)


# @login_required()
def updatecellrecord(request, id):
    if request.method == "POST":
        member = Celldetail.objects.get(id=id)
        Cell_Type = request.POST['Cell_Type']
        Cell_qty = request.POST['Cell_qty']
        Cell_price = request.POST['Cell_price']
        CellInvoiceNo = request.POST['CellInvoiceNo']
        CellDescription = request.POST['CellDescription']
        member.Cell_Type = Cell_Type
        member.Cell_qty = float(Cell_qty)
        member.Cell_price = float(Cell_price)
        member.CellInvoiceNo = CellInvoiceNo
        member.CellDescription = CellDescription
        member.save()

        return redirect("inventory")


# @login_required()
def updatebms_view(request, id):
    bms = BMSdetail.objects.get(id=id)
    context = {
        'bms': bms,
        'bmss': BMS_Type,
    }
    return render(request, 'updatebms.html', context)


# @login_required()
def updatebmsrecord(request, id):
    if request.method == "POST":
        member = BMSdetail.objects.get(id=id)
        BMS_Type = request.POST['BMS_Type']
        BMSType = request.POST['BMSType']
        BMS_qty = request.POST['BMS_qty']
        BMS_price = request.POST['BMS_price']
        BMSInvoiceNo = request.POST['BMSInvoiceNo']
        BMSDescription = request.POST['BMSDescription']
        member.BMS_Type = BMS_Type
        member.BMSType = BMSType
        member.BMS_qty = float(BMS_qty)
        member.BMS_price = float(BMS_price)
        member.BMSInvoiceNo = BMSInvoiceNo
        member.BMSDescription = BMSDescription
        member.save()

        return redirect("inventory")


# @login_required()
def updatebattery_view(request, id):
    battery = BatteryPackdetail.objects.get(id=id)
    context = {
        'battery': battery,
        'batteries': Battery_pack,
    }
    return render(request, 'updatebattery.html', context)


# @login_required()
def updatebatteryrecord(request, id):
    if request.method == "POST":
        member = BatteryPackdetail.objects.get(id=id)
        Battery_pack = request.POST['Battery_pack']
        Battery_pack_qty = request.POST['Battery_pack_qty']
        Battery_pack_price = request.POST['Battery_pack_price']
        BatteryInvoiceNo = request.POST['BatteryInvoiceNo']
        BatteryDescription = request.POST['BatteryDescription']
        member.Battery_pack = Battery_pack
        member.Battery_pack_qty = float(Battery_pack_qty)
        member.Battery_pack_price = float(Battery_pack_price)
        member.BatteryInvoiceNo = BatteryInvoiceNo
        member.BatteryDescription = BatteryDescription
        member.save()

        return redirect("inventory")


# @login_required()
def updatebike_view(request, id):
    bike = BikePackdetail.objects.get(id=id)
    context = {
        'bike': bike,
        'biketype': Bike_pack,
    }
    return render(request, 'updatebike.html', context)


# @login_required()
def updatebikerecord(request, id):
    if request.method == "POST":
        member = BikePackdetail.objects.get(id=id)
        Bike_pack = request.POST['Bike_pack']
        Bike_pack_qty = request.POST['Bike_pack_qty']
        Bike_pack_price = request.POST['Bike_pack_price']
        BikeInvoiceNo = request.POST['BikeInvoiceNo']
        BikeDescription = request.POST['BikeDescription']
        member.Bike_pack = Bike_pack
        member.Bike_pack_qty = float(Bike_pack_qty)
        member.Bike_pack_price = float(Bike_pack_price)
        member.BikeInvoiceNo = BikeInvoiceNo
        member.BikeDescription = BikeDescription
        member.save()

        return redirect("inventory")


# @login_required()
def updateBikeAccess_view(request, id):
    bike = BikeAccessorydetail.objects.get(id=id)
    context = {
        'bike': bike,
        'motor': motor_type,
        'controller': controller_type,
    }
    return render(request, 'updateBikeAccess.html', context)


# @login_required()
def updateBikeAccess(request, id):
    if request.method == "POST":
        member = BikeAccessorydetail.objects.get(id=id)
        motor_type = request.POST['motor_type']
        motor_qty = request.POST['motor_qty']
        motor_price = request.POST['motor_price']
        controller_type = request.POST['controller_type']
        controller_qty = request.POST['controller_qty']
        controller_price = request.POST['controller_price']
        throttle = request.POST['throttle']
        throttle_price = request.POST['throttle_price']
        brake = request.POST['brake']
        brake_price = request.POST['brake_price']
        spokes = request.POST['spokes']
        spokes_price = request.POST['spokes_price']
        Bike_InvoiceNo = request.POST['Bike_InvoiceNo']
        Bike_Description = request.POST['Bike_Description']
        member.motor_type = motor_type
        if motor_qty == "":
            member.motor_qty = motor_qty
            member.motor_price = motor_price
        else:
            member.motor_qty = float(motor_qty)
            member.motor_price = float(motor_price)
        member.controller_type = controller_type
        if controller_qty == "":
            member.controller_qty = controller_qty
            member.controller_price = controller_price
        else:
            member.controller_qty = float(controller_qty)
            member.controller_price = float(controller_price)
        if throttle == "":
            member.throttle = None
            member.throttle_price = None
        else:
            member.throttle = float(throttle)
            member.throttle_price = float(throttle_price)
        if brake == "":
            member.brake = None
            member.brake_price = None
        else:
            member.brake = float(brake)
            member.brake_price = float(brake_price)
        if spokes == "":
            member.spokes = None
            member.spokes_price = None
        else:
            member.spokes = float(spokes)
            member.spokes_price = float(spokes_price)
        member.Bike_InvoiceNo = Bike_InvoiceNo
        member.Bike_Description = Bike_Description
        member.save()

        return redirect("inventory")


# @login_required()
def updateBatteryAccess_view(request, id):
    battery = BatteryAccessorydetail.objects.get(id=id)
    context = {
        'battery': battery,
    }
    return render(request, 'updateBatteryAccess.html', context)


# @login_required()
def updateBatteryAccess(request, id):
    if request.method == "POST":
        member = BatteryAccessorydetail.objects.get(id=id)
        enclosure = request.POST['enclosure']
        enclosure_price = request.POST['enclosure_price']
        breaker = request.POST['breaker']
        breaker_price = request.POST['breaker_price']
        display = request.POST['display']
        display_price = request.POST['display_price']
        B_Connector = request.POST['B_Connector']
        B_Connector_price = request.POST['B_Connector_price']
        wire = request.POST['wire']
        wire_price = request.POST['wire_price']
        thimble = request.POST['thimble']
        thimble_price = request.POST['thimble_price']
        Battery_InvoiceNo = request.POST['Battery_InvoiceNo']
        Battery_Description = request.POST['Battery_Description']
        if enclosure == "":
            member.enclosure = None
            member.enclosure_price = None
        else:
            member.enclosure = float(enclosure)
            member.enclosure_price = float(enclosure_price)
        if breaker == "":
            member.breaker = None
            member.breaker_price = None
        else:
            member.breaker = float(breaker)
            member.breaker_price = float(breaker_price)
        if display == "":
            member.display = None
            member.display_price = None
        else:
            member.display = float(display)
            member.display_price = float(display_price)
        if B_Connector == "":
            member.B_Connector = None
            member.B_Connector_price = None
        else:
            member.B_Connector = float(B_Connector)
            member.B_Connector_price = float(B_Connector_price)
        if wire == "":
            member.wire = None
            member.wire_price = None
        else:
            member.wire = float(wire)
            member.wire_price = float(wire_price)
        if thimble == "":
            member.thimble = None
            member.thimble_price = None
        else:
            member.thimble = float(thimble)
            member.thimble_price = float(thimble_price)
        member.Battery_InvoiceNo = Battery_InvoiceNo
        member.Battery_Description = Battery_Description
        member.save()

        return redirect("inventory")
