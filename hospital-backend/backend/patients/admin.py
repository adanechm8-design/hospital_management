from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    CustomUser, Patient, Doctor, Appointment,
    Receptionist, Pharmacist, Nurse, Technician,
    Medication, Prescription, PrescriptionItem
)

# --------------------------
# CustomUser Admin (FIXED PROPERLY)
# --------------------------
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')

    # ✅ IMPORTANT FIX: use Django default password handling
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Role Info', {'fields': ('role',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # ✅ THIS ENABLES password1 / password2 (VERY IMPORTANT)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'role',
                'password1',
                'password2',
                'is_staff',
                'is_active'
            ),
        }),
    )

    search_fields = ('username', 'email')
    ordering = ('username',)


# --------------------------
# Patient Admin
# --------------------------
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'contact_info', 'assigned_doctor')
    list_filter = ('gender',)
    search_fields = ('name', 'contact_info', 'address')


# --------------------------
# Doctor Admin
# --------------------------
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'availability', 'contact_info', 'phone', 'user')
    search_fields = ('name', 'specialization', 'contact_info')


# --------------------------
# Appointment Admin
# --------------------------
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time', 'reason', 'status')
    list_filter = ('date', 'doctor', 'status')
    search_fields = ('patient__name', 'doctor__name', 'reason')


# --------------------------
# Staff Admin
# --------------------------
@admin.register(Receptionist)
class ReceptionistAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info', 'user')


@admin.register(Pharmacist)
class PharmacistAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info', 'user')


@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info', 'user')


@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info', 'user')


# --------------------------
# Medication Admin
# --------------------------
@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'stock')
    search_fields = ('name',)


# --------------------------
# Prescription Admin
# --------------------------
@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'appointment', 'date', 'status')
    list_filter = ('status', 'date', 'doctor')
    search_fields = ('patient__name', 'doctor__name', 'notes')


@admin.register(PrescriptionItem)
class PrescriptionItemAdmin(admin.ModelAdmin):
    list_display = ('prescription', 'medication', 'dosage', 'quantity')
    search_fields = ('medication__name', 'dosage')