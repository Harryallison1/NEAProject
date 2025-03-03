from django.shortcuts import render
from django.http import JsonResponse
from revisionmode.utils import get_questions_by_topic
from progresstracker.models import QuizProgress, UserStats
from progresstracker.utils import calculate_stars, topic_focus
from revisionmode.models import Question
from fuzzywuzzy import fuzz

def terms_view(request):
    selected_topic = request.session.get('selected_topic')
    questions = get_questions_by_topic(selected_topic)
    total_questions = len(questions)

    print(f'Selected topic: {selected_topic}') #debugging statements
    print(f'Total questions: {total_questions}') #debugging statements

    #following code intialises session variables for tracking the current index and answers if they do not exist
    #i do this to prevent the code from crashing if they do not exist
    if 'current_index' not in request.session or request.session.get('current_index') == 0:
        request.session['current_index'] = 0
        request.session['correct_answers'] = 0
        request.session['incorrect_answers'] = 0

    current_index = request.session.get('current_index', 0) 

    print(f'Current index: {current_index}') #again debugging

    if current_index >= total_questions:
        print('All questions answered, rendering complete page.')
        request.session['current_index'] = 0
        topic_questions = Question.objects.filter(topic=selected_topic) #gets all qs for selected topic 
        topic = selected_topic
        topic_question = topic_questions.first() if topic_questions.exists() else None #gets first question 
        
        if topic_question: #if there are questions this records progress of the quiz
            QuizProgress.objects.create(
                user=request.user,
                total_questions=total_questions,
                correct_answers=request.session.get('correct_answers', 0),
                incorrect_answers=request.session.get('incorrect_answers', 0),
                topic=topic
            )
        
        user_stats, created = UserStats.objects.get_or_create(user=request.user) #creates userstats object for current user
        user_stats.total_quizzes_played += 1
        bronze_stars, silver_stars, gold_stars = calculate_stars(user_stats.total_quizzes_played)
        user_stats.bronze_stars = bronze_stars
        user_stats.silver_stars = silver_stars
        user_stats.gold_stars = gold_stars
        user_stats.save()
        
        topics_to_focus_on = topic_focus(request.user) #gets list of topics the user needs to focus on
        correct_answers = request.session.get('correct_answers', 0)
        return render(request, 'termsmode/terms_complete.html', {'total_questions': total_questions, 'correct_answers': correct_answers})
        
    question = questions[current_index]

    if request.method == 'POST':
        user_answer = request.POST.get('answer', '').strip().lower()
        correct_answer = question.correct_answer.strip().lower()
        similarity_score = fuzz.ratio(user_answer, correct_answer) #Calculates similarity score between user answer and correct answer
        is_correct = similarity_score >= 80

        if is_correct:
            request.session['correct_answers'] += 1
            feedback = "Correct!"
            
        else:
            request.session['incorrect_answers'] += 1
            feedback = f"Incorrect! The correct answer was: {correct_answer}"
            

        request.session['current_index'] += 1   
        
        return JsonResponse({ #returns json response with the following
            'is_correct': is_correct,
            'feedback': feedback, 
            'correct_answer': question.correct_answer,
            'similarity_score': similarity_score,
            'remaining_questions': total_questions - request.session['current_index']
        })

    return render(request, 'termsmode/terms_page.html', {
        'question': question, #renders current question to the page
        'remaining_questions': total_questions - current_index #renders remaining questions to the page
    })
