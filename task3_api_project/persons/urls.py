from django.urls import path
from .views import PersonListCreateView, PersonDetailView

urlpatterns = [
    path('person/', PersonListCreateView.as_view(), name='person-list-create'),
    path('person/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
]