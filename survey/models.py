from django.db import models

# Create your models here.
class SurveyQuestion(models.Model):
    question = models.CharField(max_length=32)

    def clean(self):
        super(SurveyQuestion, self).clean()
        if '?' not in self.question[0]:
            question += '?'
        

'''
    SurveyDefaultAnswer está ligado a una y solo una pregunta. 
    SurveyDefaultAnswer se debe instanciar solamente al crear un SurveyQuestion.
'''
class SurveyDefaultAnswer(models.Model):
    q_question = models.OneToOneField(SurveyQuestion, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=40)
    answer2 = models.CharField(max_length=40)
    answer3 = models.CharField(max_length=40)
    answer4 = models.CharField(max_length=40)

'''
    SurveyUserAnswer es una respuesta al SurveyQuestion, la cual la hiso
    un User.
    La respuesta es un CharField(no debería poder cambiarse).
'''
class SurveyUserAnswer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    s_question = models.OneToOneField(SurveyQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=40)  # Debería no poder cambiarse una vez creado


        