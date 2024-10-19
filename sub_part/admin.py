from django.contrib import admin

# Register your models here.
 

from . models import profile,otp_details,contact_form_table,Appointment_form_submition, registration_table, add_doctor_details,add_OPD_details,add_IPD_details,add_staff_details,add_Appointment_details,add_EmergencyWard_details,add_Covid_19_details,add_BirthRecord_details,add_Radiology_details,add_Pathology_details,add_Pharmacy_details,add_Ambulance_details,add_OperationTheater_details

admin.site.register(otp_details)

admin.site.register(profile)

admin.site.register(contact_form_table)

admin.site.register(Appointment_form_submition)

admin.site.register(registration_table)

admin.site.register(add_doctor_details)

admin.site.register(add_OPD_details)

admin.site.register(add_IPD_details)

admin.site.register(add_staff_details)

admin.site.register(add_Appointment_details)

admin.site.register(add_EmergencyWard_details)

admin.site.register(add_Covid_19_details)

admin.site.register(add_BirthRecord_details)

admin.site.register(add_Radiology_details)

admin.site.register(add_Pathology_details)

admin.site.register(add_Pharmacy_details)

admin.site.register(add_Ambulance_details)

admin.site.register(add_OperationTheater_details)