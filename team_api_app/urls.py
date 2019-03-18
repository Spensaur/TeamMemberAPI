from django.urls import path

from . import views

urlpatterns = [
    path('team_members/', views.TeamMemberList.as_view()),
    path('team_members/<int:pk>/', views.TeamMemberDetail.as_view()),
]