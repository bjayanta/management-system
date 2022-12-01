from django.urls import path
from .views import Create, List, Detail, Delete, Edit

urlpatterns = [
    path('create/', Create.as_view(), name='lead.create'),
    path('list/', List.as_view(), name='lead.list'),
    path('<int:pk>/', Detail.as_view(), name='lead.detail'),
    path('<int:pk>/delete', Delete.as_view(), name='lead.delete'),
    path('<int:pk>/edit', Edit.as_view(), name='lead.edit'),
]
