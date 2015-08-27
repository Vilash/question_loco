from django.conf.urls import *
from api import QuestionResource

question_resource = QuestionResource()

urlpatterns = [
	(r'^api/', include(question_resource.urls)),
]
