from .models import Question 
from django.db.models import F

def get_questions_by_topic(topic): #function that retrieves questions based on given topic
   
    questions = Question.objects.filter(topic=topic) #Djangos ORM gets all questions where topic matches topic provided
    #above line also returns a QuerySet which is a list like collection of database records
    return questions #returns filtered QuerySet which contains the questions for the specified topic

def check_answer(question, user_answer):
    #This function compares the users answer with the correct answer and then returns whether it is correct or not
    return question.correct_answer == user_answer

def get_question_feedback(question, user_answer):
    #Gives feedback to the user based on whether their answer was correct or not

    is_correct = check_answer(question, user_answer) #stores the result as a boolean
    feedback = {
        'correct': "Correct! Well done.",
        'incorrect': f"Incorrect. The correct answer was: {question.correct_answer}",
    }
    #above code creates a dictionary with 2 feedback messages for correct and incorrect.
    return feedback['correct'] if is_correct else feedback['incorrect']
    #above line of code returns the right feedback message based on whether answer was correct or not


