# import cmath
from argparse import ONE_OR_MORE  # noqa: F401
from pickle import TRUE
from tkinter import CASCADE  # noqa: F401
from unicodedata import name  # noqa: F401
from django.db import models
from unittest.util import _MAX_LENGTH  # noqa: F401
from django.contrib.auth.models import User


# Create your models here.


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forgot_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=TRUE)

    def __str__(self):
        return self.user


class otp_details(models.Model):
    email_id = models.EmailField()
    otp = models.CharField(max_length=10)

    def __str__(self):
        return self.email_id


class contact_form_table(models.Model):
    name = models.CharField(max_length=100)  # noqa: F811
    email_id = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Appointment_form_submition(models.Model):
    Your_Name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date_time = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    doctor = models.CharField(max_length=100)

    def __str__(self):
        return self.Your_Name


class registration_table(models.Model):
    username = models.CharField(max_length=100)
    email_id = models.EmailField()
    Password = models.CharField(max_length=100)
    profile = models.FileField(upload_to="profiles")
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return self.username


class add_doctor_details(models.Model):
    # Doctor_Photo=models.FileField(upload_to="Doctors")
    Doctor_Name = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Specialization = models.CharField(max_length=100)
    Availability = models.CharField(max_length=100)
    Joined_Date = models.CharField(max_length=10)
    loger_id = models.IntegerField()

    def __str__(self):
        return self.Doctor_Name


class add_staff_details(models.Model):
    Staff_Id = models.CharField(max_length=20)
    Staff_Name = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    Joined_Date = models.CharField(max_length=10)
    Attendance = models.CharField(max_length=50)
    loger_id = models.IntegerField()

    def __str__(self):
        return self.Staff_Name


class add_Appointment_details(models.Model):
    Token_Number = models.CharField(max_length=15)
    Paitent_Name = models.CharField(max_length=100)
    Age = models.CharField(max_length=10)
    Referred_Doctor = models.CharField(max_length=100)
    Visiting_Purpose = models.CharField(max_length=100)
    Time = models.CharField(max_length=20)
    loger_id = models.IntegerField()

    def __str__(self):
        return self.Paitent_Name


class add_IPD_details(models.Model):
    Joining_Date = models.CharField(max_length=10)
    Paitent_Name = models.CharField(max_length=100)
    Age = models.CharField(max_length=10)
    Gender = models.CharField(max_length=10)
    Phone_Number = models.CharField(max_length=15)
    Docter_Name = models.CharField(max_length=100)
    Bed_Charges = models.CharField(max_length=15)
    Payment = models.CharField(max_length=15)
    Due_Payment = models.CharField(max_length=20)
    loger_id = models.IntegerField()

    def __str__(self):
        return self.Paitent_Name


class add_OPD_details(models.Model):

    Paitent_Name = models.CharField(max_length=100)
    Age = models.CharField(max_length=10)
    Gender = models.CharField(max_length=10)
    Contact_Number = models.CharField(max_length=15)
    Docter_Name = models.CharField(max_length=100)
    Last_Visit = models.CharField(max_length=20)
    Total_Visit = models.CharField(max_length=20)
    loger_id = models.IntegerField()

    def __str__(self):
        return self.Paitent_Name


class add_EmergencyWard_details(models.Model):
    Patient_Id = models.CharField(max_length=10)
    Ward_Num = models.CharField(max_length=15)
    Bed_Num = models.CharField(max_length=15)
    JOINED_DATE = models.CharField(max_length=10)
    Charges = models.CharField(max_length=15)
    loger_id = models.IntegerField()

    def __str__(self):
        return self.Patient_Id


class add_Covid_19_details(models.Model):
    Paitent_Name = models.CharField(max_length=100)
    Age = models.CharField(max_length=10)
    Gender = models.CharField(max_length=10)
    Bed_Number = models.CharField(max_length=15)
    Gaurdian_Name = models.CharField(max_length=100)
    JOINED_DATE = models.CharField(max_length=10)
    Todays_Report = models.CharField(max_length=1000)
    loger_id = models.IntegerField()

    def __str__(self):
        return self.Paitent_Name


class add_BirthRecord_details(models.Model):
    Child_Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=10)
    Birth_Date = models.CharField(max_length=20)
    Mother_Name = models.CharField(max_length=100)
    Father_Name = models.CharField(max_length=100)
    Report = models.CharField(max_length=1000)
    loger_id = models.IntegerField()

    def __str__(self):
        return self.Child_Name


class add_Radiology_details(models.Model):
    Patient_Id = models.CharField(max_length=10)
    Test_Name = models.CharField(max_length=50)
    Short_Name = models.CharField(max_length=10)
    Test_Type = models.CharField(max_length=50)
    Category = models.CharField(max_length=50)
    sub_Category = models.CharField(max_length=50)
    Report_Days = models.IntegerField()
    charge = models.CharField(max_length=15)
    loger_id = models.IntegerField()

    def __str__(self):
        return self.Patient_Id


class add_Pathology_details(models.Model):
    Patient_Id = models.CharField(max_length=10)
    Test_Name = models.CharField(max_length=50)
    Short_Name = models.CharField(max_length=10)
    Test_Type = models.CharField(max_length=50)
    Category = models.CharField(max_length=50)
    sub_Category = models.CharField(max_length=50)
    Report_Days = models.IntegerField()
    charge = models.CharField(max_length=15)
    loger_id = models.IntegerField()

    def __str__(self):
        return self.Patient_Id


class add_OperationTheater_details(models.Model):
    Patient_Number = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10)
    Contact_Number = models.CharField(max_length=15)
    Operation_Name = models.CharField(max_length=50)
    Operation_Type = models.CharField(max_length=50)
    Assigned_Doctor = models.CharField(max_length=100)
    OperationDate = models.CharField(max_length=10)
    Applied_Charges = models.CharField(max_length=15)
    loger_id = models.IntegerField()

    def __str__(self):
        return self.Patient_Number


class add_Pharmacy_details(models.Model):
    PATIENT_NAME = models.CharField(max_length=100)
    Docter_Name = models.CharField(max_length=100)
    BILL_TOTAL = models.CharField(max_length=100)
    loger_id = models.IntegerField()

    def __str__(self):
        return self.PATIENT_NAME


class add_Ambulance_details(models.Model):
    Vehical_Number = models.CharField(max_length=20)
    Vehical_Model = models.CharField(max_length=20)
    Year_Made = models.CharField(max_length=10)
    Driver_Name = models.CharField(max_length=100)
    Driver_License = models.CharField(max_length=50)
    Driver_Contact = models.CharField(max_length=15)
    Vehical_Type = models.CharField(max_length=100)
    loger_id = models.IntegerField()

    def __str__(self):
        return self.Vehical_Number
