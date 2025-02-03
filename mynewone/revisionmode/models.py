from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.TextField()
    correct_answer = models.CharField(max_length=255)
    wrong_answer1 = models.CharField(max_length=255)
    wrong_answer2 = models.CharField(max_length=255)
    wrong_answer3 = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text