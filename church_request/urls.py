"""church_request URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from request import views
from django import forms

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('test/', views.tagsInputTest, name='test'),
    path('<int:church_id>/announcement', views.announcement, name='announcement'),
    path('<int:church_id>/menu', views.church_main, name='church-main'),
    path('<int:church_id>/request', views.request_create, name='request-create'),
    path('', views.acceuil, name='request-acceuil'),
    path('<str:_customer>/<slug:requet>/<str:_type_choices>/<slug:_hours>/<slug:_start_date>/<slug:_end_date>/confirm', views.request_confirm, name='request-confirm'),
    path('<int:request_id>/detail', views.request_detail, name='request-detail'),
    path('confirmation', views.confirmation, name='request-confirmation'),
]
