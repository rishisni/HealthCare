from django.urls import path
from .views import RegisterView, LoginView, PatientListCreateView, PatientDetailView,DoctorListCreateView,DoctorDetailView,PatientDoctorMappingDetailView,PatientDoctorMappingListCreateView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'), 
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('mappings/', PatientDoctorMappingListCreateView.as_view(), name='patient-doctor-mapping-list-create'),
    path('mappings/<int:pk>/', PatientDoctorMappingDetailView.as_view(), name='patient-doctor-mapping-detail'),

]
