from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserSerializer,PatientSerializer,DoctorSerializer,PatientDoctorMappingSerializer
from .models import CustomUser,Patient,Doctor,PatientDoctorMapping
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

#RegisterView
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]  # Allow anyone to register

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)  # Generate JWT token
            return Response({
                "message": "User registered successfully!",
                "user": UserSerializer(user).data,
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh)
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# LoginView
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]  # Allow anyone to log in

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)  # Authenticate user

        if user is not None:
            refresh = RefreshToken.for_user(user)  # Generate JWT token
            return Response({
                "message": "Login successful!",
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh)
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
        
      
#  PatientListCreateView
class PatientListCreateView(generics.ListCreateAPIView):
    """
    List all patients or create a new patient.
    """
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.all()  

    def perform_create(self, serializer):
        serializer.save()  

# Retrieve, Update, Delete a Specific Patient
class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.all()


#DoctorListCreateView
class DoctorListCreateView(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]  
    queryset = Doctor.objects.all()


#DoctorDetailView
class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]  
    queryset = Doctor.objects.all()


#PatientDoctorMappingListCreateView
class PatientDoctorMappingListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.all()

    def perform_create(self, serializer):
        serializer.save()


#PatientDoctorMappingDetailView
class PatientDoctorMappingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = PatientDoctorMapping.objects.all()
