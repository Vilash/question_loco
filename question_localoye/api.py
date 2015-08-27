from tastypie.resources import ModelResource
from questions.models import Question 
from tastypie.constants import ALL
class QuestionResource(ModelResource):
	class Meta:
		queryset		=	Question.objects.all()
		resource_name	=	'questions'
		filtering		=	{"category": "contains"}