from django.shortcuts import render

from django.contrib import messages

from .models import (
    contact_form_table,
    otp_details,
    Appointment_form_submition,
    add_Pharmacy_details,
    add_OperationTheater_details,
    add_Ambulance_details,
    add_Radiology_details,
    add_Pathology_details,
    add_BirthRecord_details,
    add_Covid_19_details,
    registration_table,
    add_OPD_details,
    add_EmergencyWard_details,
    add_IPD_details,
    add_doctor_details,
    add_staff_details,
    add_Appointment_details,
)


import math
import random


# Create your views here.


def index(request):
    return render(request, "index.html")


def appintment_form(request):
    if request.method == "POST":
        if Appointment_form_submition.objects.filter(
            email=request.POST.get("email"),
            phone_number=request.POST.get("phone_number"),
        ):
            messages.error(
                request, "Already  received your appintment", extra_tags="already_a"
            )
            return render(request, "index.html")
        else:
            ex1 = Appointment_form_submition(
                Your_Name=request.POST.get("Your_Name"),
                email=request.POST.get("email"),
                phone_number=request.POST.get("phone_number"),
                date_time=request.POST.get("date_time"),
                department=request.POST.get("department"),
                doctor=request.POST.get("doctor"),
            )
            ex1.save()
           
            messages.error(
                request, "Successfully submited  your Appointment", extra_tags="saved_a"
            )
            return render(request, "index.html")


def contact_form_submition(request):
    if request.method == "POST":
        if contact_form_table.objects.filter(email_id=request.POST.get("email_id")):
            messages.error(
                request, "Already  received your responce", extra_tags="already"
            )
            return render(request, "index.html")
        else:
            ex1 = contact_form_table(
                name=request.POST.get("name"),
                email_id=request.POST.get("email_id"),
                subject=request.POST.get("subject"),
                message=request.POST.get("message"),
            )
            ex1.save()
            messages.error(request, "Successfully submited", extra_tags="saved")
            return render(request, "index.html")
    else:
        return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def registration(request):
    if request.method == "POST":
        if registration_table.objects.filter(email_id=request.POST.get("email_id")):
            messages.error(request, "Already registered", extra_tags="Alredy")
            return render(request, "login.html")

        elif registration_table.objects.filter(
            mobile_number=request.POST.get("mobile_number")
        ):
            messages.error(request, "Already registered", extra_tags="Alredy")
            return render(request, "login.html")

        elif registration_table.objects.filter(
            mobile_number=request.POST.get("mobile_number"),
            email_id=request.POST.get("email_id"),
        ):
            messages.error(request, "Already registered", extra_tags="Alredy")
            return render(request, "login.html")

        else:
            ex1 = registration_table(
                username=request.POST.get("username"),
                email_id=request.POST.get("email_id"),
                Password=request.POST.get("Password"),
                mobile_number=request.POST.get('mobile_number')
            )
            if len(request.FILES) != 0:
                ex1.profile = request.FILES.get("profiles")
            ex1.save()
             

            messages.error(request, "Successly registered", extra_tags="register")
            return render(request, "login.html")
    else:
        return render(request, "login.html")


def login_form(request):
    if request.method == "POST":
        if registration_table.objects.filter(
            email_id=request.POST.get("email_id"), Password=request.POST.get("Password")
        ).exists():
            ex1 = registration_table.objects.get(email_id=request.POST.get("email_id"))
            take_email = ex1.email_id
            # otp=generateOTP()
            # print("OTP :" + otp)

            # subject = 'welcome to MEDICE LAB'
            # message = f'Your OTP is {otp}'
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [take_email]
            # send_mail( subject, message, email_from, recipient_list )
            print(take_email)
            # if otp_details.objects.filter(email_id=request.POST.get('email_id')).exists():
            #      ex1=otp_details.objects.filter(email_id=request.POST.get('email_id')).update(email_id=request.POST.get('email_id'),
            #       otp = otp)
            # else:
            #     ex1=otp_details(   email_id = request.POST.get('email_id'),
            #       otp = otp
            #     )
            #     ex1.save()

            # maskEmail = mask(take_email)
            # emailInfo = {'email_id':take_email, 'mskEmail':maskEmail}
            # return render(request,'verify.html',{'data':emailInfo})
            take_id = ex1.id
            take_username = registration_table.objects.get(email_id=take_email)
            print(take_username)
            take_username = registration_table.objects.get(
                email_id=request.POST.get("email_id")
            )
            count_doctor = add_doctor_details.objects.filter(loger_id=take_id).count()
            count_staff = add_staff_details.objects.filter(loger_id=take_id).count()
            count_appointments = add_Appointment_details.objects.filter(
                loger_id=take_id
            ).count()
            count_ipd = add_IPD_details.objects.filter(loger_id=take_id).count()
            conut_opd = add_OPD_details.objects.filter(loger_id=take_id).count()
            count_emergency = add_EmergencyWard_details.objects.filter(
                loger_id=take_id
            ).count()
            count_covid = add_Covid_19_details.objects.filter(loger_id=take_id).count()
            count_birth = add_BirthRecord_details.objects.filter(
                loger_id=take_id
            ).count()
            count_RADIOLOGY = add_Radiology_details.objects.filter(
                loger_id=take_id
            ).count()
            count_PATHOLOGY = add_Pathology_details.objects.filter(
                loger_id=take_id
            ).count()
            count_OPERATION_THEATER = add_OperationTheater_details.objects.filter(
                loger_id=take_id
            ).count()
            count_PHARMACY = add_Pharmacy_details.objects.filter(
                loger_id=take_id
            ).count()
            count_AMBULANCE = add_Ambulance_details.objects.filter(
                loger_id=take_id
            ).count()
            return render(
                request,
                "dashboard.html",
                {
                    "take_username": take_username,
                    "count_ipd": count_ipd,
                    "conut_opd": conut_opd,
                    "count_emergency": count_emergency,
                    "count_covid": count_covid,
                    "count_RADIOLOGY": count_RADIOLOGY,
                    "count_birth": count_birth,
                    "count_PATHOLOGY": count_PATHOLOGY,
                    "count_OPERATION_THEATER": count_OPERATION_THEATER,
                    "count_appointments": count_appointments,
                    "count_PHARMACY": count_PHARMACY,
                    "count_AMBULANCE": count_AMBULANCE,
                    "count_doctor": count_doctor,
                    "count_staff": count_staff,
                },
            )

        else:
            if registration_table.objects.filter(
                email_id=request.POST.get("email_id")
            ).exists():
                messages.error(
                    request, "You entered invalid credentials", extra_tags="invalid"
                )
                return render(request, "login.html")
            else:
                messages.error(
                    request,
                    "Did not have a account create new account",
                    extra_tags="create_new",
                )
                return render(request, "login.html")

    else:
        return render(request, "login.html")


def forgot_password(request):
    return render(request, "forgot_password.html")


def otp_verfy(request):
    print("otp inside")
    if otp_details.objects.filter(
        email_id=request.POST.get("email_id"), otp=request.POST.get("otp")
    ).exists():
        print("otp success")
        ex1 = registration_table.objects.get(email_id=request.POST.get("email_id"))
        take_email = ex1.email_id
        request.session["email_id"] = ex1.email_id
        take_id = ex1.id
        print(take_email)
        take_username = registration_table.objects.get(email_id=take_email)
        print(take_username)
        take_username = registration_table.objects.get(
            email_id=request.POST.get("email_id")
        )
        count_doctor = add_doctor_details.objects.filter(loger_id=take_id).count()
        count_staff = add_staff_details.objects.filter(loger_id=take_id).count()
        count_appointments = add_Appointment_details.objects.filter(
            loger_id=take_id
        ).count()
        count_ipd = add_IPD_details.objects.filter(loger_id=take_id).count()
        conut_opd = add_OPD_details.objects.filter(loger_id=take_id).count()
        count_emergency = add_EmergencyWard_details.objects.filter(
            loger_id=take_id
        ).count()
        count_covid = add_Covid_19_details.objects.filter(loger_id=take_id).count()
        count_birth = add_BirthRecord_details.objects.filter(loger_id=take_id).count()
        count_RADIOLOGY = add_Radiology_details.objects.filter(loger_id=take_id).count()
        count_PATHOLOGY = add_Pathology_details.objects.filter(loger_id=take_id).count()
        count_OPERATION_THEATER = add_OperationTheater_details.objects.filter(
            loger_id=take_id
        ).count()
        count_PHARMACY = add_Pharmacy_details.objects.filter(loger_id=take_id).count()
        count_AMBULANCE = add_Ambulance_details.objects.filter(loger_id=take_id).count()
        return render(
            request,
            "dashboard.html",
            {
                "take_username": take_username,
                "count_ipd": count_ipd,
                "conut_opd": conut_opd,
                "count_emergency": count_emergency,
                "count_covid": count_covid,
                "count_RADIOLOGY": count_RADIOLOGY,
                "count_birth": count_birth,
                "count_PATHOLOGY": count_PATHOLOGY,
                "count_OPERATION_THEATER": count_OPERATION_THEATER,
                "count_appointments": count_appointments,
                "count_PHARMACY": count_PHARMACY,
                "count_AMBULANCE": count_AMBULANCE,
                "count_doctor": count_doctor,
                "count_staff": count_staff,
            },
        )
    else:
        messages.error(request, "invalid OTP", extra_tags="login")
        return render(request, "verify.html")


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def mask(s):
    lo = s.find("@")
    eml = s.split("@")
    emf, eml = eml
    msk = ""
    if lo > 0:
        msk = s[0] + "*********" + s[lo - 1] + "@" + eml
        print("masked email: " + msk)
    return msk


def logout(request):
    # request.session.clear()
    return render(request, "login.html")


def dashboard(request, id):
    take_username = registration_table.objects.get(id=id)
    count_doctor = add_doctor_details.objects.filter(loger_id=id).count()
    count_staff = add_staff_details.objects.filter(loger_id=id).count()
    count_appointments = add_Appointment_details.objects.filter(loger_id=id).count()
    count_ipd = add_IPD_details.objects.filter(loger_id=id).count()
    conut_opd = add_OPD_details.objects.filter(loger_id=id).count()
    count_emergency = add_EmergencyWard_details.objects.filter(loger_id=id).count()
    count_covid = add_Covid_19_details.objects.filter(loger_id=id).count()
    count_birth = add_BirthRecord_details.objects.filter(loger_id=id).count()
    count_RADIOLOGY = add_Radiology_details.objects.filter(loger_id=id).count()
    count_PATHOLOGY = add_Pathology_details.objects.filter(loger_id=id).count()
    count_OPERATION_THEATER = add_OperationTheater_details.objects.filter(
        loger_id=id
    ).count()
    count_PHARMACY = add_Pharmacy_details.objects.filter(loger_id=id).count()
    count_AMBULANCE = add_Ambulance_details.objects.filter(loger_id=id).count()
    return render(
        request,
        "dashboard.html",
        {
            "take_username": take_username,
            "count_PHARMACY": count_PHARMACY,
            "count_AMBULANCE": count_AMBULANCE,
            "count_OPERATION_THEATER": count_OPERATION_THEATER,
            "count_PATHOLOGY": count_PATHOLOGY,
            "count_RADIOLOGY": count_RADIOLOGY,
            "count_covid": count_covid,
            "count_birth": count_birth,
            "count_emergency": count_emergency,
            "count_doctor": count_doctor,
            "count_staff": count_staff,
            "count_appointments": count_appointments,
            "conut_opd": conut_opd,
            "count_ipd": count_ipd,
        },
    )


# doctors
def doctors(request, id):
    take_username = registration_table.objects.get(id=id)
    view_Doctor_details = add_doctor_details.objects.filter(loger_id=id)
    return render(
        request,
        "doctors.html",
        {"take_username": take_username, "view_Doctor_details": view_Doctor_details},
    )


def doctor_add(request, id):
    take_username = registration_table.objects.get(id=id)
    return render(request, "doctor_add.html", {"take_username": take_username})


def add_doctors(request, id):
    take_username = registration_table.objects.get(id=id)
    if request.method == "POST":
        ex1 = add_doctor_details(
            Doctor_Name=request.POST.get("Doctor_Name"),
            Department=request.POST.get("Department"),
            Specialization=request.POST.get("Specialization"),
            Availability=request.POST.get("Availability"),
            Joined_Date=request.POST.get("Joined_Date"),
            loger_id=request.POST.get("loger_id"),
        )
        ex1.save()
        view_Doctor_details = add_doctor_details.objects.filter(loger_id=id)
        messages.error(
            request, "Successfully added Doctor details", extra_tags="doctor_add"
        )
        return render(
            request,
            "doctors.html",
            {
                "take_username": take_username,
                "view_Doctor_details": view_Doctor_details,
            },
        )


def Doctors_edit(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_doctor_details.objects.get(id=row_id)
    return render(
        request,
        "Doctors_edit.html",
        {"take_username": take_username, "edit_data": edit_data},
    )


def update_doctor_datails(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_doctor_details.objects.get(id=row_id)
    if request.method == "POST":
        ex1 = add_doctor_details.objects.filter(id=row_id).update(
            Doctor_Name=request.POST.get("Doctor_Name"),
            Department=request.POST.get("Department"),
            Specialization=request.POST.get("Specialization"),
            Availability=request.POST.get("Availability"),
            Joined_Date=request.POST.get("Joined_Date"),
            loger_id=request.POST.get("loger_id"),
        )
        ex1
        view_Doctor_details = add_doctor_details.objects.filter(loger_id=id)
        print("successfully updated.....")
        messages.error(
            request, "Successfully edited Doctor details", extra_tags="doctor_add"
        )
        return render(
            request,
            "doctors.html",
            {
                "take_username": take_username,
                "edit_data": edit_data,
                "view_Doctor_details": view_Doctor_details,
            },
        )


def delete_doctor_details(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_doctor_details.objects.get(id=row_id)
    edit_data.delete()
    view_Doctor_details = add_doctor_details.objects.filter(loger_id=id)
    messages.error(
        request, "Successfully deleted Doctor details", extra_tags="doctor_add"
    )
    return render(
        request,
        "doctors.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_Doctor_details": view_Doctor_details,
        },
    )


# Staff


def Staff(request, id):
    take_username = registration_table.objects.get(id=id)
    view_staff_details = add_staff_details.objects.filter(loger_id=id)
    return render(
        request,
        "Staff.html",
        {"take_username": take_username, "view_staff_details": view_staff_details},
    )


def Staff_edit(request, id, row_id):
    edit_data = add_staff_details.objects.get(id=row_id)
    take_username = registration_table.objects.get(id=id)
    return render(
        request,
        "Staff_edit.html",
        {"take_username": take_username, "edit_data": edit_data},
    )


def staff_add(request, id):
    take_username = registration_table.objects.get(id=id)
    return render(request, "staff_add.html", {"take_username": take_username})


def add_staff(request, id):
    take_username = registration_table.objects.get(id=id)
    if request.method == "POST":
        ex1 = add_staff_details(
            Staff_Id=request.POST.get("Staff_Id"),
            Staff_Name=request.POST.get("Staff_Name"),
            Category=request.POST.get("Category"),
            Joined_Date=request.POST.get("Joined_Date"),
            Attendance=request.POST.get("Attendance"),
            loger_id=request.POST.get("loger_id"),
        )
        ex1.save()
        view_staff_details = add_staff_details.objects.filter(loger_id=id)
        messages.error(
            request, "Successfully added staff details", extra_tags="staff_add"
        )
        return render(
            request,
            "Staff.html",
            {"take_username": take_username, "view_staff_details": view_staff_details},
        )


def update_Staff_datails(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_staff_details.objects.get(id=row_id)
    if request.method == "POST":
        ex1 = add_staff_details.objects.filter(id=row_id).update(
            Staff_Id=request.POST.get("Staff_Id"),
            Staff_Name=request.POST.get("Staff_Name"),
            Category=request.POST.get("Category"),
            Joined_Date=request.POST.get("Joined_Date"),
            Attendance=request.POST.get("Attendance"),
            loger_id=request.POST.get("loger_id"),
        )
        ex1
        view_staff_details = add_staff_details.objects.filter(loger_id=id)
        print("successfully updated.....")
        messages.error(
            request, "Successfully edited Staff details", extra_tags="staff_add"
        )
        return render(
            request,
            "Staff.html",
            {
                "take_username": take_username,
                "edit_data": edit_data,
                "view_staff_details": view_staff_details,
            },
        )


def delete_Staff_details(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_staff_details.objects.get(id=row_id)
    edit_data.delete()
    view_staff_details = add_staff_details.objects.filter(loger_id=id)
    messages.error(
        request, "Successfully deleted Staff details", extra_tags="staff_add"
    )
    return render(
        request,
        "Staff.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_staff_details": view_staff_details,
        },
    )


# appointment


def appointment(request, id):
    take_username = registration_table.objects.get(id=id)
    view_Appointment_details = add_Appointment_details.objects.filter(loger_id=id)
    return render(
        request,
        "appointment.html",
        {
            "take_username": take_username,
            "view_Appointment_details": view_Appointment_details,
        },
    )


def appointment_edit(request, id, row_id):
    edit_data = add_Appointment_details.objects.get(id=row_id)
    take_username = registration_table.objects.get(id=id)
    return render(
        request,
        "appointment_edit.html",
        {"take_username": take_username, "edit_data": edit_data},
    )


def appointment_add(request, id):
    take_username = registration_table.objects.get(id=id)
    return render(request, "appointment_add.html", {"take_username": take_username})


def add_Appointments(request, id):
    take_username = registration_table.objects.get(id=id)
    if request.method == "POST":
        ex1 = add_Appointment_details(
            Token_Number=request.POST.get("Token_Number"),
            Paitent_Name=request.POST.get("Paitent_Name"),
            Age=request.POST.get("Age"),
            Referred_Doctor=request.POST.get("Referred_Doctor"),
            Visiting_Purpose=request.POST.get("Visiting_Purpose"),
            Time=request.POST.get("Time"),
            loger_id=request.POST.get("loger_id"),
        )
        ex1.save()
        view_Appointment_details = add_Appointment_details.objects.filter(loger_id=id)
        messages.error(
            request,
            "Successfully added appointment details",
            extra_tags="add_Appointments",
        )
        return render(
            request,
            "appointment.html",
            {
                "take_username": take_username,
                "view_Appointment_details": view_Appointment_details,
            },
        )


def update_appointment_datails(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_Appointment_details.objects.get(id=row_id)
    ex1 = add_Appointment_details.objects.filter(id=row_id).update(
        Token_Number=request.POST.get("Token_Number"),
        Paitent_Name=request.POST.get("Paitent_Name"),
        Age=request.POST.get("Age"),
        Referred_Doctor=request.POST.get("Referred_Doctor"),
        Visiting_Purpose=request.POST.get("Visiting_Purpose"),
        Time=request.POST.get("Time"),
        loger_id=request.POST.get("loger_id"),
    )
    ex1
    view_Appointment_details = add_Appointment_details.objects.filter(loger_id=id)
    print("successfully updated.....")
    messages.error(
        request,
        "Successfully edited appointment details",
        extra_tags="add_Appointments",
    )
    return render(
        request,
        "appointment.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_Appointment_details": view_Appointment_details,
        },
    )


def delete_appointment_details(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_Appointment_details.objects.get(id=row_id)
    edit_data.delete()
    view_Appointment_details = add_Appointment_details.objects.filter(loger_id=id)
    messages.error(
        request,
        "Successfully deleted appointment details",
        extra_tags="add_Appointments",
    )
    return render(
        request,
        "appointment.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_Appointment_details": view_Appointment_details,
        },
    )


# in_patient


def in_patient(request, id):
    take_username = registration_table.objects.get(id=id)
    view_ipd_details = add_IPD_details.objects.filter(loger_id=id)
    return render(
        request,
        "in_patient.html",
        {"take_username": take_username, "view_ipd_details": view_ipd_details},
    )


def ipd_add(request, id):
    take_username = registration_table.objects.get(id=id)
    return render(request, "ipd_add.html", {"take_username": take_username})


def add_ipd(request, id):
    take_username = registration_table.objects.get(id=id)
    if request.method == "POST":
        ex1 = add_IPD_details(
            Joining_Date=request.POST.get("Joining_Date"),
            Paitent_Name=request.POST.get("Paitent_Name"),
            Age=request.POST.get("Age"),
            Gender=request.POST.get("Gender"),
            Phone_Number=request.POST.get("Phone_Number"),
            Docter_Name=request.POST.get("Docter_Name"),
            Bed_Charges=request.POST.get("Bed_Charges"),
            Payment=request.POST.get("Payment"),
            Due_Payment=request.POST.get("Due_Payment"),
            loger_id=request.POST.get("loger_id"),
        )
        ex1.save()
        view_ipd_details = add_IPD_details.objects.filter(loger_id=id)
        messages.error(
            request, "Successfully added in paitent details", extra_tags="add_ipd"
        )
        return render(
            request,
            "in_patient.html",
            {"take_username": take_username, "view_ipd_details": view_ipd_details},
        )


def ipd_edit(request, id, row_id):
    edit_data = add_IPD_details.objects.get(id=row_id)
    take_username = registration_table.objects.get(id=id)
    return render(
        request,
        "ipd_edit.html",
        {"take_username": take_username, "edit_data": edit_data},
    )


def update_in_patient_datails(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_IPD_details.objects.get(id=row_id)
    ex1 = add_IPD_details.objects.filter(id=row_id).update(
        Joining_Date=request.POST.get("Joining_Date"),
        Paitent_Name=request.POST.get("Paitent_Name"),
        Age=request.POST.get("Age"),
        Gender=request.POST.get("Gender"),
        Phone_Number=request.POST.get("Phone_Number"),
        Docter_Name=request.POST.get("Docter_Name"),
        Bed_Charges=request.POST.get("Bed_Charges"),
        Payment=request.POST.get("Payment"),
        Due_Payment=request.POST.get("Due_Payment"),
        loger_id=request.POST.get("loger_id"),
    )
    ex1
    view_ipd_details = add_IPD_details.objects.filter(loger_id=id)
    print("successfully updated.....")
    messages.error(
        request, "Successfully edited in_patient details", extra_tags="add_ipd"
    )
    return render(
        request,
        "in_patient.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_ipd_details": view_ipd_details,
        },
    )


def delete_in_patient_details(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_IPD_details.objects.get(id=row_id)
    edit_data.delete()
    view_ipd_details = add_IPD_details.objects.filter(loger_id=id)
    messages.error(
        request, "Successfully deleted in_patient details", extra_tags="add_ipd"
    )
    return render(
        request,
        "in_patient.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_ipd_details": view_ipd_details,
        },
    )


# out_paitent


def out_paitent(request, id):
    view_opd_details = add_OPD_details.objects.filter(loger_id=id)
    take_username = registration_table.objects.get(id=id)
    return render(
        request,
        "out_paitent.html",
        {"take_username": take_username, "view_opd_details": view_opd_details},
    )


def opd_add(request, id):
    take_username = registration_table.objects.get(id=id)
    return render(request, "opd_add.html", {"take_username": take_username})


def add_opd(request, id):
    take_username = registration_table.objects.get(id=id)
    if request.method == "POST":
        ex1 = add_OPD_details(
            Paitent_Name=request.POST.get("Paitent_Name"),
            Age=request.POST.get("Age"),
            Gender=request.POST.get("Gender"),
            Contact_Number=request.POST.get("Contact_Number"),
            Docter_Name=request.POST.get("Docter_Name"),
            Last_Visit=request.POST.get("Last_Visit"),
            Total_Visit=request.POST.get("Total_Visit"),
            loger_id=request.POST.get("loger_id"),
        )
        ex1.save()
        view_opd_details = add_OPD_details.objects.filter(loger_id=id)
        messages.error(
            request, "Successfully added out patient details", extra_tags="add_opd"
        )
        return render(
            request,
            "out_paitent.html",
            {"take_username": take_username, "view_opd_details": view_opd_details},
        )


def opd_edit(request, id, row_id):
    edit_data = add_OPD_details.objects.get(id=row_id)
    take_username = registration_table.objects.get(id=id)
    return render(
        request,
        "opd_edit.html",
        {"take_username": take_username, "edit_data": edit_data},
    )


def update_out_paitent_datails(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_OPD_details.objects.get(id=row_id)
    ex1 = add_OPD_details.objects.filter(id=row_id).update(
        Paitent_Name=request.POST.get("Paitent_Name"),
        Age=request.POST.get("Age"),
        Gender=request.POST.get("Gender"),
        Contact_Number=request.POST.get("Contact_Number"),
        Docter_Name=request.POST.get("Docter_Name"),
        Last_Visit=request.POST.get("Last_Visit"),
        Total_Visit=request.POST.get("Total_Visit"),
        loger_id=request.POST.get("loger_id"),
    )
    print(ex1)
    view_opd_details = add_OPD_details.objects.filter(loger_id=id)
    print("successfully updated.....")
    messages.error(
        request, "Successfully edited out_paitent details", extra_tags="add_opd"
    )
    return render(
        request,
        "out_paitent.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_opd_details": view_opd_details,
        },
    )


def delete_out_paitent_details(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_OPD_details.objects.get(id=row_id)
    edit_data.delete()
    view_opd_details = add_OPD_details.objects.filter(loger_id=id)
    messages.error(
        request, "Successfully deleted out_paitent details", extra_tags="add_opd"
    )
    return render(
        request,
        "out_paitent.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_opd_details": view_opd_details,
        },
    )


# EmergencyWard


def EmergencyWard(request, id):
    view_EmergencyWard_details = add_EmergencyWard_details.objects.filter(loger_id=id)
    take_username = registration_table.objects.get(id=id)
    return render(
        request,
        "EmergencyWard.html",
        {
            "take_username": take_username,
            "view_EmergencyWard_details": view_EmergencyWard_details,
        },
    )


def emergency_edit(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_EmergencyWard_details.objects.get(id=row_id)
    return render(
        request,
        "emergency_edit.html",
        {"take_username": take_username, "edit_data": edit_data},
    )


def emergency_add(request, id):
    take_username = registration_table.objects.get(id=id)
    return render(request, "emergency_add.html", {"take_username": take_username})


def add_Emergency(request, id):
    take_username = registration_table.objects.get(id=id)
    if request.method == "POST":
        ex1 = add_EmergencyWard_details(
            Patient_Id=request.POST.get("Patient_Id"),
            Ward_Num=request.POST.get("Ward_Num"),
            Bed_Num=request.POST.get("Bed_Num"),
            JOINED_DATE=request.POST.get("JOINED_DATE"),
            Charges=request.POST.get("Charges"),
            loger_id=request.POST.get("loger_id"),
        )
        ex1.save()
        view_EmergencyWard_details = add_EmergencyWard_details.objects.filter(
            loger_id=id
        )
        messages.error(
            request,
            "Successfully added EmergencyWard details",
            extra_tags="add_Emergency",
        )
        return render(
            request,
            "EmergencyWard.html",
            {
                "take_username": take_username,
                "view_EmergencyWard_details": view_EmergencyWard_details,
            },
        )


def update_EmergencyWard_datails(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_EmergencyWard_details.objects.get(id=row_id)
    ex1 = add_EmergencyWard_details.objects.filter(id=row_id).update(
        Patient_Id=request.POST.get("Patient_Id"),
        Ward_Num=request.POST.get("Ward_Num"),
        Bed_Num=request.POST.get("Bed_Num"),
        JOINED_DATE=request.POST.get("JOINED_DATE"),
        Charges=request.POST.get("Charges"),
        loger_id=request.POST.get("loger_id"),
    )
    print(ex1)
    view_EmergencyWard_details = add_EmergencyWard_details.objects.filter(loger_id=id)
    print("successfully updated.....")
    messages.error(
        request, "Successfully edited EmergencyWard details", extra_tags="add_Emergency"
    )
    return render(
        request,
        "EmergencyWard.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_EmergencyWard_details": view_EmergencyWard_details,
        },
    )


def delete_EmergencyWard_details(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_EmergencyWard_details.objects.get(id=row_id)
    edit_data.delete()
    view_EmergencyWard_details = add_EmergencyWard_details.objects.filter(loger_id=id)
    messages.error(
        request,
        "Successfully deleted EmergencyWard details",
        extra_tags="add_Emergency",
    )
    return render(
        request,
        "EmergencyWard.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_EmergencyWard_details": view_EmergencyWard_details,
        },
    )


# Covid_19


def Covid_19(request, id):
    take_username = registration_table.objects.get(id=id)
    view_covid_details = add_Covid_19_details.objects.filter(loger_id=id)
    return render(
        request,
        "Covid_19.html",
        {"take_username": take_username, "view_covid_details": view_covid_details},
    )


def covid_add(request, id):
    take_username = registration_table.objects.get(id=id)
    return render(request, "covid_add.html", {"take_username": take_username})


def add_covid(request, id):
    take_username = registration_table.objects.get(id=id)
    if request.method == "POST":
        ex1 = add_Covid_19_details(
            Paitent_Name=request.POST.get("Paitent_Name"),
            Age=request.POST.get("Age"),
            Gender=request.POST.get("Gender"),
            Bed_Number=request.POST.get("Bed_Number"),
            Gaurdian_Name=request.POST.get("Gaurdian_Name"),
            JOINED_DATE=request.POST.get("JOINED_DATE"),
            Todays_Report=request.POST.get("Todays_Report"),
            loger_id=request.POST.get("loger_id"),
        )
        ex1.save()
        messages.error(
            request, "Successfully added Covid_19 details", extra_tags="add_covid"
        )
        view_covid_details = add_Covid_19_details.objects.filter(loger_id=id)
        return render(
            request,
            "Covid_19.html",
            {"take_username": take_username, "view_covid_details": view_covid_details},
        )


def covid_edit(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_Covid_19_details.objects.get(id=row_id)
    return render(
        request,
        "covid_edit.html",
        {"take_username": take_username, "edit_data": edit_data},
    )


def update_Covid_19_datails(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_Covid_19_details.objects.get(id=row_id)
    ex1 = add_Covid_19_details.objects.filter(id=row_id).update(
        Paitent_Name=request.POST.get("Paitent_Name"),
        Age=request.POST.get("Age"),
        Gender=request.POST.get("Gender"),
        Bed_Number=request.POST.get("Bed_Number"),
        Gaurdian_Name=request.POST.get("Gaurdian_Name"),
        JOINED_DATE=request.POST.get("JOINED_DATE"),
        Todays_Report=request.POST.get("Todays_Report"),
        loger_id=request.POST.get("loger_id"),
    )
    ex1
    view_covid_details = add_Covid_19_details.objects.filter(loger_id=id)
    print("successfully updated.....")
    messages.error(
        request, "Successfully edited Covid_19 details", extra_tags="add_covid"
    )
    return render(
        request,
        "Covid_19.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_covid_details": view_covid_details,
        },
    )


def delete_Covid_19_details(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_Covid_19_details.objects.get(id=row_id)
    edit_data.delete()
    view_covid_details = add_Covid_19_details.objects.filter(loger_id=id)
    messages.error(
        request, "Successfully deleted Covid_19 details", extra_tags="add_covid"
    )
    return render(
        request,
        "Covid_19.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_covid_details": view_covid_details,
        },
    )


# BirthRecord


def BirthRecord(request, id):
    take_username = registration_table.objects.get(id=id)
    view_BirthRecord_details = add_BirthRecord_details.objects.filter(loger_id=id)
    return render(
        request,
        "BirthRecord.html",
        {
            "take_username": take_username,
            "view_BirthRecord_details": view_BirthRecord_details,
        },
    )


def birth_add(request, id):
    take_username = registration_table.objects.get(id=id)
    return render(request, "birth_add.html", {"take_username": take_username})


def add_BirthRecord(request, id):
    take_username = registration_table.objects.get(id=id)
    if request.method == "POST":
        ex1 = add_BirthRecord_details(
            Child_Name=request.POST.get("Child_Name"),
            Gender=request.POST.get("Gender"),
            Birth_Date=request.POST.get("Birth_Date"),
            Mother_Name=request.POST.get("Mother_Name"),
            Father_Name=request.POST.get("Father_Name"),
            Report=request.POST.get("Report"),
            loger_id=request.POST.get("loger_id"),
        )
        ex1.save()
        messages.error(
            request,
            "Successfully added BirthRecord details",
            extra_tags="add_BirthRecord",
        )
        view_BirthRecord_details = add_BirthRecord_details.objects.filter(loger_id=id)
        return render(
            request,
            "BirthRecord.html",
            {
                "take_username": take_username,
                "view_BirthRecord_details": view_BirthRecord_details,
            },
        )


def birth_edit(request, id, row_id):
    edit_data = add_BirthRecord_details.objects.get(id=row_id)
    take_username = registration_table.objects.get(id=id)
    return render(
        request,
        "birth_edit.html",
        {"take_username": take_username, "edit_data": edit_data},
    )


def update_BirthRecord_datails(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_BirthRecord_details.objects.get(id=row_id)
    ex1 = add_BirthRecord_details.objects.filter(id=row_id).update(
        Child_Name=request.POST.get("Child_Name"),
        Gender=request.POST.get("Gender"),
        Birth_Date=request.POST.get("Birth_Date"),
        Mother_Name=request.POST.get("Mother_Name"),
        Father_Name=request.POST.get("Father_Name"),
        Report=request.POST.get("Report"),
        loger_id=request.POST.get("loger_id"),
    )
    print(ex1)
    view_BirthRecord_details = add_BirthRecord_details.objects.filter(loger_id=id)
    print("successfully updated.....")
    messages.error(
        request, "Successfully edited BirthRecord details", extra_tags="add_BirthRecord"
    )
    return render(
        request,
        "BirthRecord.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_BirthRecord_details": view_BirthRecord_details,
        },
    )


def delete_BirthRecord_details(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_BirthRecord_details.objects.get(id=row_id)
    edit_data.delete()
    view_BirthRecord_details = add_BirthRecord_details.objects.filter(loger_id=id)
    messages.error(
        request, "Successfully deleted BirthRecord details", extra_tags="add_ambulance"
    )
    return render(
        request,
        "BirthRecord.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_BirthRecord_details": view_BirthRecord_details,
        },
    )


# Radiology


def Radiology(request, id):
    take_username = registration_table.objects.get(id=id)
    view_Radiology_details = add_Radiology_details.objects.filter(loger_id=id)
    return render(
        request,
        "Radiology.html",
        {
            "take_username": take_username,
            "view_Radiology_details": view_Radiology_details,
        },
    )


def Radiology_add(request, id):
    take_username = registration_table.objects.get(id=id)
    return render(request, "Radiology_add.html", {"take_username": take_username})


def add_Radiology(request, id):
    take_username = registration_table.objects.get(id=id)
    if request.method == "POST":
        ex1 = add_Radiology_details(
            Patient_Id=request.POST.get("Patient_Id"),
            Test_Name=request.POST.get("Test_Name"),
            Short_Name=request.POST.get("Short_Name"),
            Test_Type=request.POST.get("Test_Type"),
            Category=request.POST.get("Category"),
            sub_Category=request.POST.get("sub_Category"),
            Report_Days=request.POST.get("Report_Days"),
            charge=request.POST.get("charge"),
            loger_id=request.POST.get("loger_id"),
        )
        ex1.save()
        messages.error(
            request, "Successfully added Radiology details", extra_tags="add_Radiology"
        )
        view_Radiology_details = add_Radiology_details.objects.filter(loger_id=id)
        return render(
            request,
            "Radiology.html",
            {
                "take_username": take_username,
                "view_Radiology_details": view_Radiology_details,
            },
        )


def Radiology_edit(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_Radiology_details.objects.get(id=row_id)
    return render(
        request,
        "Radiology_edit.html",
        {"take_username": take_username, "edit_data": edit_data},
    )


def update_Radiology_datails(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_Radiology_details.objects.get(id=row_id)
    ex1 = add_Radiology_details.objects.filter(id=row_id).update(
        Patient_Id=request.POST.get("Patient_Id"),
        Test_Name=request.POST.get("Test_Name"),
        Short_Name=request.POST.get("Short_Name"),
        Test_Type=request.POST.get("Test_Type"),
        Category=request.POST.get("Category"),
        sub_Category=request.POST.get("sub_Category"),
        Report_Days=request.POST.get("Report_Days"),
        charge=request.POST.get("charge"),
        loger_id=request.POST.get("loger_id"),
    )
    print(ex1)
    view_Radiology_details = add_Radiology_details.objects.filter(loger_id=id)
    print("successfully updated.....")
    messages.error(
        request, "Successfully edited Radiology details", extra_tags="add_Radiology"
    )
    return render(
        request,
        "Radiology.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_Radiology_details": view_Radiology_details,
        },
    )


def delete_Radiology_details(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_Radiology_details.objects.get(id=row_id)
    edit_data.delete()
    view_Radiology_details = add_Radiology_details.objects.filter(loger_id=id)
    messages.error(
        request, "Successfully deleted Radiology details", extra_tags="add_Radiology"
    )
    return render(
        request,
        "Radiology.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_Radiology_details": view_Radiology_details,
        },
    )


# Pathology


def Pathology(request, id):
    view_Pathology_details = add_Pathology_details.objects.filter(loger_id=id)
    take_username = registration_table.objects.get(id=id)
    return render(
        request,
        "Pathology.html",
        {
            "take_username": take_username,
            "view_Pathology_details": view_Pathology_details,
        },
    )


def Pathology_add(request, id):
    take_username = registration_table.objects.get(id=id)
    return render(request, "Pathology_add.html", {"take_username": take_username})


def add_Pathology(request, id):
    take_username = registration_table.objects.get(id=id)
    if request.method == "POST":
        ex1 = add_Pathology_details(
            Patient_Id=request.POST.get("Patient_Id"),
            Test_Name=request.POST.get("Test_Name"),
            Short_Name=request.POST.get("Short_Name"),
            Test_Type=request.POST.get("Test_Type"),
            Category=request.POST.get("Category"),
            sub_Category=request.POST.get("sub_Category"),
            Report_Days=request.POST.get("Report_Days"),
            charge=request.POST.get("charge"),
            loger_id=request.POST.get("loger_id"),
        )
        ex1.save()
        messages.error(
            request, "Successfully added Pathology details", extra_tags="add_Pathology"
        )
        view_Pathology_details = add_Pathology_details.objects.filter(loger_id=id)
        return render(
            request,
            "Pathology.html",
            {
                "take_username": take_username,
                "view_Pathology_details": view_Pathology_details,
            },
        )


def Pathology_edit(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_Pathology_details.objects.get(id=row_id)
    return render(
        request,
        "Pathology_edit.html",
        {"take_username": take_username, "edit_data": edit_data},
    )


def update_Pathology_datails(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_Pathology_details.objects.get(id=row_id)
    ex1 = add_Pathology_details.objects.filter(id=row_id).update(
        Patient_Id=request.POST.get("Patient_Id"),
        Test_Name=request.POST.get("Test_Name"),
        Short_Name=request.POST.get("Short_Name"),
        Test_Type=request.POST.get("Test_Type"),
        Category=request.POST.get("Category"),
        sub_Category=request.POST.get("sub_Category"),
        Report_Days=request.POST.get("Report_Days"),
        charge=request.POST.get("charge"),
        loger_id=request.POST.get("loger_id"),
    )
    print(ex1)
    view_Pathology_details = add_Pathology_details.objects.filter(loger_id=id)
    print("successfully updated.....")
    messages.error(
        request, "Successfully edited Pathology details", extra_tags="add_Pathology"
    )
    return render(
        request,
        "Pathology.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_Pathology_details": view_Pathology_details,
        },
    )


def delete_Pathology_details(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_Pathology_details.objects.get(id=row_id)
    edit_data.delete()
    view_Pathology_details = add_Pathology_details.objects.filter(loger_id=id)
    messages.error(
        request, "Successfully deleted Pathology details", extra_tags="add_Pathology"
    )
    return render(
        request,
        "Pathology.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_Pathology_details": view_Pathology_details,
        },
    )


# OperationTheater


def OperationTheater(request, id):
    take_username = registration_table.objects.get(id=id)
    view_OperationTheater_details = add_OperationTheater_details.objects.filter(
        loger_id=id
    )
    return render(
        request,
        "OperationTheater.html",
        {
            "take_username": take_username,
            "view_OperationTheater_details": view_OperationTheater_details,
        },
    )


def OperationTheater_add(request, id):
    take_username = registration_table.objects.get(id=id)
    return render(
        request, "OperationTheater_add.html", {"take_username": take_username}
    )


def add_OperationTheater(request, id):
    take_username = registration_table.objects.get(id=id)
    if request.method == "POST":
        ex1 = add_OperationTheater_details(
            Patient_Number=request.POST.get("Patient_Number"),
            Gender=request.POST.get("Gender"),
            Contact_Number=request.POST.get("Contact_Number"),
            Operation_Name=request.POST.get("Operation_Name"),
            Operation_Type=request.POST.get("Operation_Type"),
            Assigned_Doctor=request.POST.get("Assigned_Doctor"),
            OperationDate=request.POST.get("OperationDate"),
            Applied_Charges=request.POST.get("Applied_Charges"),
            loger_id=request.POST.get("loger_id"),
        )
        ex1.save()
        messages.error(
            request,
            "Successfully added OperationTheater details",
            extra_tags="add_OperationTheater",
        )
        view_OperationTheater_details = add_OperationTheater_details.objects.filter(
            loger_id=id
        )
        return render(
            request,
            "OperationTheater.html",
            {
                "take_username": take_username,
                "view_OperationTheater_details": view_OperationTheater_details,
            },
        )


def OperationTheater_edit(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_OperationTheater_details.objects.get(id=row_id)
    return render(
        request,
        "OperationTheater_edit.html",
        {"take_username": take_username, "edit_data": edit_data},
    )


def update_OperationTheater_datails(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_OperationTheater_details.objects.get(id=row_id)
    ex1 = add_OperationTheater_details.objects.filter(id=row_id).update(
        Patient_Number=request.POST.get("Patient_Number"),
        Gender=request.POST.get("Gender"),
        Contact_Number=request.POST.get("Contact_Number"),
        Operation_Name=request.POST.get("Operation_Name"),
        Operation_Type=request.POST.get("Operation_Type"),
        Assigned_Doctor=request.POST.get("Assigned_Doctor"),
        OperationDate=request.POST.get("OperationDate"),
        Applied_Charges=request.POST.get("Applied_Charges"),
        loger_id=request.POST.get("loger_id"),
    )
    print(ex1)
    view_OperationTheater_details = add_OperationTheater_details.objects.filter(
        loger_id=id
    )
    print("successfully updated.....")
    messages.error(
        request,
        "Successfully edited Operation Theater details",
        extra_tags="add_OperationTheater",
    )
    return render(
        request,
        "OperationTheater.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_OperationTheater_details": view_OperationTheater_details,
        },
    )


def delete_OperationTheater_details(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_OperationTheater_details.objects.get(id=row_id)
    edit_data.delete()
    view_OperationTheater_details = add_OperationTheater_details.objects.filter(
        loger_id=id
    )
    messages.error(
        request,
        "Successfully deleted Operation Theater details",
        extra_tags="add_OperationTheater",
    )
    return render(
        request,
        "OperationTheater.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_OperationTheater_details": view_OperationTheater_details,
        },
    )


# Pharmacy


def Pharmacy(request, id):
    view_Pharmacy_details = add_Pharmacy_details.objects.filter(loger_id=id)
    take_username = registration_table.objects.get(id=id)
    return render(
        request,
        "Pharmacy.html",
        {
            "take_username": take_username,
            "view_Pharmacy_details": view_Pharmacy_details,
        },
    )


def Pharmacy_add(request, id):
    take_username = registration_table.objects.get(id=id)
    return render(request, "Pharmacy_add.html", {"take_username": take_username})


def add_Pharmacy(request, id):
    take_username = registration_table.objects.get(id=id)
    if request.method == "POST":
        ex1 = add_Pharmacy_details(
            PATIENT_NAME=request.POST.get("PATIENT_NAME"),
            Docter_Name=request.POST.get("Docter_Name"),
            BILL_TOTAL=request.POST.get("BILL_TOTAL"),
            loger_id=request.POST.get("loger_id"),
        )
        ex1.save()
        messages.error(
            request, "Successfully added Pharmacy details", extra_tags="add_Pharmacy"
        )
        view_Pharmacy_details = add_Pharmacy_details.objects.filter(loger_id=id)
        return render(
            request,
            "Pharmacy.html",
            {
                "take_username": take_username,
                "view_Pharmacy_details": view_Pharmacy_details,
            },
        )


def Pharmacy_edit(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_Pharmacy_details.objects.get(id=row_id)
    return render(
        request,
        "Pharmacy_edit.html",
        {"take_username": take_username, "edit_data": edit_data},
    )


def update_Pharmacy_datails(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_Pharmacy_details.objects.get(id=row_id)
    ex1 = add_Pharmacy_details.objects.filter(id=row_id).update(
        PATIENT_NAME=request.POST.get("PATIENT_NAME"),
        Docter_Name=request.POST.get("Docter_Name"),
        BILL_TOTAL=request.POST.get("BILL_TOTAL"),
        loger_id=request.POST.get("loger_id"),
    )
    print(ex1)
    view_Pharmacy_details = add_Pharmacy_details.objects.filter(loger_id=id)
    print("successfully updated.....")
    messages.error(
        request, "Successfully edited Pharmacy details", extra_tags="add_Pharmacy"
    )
    return render(
        request,
        "Pharmacy.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_Pharmacy_details": view_Pharmacy_details,
        },
    )


def delete_Pharmacy_details(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_Pharmacy_details.objects.get(id=row_id)
    edit_data.delete()
    view_Pharmacy_details = add_Pharmacy_details.objects.filter(loger_id=id)
    messages.error(
        request, "Successfully deleted Pharmacy details", extra_tags="add_Pharmacy"
    )
    return render(
        request,
        "Pharmacy.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_Pharmacy_details": view_Pharmacy_details,
        },
    )


# ambulance


def ambulance(request, id):
    view_ambulance_details = add_Ambulance_details.objects.filter(loger_id=id)
    take_username = registration_table.objects.get(id=id)
    return render(
        request,
        "ambulance.html",
        {
            "take_username": take_username,
            "view_ambulance_details": view_ambulance_details,
        },
    )


def ambulance_edit(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_Ambulance_details.objects.get(id=row_id)
    return render(
        request,
        "ambulance_edit.html",
        {"take_username": take_username, "edit_data": edit_data},
    )


def ambulance_add(request, id):
    take_username = registration_table.objects.get(id=id)
    return render(request, "ambulance_add.html", {"take_username": take_username})


def add_ambulance(request, id):
    take_username = registration_table.objects.get(id=id)
    if request.method == "POST":
        ex1 = add_Ambulance_details(
            Vehical_Number=request.POST.get("Vehical_Number"),
            Vehical_Model=request.POST.get("Vehical_Model"),
            Year_Made=request.POST.get("Year_Made"),
            Driver_Name=request.POST.get("Driver_Name"),
            Driver_License=request.POST.get("Driver_License"),
            Driver_Contact=request.POST.get("Driver_Contact"),
            Vehical_Type=request.POST.get("Vehical_Type"),
            loger_id=request.POST.get("loger_id"),
        )
        ex1.save()
        messages.error(
            request, "Successfully added ambulance details", extra_tags="add_ambulance"
        )
        view_ambulance_details = add_Ambulance_details.objects.filter(loger_id=id)
        return render(
            request,
            "ambulance.html",
            {
                "take_username": take_username,
                "view_ambulance_details": view_ambulance_details,
            },
        )


def update_Ambulance_datails(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_Ambulance_details.objects.get(id=row_id)
    ex1 = add_Ambulance_details.objects.filter(id=row_id).update(
        Vehical_Number=request.POST.get("Vehical_Number"),
        Vehical_Model=request.POST.get("Vehical_Model"),
        Year_Made=request.POST.get("Year_Made"),
        Driver_Name=request.POST.get("Driver_Name"),
        Driver_License=request.POST.get("Driver_License"),
        Driver_Contact=request.POST.get("Driver_Contact"),
        Vehical_Type=request.POST.get("Vehical_Type"),
        loger_id=request.POST.get("loger_id"),
    )
    print(ex1)
    view_ambulance_details = add_Ambulance_details.objects.filter(loger_id=id)
    print("successfully updated.....")
    messages.error(
        request, "Successfully edited ambulance details", extra_tags="add_ambulance"
    )
    return render(
        request,
        "ambulance.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_ambulance_details": view_ambulance_details,
        },
    )


def delete_Ambulance_details(request, id, row_id):
    take_username = registration_table.objects.get(id=id)
    edit_data = add_Ambulance_details.objects.get(id=row_id)
    edit_data.delete()
    messages.error(
        request, "Successfully deleted ambulance details", extra_tags="add_ambulance"
    )
    view_ambulance_details = add_Ambulance_details.objects.filter(loger_id=id)
    return render(
        request,
        "ambulance.html",
        {
            "take_username": take_username,
            "edit_data": edit_data,
            "view_ambulance_details": view_ambulance_details,
        },
    )
