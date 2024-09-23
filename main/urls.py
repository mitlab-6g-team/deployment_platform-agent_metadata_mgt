"""data_mgt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from main.utils.config import config

ABSTRACT_METADATA_VERSION=config.ABSTRACT_METADATA.VERSION
FILE_METADATA_VERSION=config.FILE_METADATA.VERSION
MONGO_OPERATION_VERSION=config.MONGO_OPERATION.VERSION

urlpatterns = [
    path(f'api/{FILE_METADATA_VERSION}/', include('main.apps.file_metadata.api.urls')),
    path(f'api/{ABSTRACT_METADATA_VERSION}/', include('main.apps.abstract_metadata.api.urls')),
    path(f'api/{MONGO_OPERATION_VERSION}/', include('main.apps.mongo_operation.api.urls'))
]
