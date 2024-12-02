from django.contrib import admin
from django.urls import path

from home_view.views import HomeView, LoginView, PfSignUpView, PjSignUpView, UserTypeView, FriedsListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('userType', UserTypeView.as_view(), name='user_type'),
    path('pfSignUp', PfSignUpView.as_view(), name='pf_SignUp'),
    path('pjSignUp', PjSignUpView.as_view(), name='pj_SignUp'),
    path('friendsList', FriedsListView.as_view(), name='friends_list'),
    path('login', LoginView.as_view(), name='login'),
]
