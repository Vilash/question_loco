from django.conf.urls import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from . import api

question_resource	=	api.QuestionResource()

urlpatterns = [
    url(r'^questions/', include('questions.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(question_resource.urls)),
    url(r'^$', views.hello_world, name='home'),



]

urlpatterns += staticfiles_urlpatterns()