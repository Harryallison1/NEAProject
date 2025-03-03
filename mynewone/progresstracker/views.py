from django.shortcuts import render
from progresstracker.models import UserStats, QuizProgress
from progresstracker.utils import topic_focus
from django.contrib.auth.decorators import login_required  #This ensures only loggedin users can access this view

@login_required
def progress_view(request):
    #Gets the UserStats for the logged in user
    #user_stats = UserStats.objects.get(user=request.user)
    user_stats, created = UserStats.objects.get_or_create(user=request.user)
    
    #Gets the total number of quizzes played by the user
    total_quizzes_played = user_stats.total_quizzes_played

    #Calculates the stars
    bronze_stars = user_stats.bronze_stars
    silver_stars = user_stats.silver_stars
    gold_stars = user_stats.gold_stars

    #Gets the topics to focus on based on the user's incorrect answers
    topics_to_focus_on = topic_focus(request.user)

    #Retrieves the quiz progress for the user 
    quiz_progress = QuizProgress.objects.filter(user=request.user).order_by('-quiz_date')[:5]  #Gets the last 5 quizzes

    return render(request, 'progresstracker/progress_page.html', {
        'user_stats': user_stats,  #Passes user stats to template
        'total_quizzes_played': total_quizzes_played,
        'bronze_stars': bronze_stars,
        'silver_stars': silver_stars,
        'gold_stars': gold_stars,
        'topics_to_focus_on': topics_to_focus_on,
        'quiz_progress': quiz_progress  
    })
