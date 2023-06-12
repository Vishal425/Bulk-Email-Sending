"""email_send URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include, include
from django.urls import path
#from file_upload import views as uploader_views
from django.conf.urls.static import static
from django.conf import settings
from file_upload import views

from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tutorials/upload/', views.uploadTutorial, name='upload_tutorial'),
    path('tutorials/', views.tutorialList, name='tutorial_list'),
    path('tutorials/<int:pk>', views.deleteTutorial, name='tutorial'),
    # path('', uploader_views.UploadView.as_view(), name='fileupload'),
    # path('accounts/', include('file_upload.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('', TemplateView.as_view(template_name=r'D:\Python_Project\py\web_scraping\Email_Send\email_send\file_upload\templates\file_upload\home.html'), name='home')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#main service url
#http://192.168.1.46:8000/tutorials/upload/