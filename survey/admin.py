from django.contrib import admin
from .models import SurveyQuestion, SurveyDefaultAnswer, SurveyUserAnswer

# Register your models here.
admin.site.register(SurveyQuestion)
admin.site.register(SurveyDefaultAnswer)
admin.site.register(SurveyUserAnswer)