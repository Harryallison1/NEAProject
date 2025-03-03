from .models import QuizProgress
from django.db import models
from revisionmode.models import Question
from django.db.models import Max

def calculate_stars(total_quizzes_played):

    #Calculates number of bronze stars
    bronze_stars = total_quizzes_played // 5

    #Converts 5 bronze stars into 1 silver star
    silver_stars = bronze_stars // 5

    #Converts 5 silver stars into 1 gold star
    gold_stars = silver_stars // 5

    #Calculates remaining bronze and silver stars after conversion
    remaining_bronze_stars = bronze_stars % 5
    remaining_silver_stars = silver_stars % 5

    return remaining_bronze_stars, remaining_silver_stars, gold_stars

def topic_focus(user):
    topic_performance = QuizProgress.objects.filter(user=user).values('topic').annotate(
        latest_attempt=Max('id')  #This extracts the latest quiz attempt ID for each topic
    )

    topics_to_focus_on = []

    for topic_data in topic_performance:
        latest_quiz = QuizProgress.objects.filter(id=topic_data['latest_attempt']).first() #gets latest quiz for a certain topic
        
        if latest_quiz: #checks if quiz exists
            score_percentage = (latest_quiz.correct_answers / latest_quiz.total_questions) * 100
            if score_percentage < 70: #if sscore is lower than 70 percent
                topics_to_focus_on.append(latest_quiz.topic) #add the topics to the focus list

    return topics_to_focus_on

"""""
def topic_focus(user):
   
    topic_performance = QuizProgress.objects.filter(user=user).values('topic').annotate(
        total_incorrect=models.Sum('incorrect_answers')
    ).order_by('-total_incorrect')

    topics_to_focus_on = []
    for topic_data in topic_performance:
        if topic_data['total_incorrect'] > 3:
            question = Question.objects.filter(topic=topic_data['topic']).first()
            if question:
                topics_to_focus_on.append(question.topic) 

    return topics_to_focus_on
"""


"""""
def topic_focus(user):
    topic_performance = (
        QuizProgress.objects
        .filter(user=user)
        .values('topic')  # Directly use 'topic' if it's stored as a string
        .annotate(total_incorrect=models.Sum('incorrect_answers'))
        .order_by('-total_incorrect')
    )

    # Extract topics where incorrect answers > 0
    topics_to_focus_on = [
        topic_data['topic'] for topic_data in topic_performance if topic_data['total_incorrect'] > 0
    ]

    return topics_to_focus_on
"""


"""""
def topic_focus(user):
    topic_performance = QuizProgress.objects.filter(user=user).values('topic').annotate(
        total_incorrect=models.Sum('incorrect_answers')
    ).order_by('-total_incorrect')

    topics_to_focus_on = [topic_data['topic'] for topic_data in topic_performance if topic_data['total_incorrect'] > 0]
    
    return topics_to_focus_on
"""







