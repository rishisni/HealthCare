from django.contrib import admin
from .models import CustomUser, Patient, Doctor, PatientDoctorMapping


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'gender', 'dob', 'is_active')
    search_fields = ('email', 'first_name', 'last_name', 'phone_number')
    list_filter = ('gender',  'is_active')


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'email', 'created_at')
    search_fields = ('name', 'phone_number', 'email')
    list_filter = ('created_at',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialization', 'phone_number', 'email', 'created_at')
    search_fields = ('name', 'specialization', 'phone_number', 'email')
    list_filter = ('specialization', 'created_at')


@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'get_patient_email', 'get_doctor_name', 'assigned_at')
    search_fields = ('patient__user__email', 'doctor__name')
    list_filter = ('assigned_at',)

    def get_patient_email(self, obj):
        return obj.patient.user.email
    get_patient_email.short_description = 'Patient Email'

    def get_doctor_name(self, obj):
        return obj.doctor.name
    get_doctor_name.short_description = 'Doctor Name'

