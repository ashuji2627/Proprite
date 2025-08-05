from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def manage(request):
    return render(request,'manage.html')

def block_inventory(request):
    return render(request,'block_inventory.html')

def blocked_flats(request):
    return render(request,'blocked_flats.html')

def booked_flats(request):
    return render(request,'booked_flats.html')

def cancelled_flats(request):
    return render(request,'cancelled_flats.html')

def channel_partner(request):
    return render(request,'channel_partner.html')

def construction_updates(request):
    return render(request,'construction_updates.html')

def customer(request):
    return render(request,'customer.html')

def documents_section(request):
    return render(request,'documents_section.html')

def flat_customization(request):
    return render(request,'flat_customization.html')

def flats_summary(request):
    return render(request,'flats_summary.html')

def flats_status(request):
    return render(request,'flats_status.html')

def flats_verification(request):
    return render(request,'flats_verification.html')

def handover_activities(request):
    return render(request,'handover_activities.html')

def loan(request):
    return render(request,'loan.html')

def new_booking(request):
    return render(request,'new_booking.html')

def payment_received(request):
    return render(request,'payment_received.html')

def payment_status(request):
    return render(request,'payment_status.html')

def Project_Snapshot(request):
    return render(request,'Project_Snapshot.html')

def reports(request):
    return render(request,'reports.html')

def set_reminder(request):
    return render(request,'set_reminder.html')
