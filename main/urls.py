from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import contact

urlpatterns = [
    path('',views.home),
    path('services/',views.services,name = 'services'),
    path('contact/',contact,name = 'contact'),
    path('about/',views.about,name = 'about'),
    path('register/',views.registerPage,name = 'register'),
    path('login/',views.loginPage,name = 'login'),
    path('logout/',views.logoutUser,name = 'logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uid64>/<token>', auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]
