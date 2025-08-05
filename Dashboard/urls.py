from django.contrib import admin
from django.urls import path
from Dashboard import views

urlpatterns = [
    path('',views.index,name='Days'),
    path('block_inventory',views.block_inventory,name='block_inventory'),
    path('blocked_flats',views.blocked_flats,name='blocked_flats'),
    path('booked_flats',views.booked_flats,name='booked_flats'),
    path('cancelled_flats',views.cancelled_flats,name='cancelled_flats'),
    path('channel_partner',views.channel_partner,name='channel_partner'),
    path('construction_updates',views.construction_updates,name='construction_updates'),
    path('customer',views.customer,name='customer'),
    path('documents_section',views.documents_section,name='documents_section'),
    path('flat_customization',views.flat_customization,name='flat_customization'),
    path('flats_summary',views.flats_summary,name='flats_summary'),
    path('flats_verification',views.flats_verification,name='flats_verification'),
    path('flats_status',views.flats_status,name='flats_status'),
    path('handover_activities',views.handover_activities,name='handover_activities'),
    path('index',views.index,name='index'),
    path('loan',views.loan,name='loan'),
    path('manage',views.manage,name='manage'),
    path('new_booking',views.new_booking,name='new_booking'),
    path('payment_received',views.payment_received,name='payment_received'),
    path('payment_status',views.payment_status,name='payment_status'),
    path('Project_Snapshot',views.Project_Snapshot,name='Project_Snapshot'),
    path('reports',views.reports,name='reports'),
    path('set_reminder',views.set_reminder,name='set_reminder')
]