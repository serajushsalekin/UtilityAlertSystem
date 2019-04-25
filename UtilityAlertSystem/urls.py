"""UtilityAlertSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from accounts.views import index, tem, sms_list, users, search
from complain.views import ComplainCreate, ComplainList, ComplainDelete, ComplainDetail, complain_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path("", tem, name="home"),
    path('sms/', sms_list, name='sms'),
    path('alert/', index, name="msg"),
    path('users', users, name='users'),
    path('search', search, name='search'),
    path('complain/', ComplainCreate.as_view(), name='complain'),
    path('complain/list/', ComplainList.as_view(), name='complain-list'),
    path('complain/list/<int:pk>', ComplainDetail.as_view(), name='complain-detail'),
    path('complain/list/delete/<int:id>', complain_delete, name='complain-delete')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
