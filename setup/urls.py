from django.contrib import admin
from django.urls import path

from home_view.views import HomeView, PfSignUpView, PjSignUpView, UserTypeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('userType', UserTypeView.as_view(), name='user_type'),
    path('pfSignUp', PfSignUpView.as_view(), name='pf_SignUp'),
    path('pjSignUp', PjSignUpView.as_view(), name='pj_SignUp'),
]
