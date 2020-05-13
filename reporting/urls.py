from django.urls import path
from .views import (registration_view, login_view, signup_view, validate_otp)
from rest_framework.authtoken.views import obtain_auth_token

app_name= ""
urlpatterns = [
path('registration', registration_view, name= "register"),
path('login', obtain_auth_token, name= "login"),
path('sendotp', signup_view, name= "sendotp"),
path('validateotp', validate_otp, name= "validateotp")

#  path('getsites', views.get_sitess),
#  path('addsite', views.savesite),
#  path('updatesite/<int:siteId>', views.update_site),
#  path('deletesite/<int:siteId>', views.delete_site),
#    path('getsite/<int:siteId>', views.get_site),  
]
