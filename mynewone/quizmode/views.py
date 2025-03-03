from django.shortcuts import render
from revisionmode.utils import get_questions_by_topic, get_question_feedback #imports functions used in the view
from django.http import JsonResponse #imports the JsonResponse class used to return a JSON response to the user 
from progresstracker.models import QuizProgress, UserStats
from progresstracker.utils import calculate_stars, topic_focus
from revisionmode.models import Question


def quiz_view(request):
    selected_topic = request.session.get('selected_topic')
    print(selected_topic)
   
    questions = get_questions_by_topic(selected_topic)  #Fetches questions from selected topic
    total_questions = len(questions) #total number of questions in topic selected

    if 'current_index' not in request.session or request.session.get('current_index') == 0: #checks if currentindex exists in the current session. If not initalises it to 0
        request.session['current_index'] = 0 
        request.session['correct_answers'] = 0
        request.session['incorrect_answers'] = 0
   
    current_index = request.session.get('current_index', 0) #Retrieves the current question index

    #If all questions have been answered, reset progress
    if current_index >= total_questions: #Checks if all questions have been answered by comparing currentindex with totalquestions
        request.session['current_index'] = 0
        topic_questions = Question.objects.filter(topic=selected_topic)

        #new code
        topic = selected_topic

        topic_question = topic_questions.first() if topic_questions.exists() else None
        if topic_question:
            quiz_progress = QuizProgress.objects.create(
                user=request.user,
                total_questions=total_questions,
                correct_answers=request.session.get('correct_answers', 0),
                incorrect_answers=request.session.get('incorrect_answers', 0),
                topic=topic #use to be topic=topic_question
            )
        

        #Updates user stats
        #user_stats = UserStats.objects.get_or_create(user=request.user)[0]
        user_stats, created = UserStats.objects.get_or_create(user=request.user)

        user_stats.total_quizzes_played += 1
        
        #Calls the calculate_stars function
        bronze_stars, silver_stars, gold_stars = calculate_stars(user_stats.total_quizzes_played)
        user_stats.bronze_stars = bronze_stars
        user_stats.silver_stars = silver_stars
        user_stats.gold_stars = gold_stars
        user_stats.save()
        #Calls the topic_focus function
        topics_to_focus_on = topic_focus(request.user)
        correct_answers = request.session.get('correct_answers', 0)
        return render(request, 'quizmode/quiz_complete.html', {'total_questions': total_questions, 'correct_answers': correct_answers}) #add total correct

    #Gets the current question
    question = questions[current_index]

    if request.method == 'POST': #Checks if request method is post which is used when submitting answers
        user_answer = request.POST.get('answer') #retrieves the users answer
        feedback = get_question_feedback(question, user_answer)  #Gets feedback for the answer using the function defined in utils.py from rmode
        is_correct = question.correct_answer == user_answer #Compares users answers with the correct answer to check if it is correct

        #Tracks correct/incorrect answers
        if is_correct:
            request.session['correct_answers'] = request.session.get('correct_answers', 0) + 1
        else:
            request.session['incorrect_answers'] = request.session.get('incorrect_answers', 0) + 1

        #Moves to the next question
        request.session['current_index'] += 1 #Increments by 1 

        return JsonResponse({ #Returns jsonresponse with:
            'is_correct': is_correct, #Boolean indicating whether answer was correct
            'feedback': feedback,  #Feedback for the user
            'correct_answer': question.correct_answer, #Correct answer if the user was incorrect
            'remaining_questions': total_questions - request.session['current_index'] #NUmber of questions left in the quiz
        })

    return render(request, 'quizmode/quiz_page.html', { #This renders quizpage with current question and remaining number of questions
        'question': question,
        'remaining_questions': total_questions - current_index
    })
