from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/<str:username>/', views.PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('portfolio/<str:username>/delete/', views.PortfolioDeleteView.as_view(), name='portfolio-delete'),
]
