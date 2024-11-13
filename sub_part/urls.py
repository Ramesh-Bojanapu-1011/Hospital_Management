from importlib.resources import path

from django.urls import path  # noqa: F811


from . import views 

# The code is defining URL patterns for a Django web application. Each `path` function call
# specifies a URL pattern along with the corresponding view function that should be called when that
# URL is accessed. The URLs are mapped to specific views within the Django application.
urlpatterns =[
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('contact_form_submition',views.contact_form_submition,name='contact_form_submition'), 
    path('appintment_form',views.appintment_form,name='appintment_form'),
    path('login',views.login,name='login'),
    path('dashboard/<int:id>',views.dashboard,name='dashboard'),

    path('otp_verfy',views.otp_verfy,name='otp_verfy'),
    path('registration',views.registration,name='registration'), 
    path('login_form',views.login_form,name='login_form'), 
    path('logout',views.logout,name='logout'), 
    path('forgot_password',views.forgot_password,name='forgot_password'),    

    path('doctors/<int:id>',views.doctors,name='doctors'),
    path('doctor_add/<int:id>',views.doctor_add,name='doctor_add'),
    path('Doctors_edit/<int:id>/<int:row_id>',views.Doctors_edit,name='Doctors_edit'),
    path('add_doctors/<int:id>',views.add_doctors,name='add_doctors'),
    path('update_doctor_datails/<int:id>/<int:row_id>',views.update_doctor_datails,name='update_doctor_datails'),
    path('delete_doctor_details/<int:id>/<int:row_id>',views.delete_doctor_details,name='delete_doctor_details'),

    path('Staff/<int:id>',views.Staff,name='Staff'),
    path('Staff_edit/<int:id>/<int:row_id>',views.Staff_edit,name='Staff_edit'),
    path('staff_add/<int:id>',views.staff_add,name='staff_add'),
    path('add_staff/<int:id>',views.add_staff,name='add_staff'),
    path('update_Staff_datails/<int:id>/<int:row_id>',views.update_Staff_datails,name='update_Staff_datails'),
    path('delete_Staff_details/<int:id>/<int:row_id>',views.delete_Staff_details,name='delete_Staff_details'),
    
    path('appointment/<int:id>',views.appointment,name='appointment'),
    path('appointment_edit/<int:id>/<int:row_id>',views.appointment_edit,name='appointment_edit'),
    path('appointment_add/<int:id>',views.appointment_add,name='appointment_add'),
    path('add_Appointments/<int:id>',views.add_Appointments,name='add_Appointments'),
    path('update_appointment_datails/<int:id>/<int:row_id>',views.update_appointment_datails,name='update_appointment_datails'),
    path('delete_appointment_details/<int:id>/<int:row_id>',views.delete_appointment_details,name='delete_appointment_details'),

    path('in_patient/<int:id>',views.in_patient,name='in_patient'),
    path('ipd_add/<int:id>',views.ipd_add,name='ipd_add'),
    path('ipd_edit/<int:id>/<int:row_id>',views.ipd_edit,name='ipd_edit'),
    path('add_ipd/<int:id>',views.add_ipd,name='add_ipd'),
    path('update_in_patient_datails/<int:id>/<int:row_id>',views.update_in_patient_datails,name='update_in_patient_datails'),
    path('delete_in_patient_details/<int:id>/<int:row_id>',views.delete_in_patient_details,name='delete_in_patient_details'),    

    path('out_paitent/<int:id>',views.out_paitent,name='out_paitent'),
    path('opd_add/<int:id>',views.opd_add,name='opd_add'),
    path('opd_edit/<int:id>/<int:row_id>',views.opd_edit,name='opd_edit'),
    path('add_opd/<int:id>',views.add_opd,name='add_opd'),
    path('update_out_paitent_datails/<int:id>/<int:row_id>',views.update_out_paitent_datails,name='update_out_paitent_datails'),
    path('delete_out_paitent_details/<int:id>/<int:row_id>',views.delete_out_paitent_details,name='delete_out_paitent_details'),

    path('EmergencyWard/<int:id>',views.EmergencyWard,name='EmergencyWard'),
    path('emergency_edit/<int:id>/<int:row_id>',views.emergency_edit,name='emergency_edit'),
    path('emergency_add/<int:id>',views.emergency_add,name='emergency_add'),
    path('add_Emergency/<int:id>',views.add_Emergency,name='add_Emergency'),
    path('update_EmergencyWard_datails/<int:id>/<int:row_id>',views.update_EmergencyWard_datails,name='update_EmergencyWard_datails'),
    path('delete_EmergencyWard_details/<int:id>/<int:row_id>',views.delete_EmergencyWard_details,name='delete_EmergencyWard_details'),

    path('Covid_19/<int:id>',views.Covid_19,name='Covid_19'),
    path('covid_add/<int:id>',views.covid_add,name='covid_add'),
    path('covid_edit/<int:id>/<int:row_id>',views.covid_edit,name='covid_edit'),
    path('add_covid/<int:id>',views.add_covid,name='add_covid'),
    path('update_Covid_19_datails/<int:id>/<int:row_id>',views.update_Covid_19_datails,name='update_Covid_19_datails'),
    path('delete_Covid_19_details/<int:id>/<int:row_id>',views.delete_Covid_19_details,name='delete_Covid_19_details'),

    path('BirthRecord/<int:id>',views.BirthRecord,name='BirthRecord'),
    path('birth_add/<int:id>',views.birth_add,name='birth_add'),
    path('birth_edit/<int:id>/<int:row_id>',views.birth_edit,name='birth_edit'),
    path('add_BirthRecord/<int:id>',views.add_BirthRecord,name='add_BirthRecord'),
    path('update_BirthRecord_datails/<int:id>/<int:row_id>',views.update_BirthRecord_datails,name='update_BirthRecord_datails'),
    path('delete_BirthRecord_details/<int:id>/<int:row_id>',views.delete_BirthRecord_details,name='delete_BirthRecord_details'),

    path('Radiology/<int:id>',views.Radiology,name='Radiology'),
    path('Radiology_edit/<int:id>/<int:row_id>',views.Radiology_edit,name='Radiology_edit'),
    path('Radiology_add/<int:id>',views.Radiology_add,name='Radiology_add'),
    path('add_Radiology/<int:id>',views.add_Radiology,name='add_Radiology'),
    path('update_Radiology_datails/<int:id>/<int:row_id>',views.update_Radiology_datails,name='update_Radiology_datails'),
    path('delete_Radiology_details/<int:id>/<int:row_id>',views.delete_Radiology_details,name='delete_Radiology_details'),

    path('Pathology/<int:id>',views.Pathology,name='Pathology'),
    path('Pathology_edit/<int:id>/<int:row_id>',views.Pathology_edit,name='Pathology_edit'),
    path('Pathology_add/<int:id>',views.Pathology_add,name='Pathology_add'),
    path('add_Pathology/<int:id>',views.add_Pathology,name='add_Pathology'),
    path('update_Pathology_datails/<int:id>/<int:row_id>',views.update_Pathology_datails,name='update_Pathology_datails'),
    path('delete_Pathology_details/<int:id>/<int:row_id>',views.delete_Pathology_details,name='delete_Pathology_details'),

    path('OperationTheater/<int:id>',views.OperationTheater,name='OperationTheater'),
    path('OperationTheater_add/<int:id>',views.OperationTheater_add,name='OperationTheater_add'),
    path('OperationTheater_edit/<int:id>/<int:row_id>',views.OperationTheater_edit,name='OperationTheater_edit'),
    path('add_OperationTheater/<int:id>',views.add_OperationTheater,name='add_OperationTheater'),
    path('update_OperationTheater_datails/<int:id>/<int:row_id>',views.update_OperationTheater_datails,name='update_OperationTheater_datails'),
    path('delete_OperationTheater_details/<int:id>/<int:row_id>',views.delete_OperationTheater_details,name='delete_OperationTheater_details'),

    path('Pharmacy/<int:id>',views.Pharmacy,name='Pharmacy'),
    path('Pharmacy_add/<int:id>',views.Pharmacy_add,name='Pharmacy_add'),
    path('Pharmacy_edit/<int:id>/<int:row_id>',views.Pharmacy_edit,name='Pharmacy_edit'),
    path('add_Pharmacy/<int:id>',views.add_Pharmacy,name='add_Pharmacy'),
    path('update_Pharmacy_datails/<int:id>/<int:row_id>',views.update_Pharmacy_datails,name='update_Pharmacy_datails'),
    path('delete_Pharmacy_details/<int:id>/<int:row_id>',views.delete_Pharmacy_details,name='delete_Pharmacy_details'),
    
    path('ambulance/<int:id>',views.ambulance,name='ambulance'),
    path('ambulance_edit/<int:id>/<int:row_id>',views.ambulance_edit,name='ambulance_edit'),
    path('ambulance_add/<int:id>',views.ambulance_add,name='ambulance_add'),
    path('add_ambulance/<int:id>',views.add_ambulance,name='add_ambulance'),
    path('update_Ambulance_datails/<int:id>/<int:row_id>',views.update_Ambulance_datails,name='update_Ambulance_datails'),
    path('delete_Ambulance_details/<int:id>/<int:row_id>',views.delete_Ambulance_details,name='delete_Ambulance_details'),
]