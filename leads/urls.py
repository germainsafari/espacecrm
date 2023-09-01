from django.urls import path
from .views import lead_list, lead_detail, lead_create, lead_update, lead_delete
  
app_name = 'leads'


urlpatterns = [
    path('', lead_list, name='lead-list'),
    path('<int:pk>/', lead_detail, name='lead-detail'),  # Corrected
    path('<int:pk>/update/', lead_update, name='lead-update'),  # Corrected
    path('<int:pk>/delete/', lead_delete, name='lead-delete'),  # Corrected
    path('create/', lead_create, name='lead-create'),
]
