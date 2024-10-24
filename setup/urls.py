from django.contrib import admin
from django.urls import path

from home_view.views import HomeView, PjPfView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('userType', PjPfView.as_view(), name='user_type')
]
