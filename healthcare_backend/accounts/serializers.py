from rest_framework import serializers
from .models import CustomUser,Patient,Doctor,PatientDoctorMapping

#UserSerializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'gender', 'dob', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

#PatientSerializer
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'phone_number', 'email', 'created_at']


#DoctorSerializer
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialization', 'phone_number', 'email', 'created_at']


#PatientDoctorMappingSerializer
class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_email = serializers.ReadOnlyField(source='patient.user.email')
    doctor_name = serializers.ReadOnlyField(source='doctor.name')

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'patient_email', 'doctor_name', 'assigned_at']
