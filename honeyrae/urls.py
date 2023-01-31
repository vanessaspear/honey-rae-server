from rest_framework import routers

from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from repairsapi.views import CustomerView
from repairsapi.views import register_user, login_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'customers', CustomerView, 'customer')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
]
