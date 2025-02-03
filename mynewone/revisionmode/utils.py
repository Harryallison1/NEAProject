from .models import Question
from django.db.models import F

def get_questions_by_topic(topic):
   
    questions = Question.objects.filter(topic=topic)
    return questions

def check_answer(question, user_answer):
    """
    This Compares the user's answer with the correct answer and returns whether it's correct.
    """
    return question.correct_answer == user_answer

def get_question_feedback(question, user_answer):
    """
    Returns feedback to the user based on whether their answer is correct or not.
    """
    is_correct = check_answer(question, user_answer)
    feedback = {
        'correct': "Correct! Well done.",
        'incorrect': f"Incorrect. The correct answer was: {question.correct_answer}",
    }
    return feedback['correct'] if is_correct else feedback['incorrect']

def get_remaining_questions(questions, answered_questions): 
    """
    Returns the remaining questions that have not been answered yet.
    """
    remaining = [q for q in questions if q not in answered_questions]
    return remaining
