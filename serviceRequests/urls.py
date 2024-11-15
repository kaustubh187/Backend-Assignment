from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Login and Logout
    path('', views.redirect_dashboard, name='home'),
    path('login/', views.custom_login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),

    # Service Request Views (Customer-side)
    path('create/', views.create_service_request, name='create_service_request'),
    path('track/', views.track_requests, name='track_requests'),

    # Support Representative Views
    path('manage/', views.manage_requests, name='manage_requests'),
    path('update/<int:request_id>/', views.update_request_status, name='update_request_status'),

    # Dashboard Views
    path('customer-dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('support-dashboard/', views.support_dashboard, name='support_dashboard'),
    path('get_request_details/<int:request_id>/', views.get_request_details, name='get_request_details'),
]