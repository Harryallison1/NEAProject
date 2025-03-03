from django.db import models
from django.contrib.auth.models import User
from revisionmode.models import Question  

#This model stores data about a quiz attempt by a user
class QuizProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_date = models.DateTimeField(auto_now_add=True)
    total_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)
    #topic = models.ForeignKey(Question, related_name='topic_progress', on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)

#This model tracks the overall quiz performance
class UserStats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_quizzes_played = models.IntegerField(default=0)
    bronze_stars = models.IntegerField(default=0)
    silver_stars = models.IntegerField(default=0)
    gold_stars = models.IntegerField(default=0)
    



