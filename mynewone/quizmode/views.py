from django.shortcuts import render
from revisionmode.utils import get_questions_by_topic, get_question_feedback, get_remaining_questions

def quiz_view(request):
    # Get the selected topic from GET request
    topic = request.GET.get('topic', 'default_topic')  # Use a default if no topic is selected
    
    # Fetch questions for the selected topic
    questions = get_questions_by_topic(topic)
    answered_questions = []  # Store the questions already answered by the user

    # Initialize the current question index in the session if not already set
    if 'current_question_index' not in request.session:
        request.session['current_question_index'] = 0

    # Get the current question index from session
    current_question_index = request.session['current_question_index']

    if request.method == 'POST':
        # Get the user's answer from the form
        user_answer = request.POST.get('answer', None)

        if user_answer:
            question = questions[current_question_index]  # Get the current question
            feedback = get_question_feedback(question, user_answer)

            # Mark the current question as answered and update the index
            answered_questions.append(question)
            request.session['current_question_index'] += 1  # Move to the next question

            # Update the remaining questions
            remaining_questions = get_remaining_questions(questions, answered_questions)

            # Check if there are more questions
            if request.session['current_question_index'] >= len(questions):
                return render(request, 'quiz_page.html', {
                    'feedback': 'Quiz Complete!',
                    'remaining_questions': 0,
                    'topic': topic
                })

            # Return the response with feedback and remaining questions
            return render(request, 'quiz_page.html', {
                'feedback': feedback,
                'remaining_questions': len(remaining_questions),
                'topic': topic
            })

    # If it's a GET request, just display the first question
    return render(request, 'quiz_page.html', {
        'questions': questions,
        'topic': topic
    })
