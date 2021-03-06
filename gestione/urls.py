"""gestione URL Configuration

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
from gestione import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-data', views.get_data, name='get-data'),
    path('<str:field>/<str:query>/<str:is_syn>/<int:page>', views.homepage, name='homepage'),
    path('<str:field>/<str:query>/<int:page>', views.homepage, name='homepage'),
    path('<str:field>/<str:query>/<str:is_syn>', views.homepage, name='homepage'),
    path('<str:field>/<str:query>', views.homepage, name='homepage'),
    path('<str:field>/', views.homepage, name='homepage'),
    path('', views.homepage, name='homepage'),
]
