from django.shortcuts import render, redirect
from main import models

def index(request):
    quizzes = models.Quiz.objects.filter(author=request.user)
    context = {
        'quizzes':quizzes
    }
    return render(request, 'index.html', context)


# >>>>>>>>  Quiz create list detail <<<<<<<<<<<<



# -------------- Quiz create --------------
def quiz_create(request):
    """ Quiz create view """
    if request.method == 'POST':
        name = request.POST['quiz']
        quiz = models.Quiz.objects.create(name=name, author=request.user)
        return redirect('quiz_detail' , quiz.code)
    
    return render(request, 'quiz/create.html' )


# -------------- Quiz list --------------
def quiz_list(request):
    """ Quiz list view """
    quizzes = models.Quiz.objects.all()
    context = {
        'quizzes':quizzes
    }
    return render(request, 'quiz/list.html', context)


# --------------- Quiz Details ---------------
def quiz_detail(request, code):
    """ Quiz detail view """
    quiz = models.Quiz.objects.get(code=code)
    questions = models.Question.objects.filter(quiz=quiz)
    context = {
        'code':code,
        'quiz':quiz,
        'questions':questions
    }
    return render(request, 'quiz/detail.html', context)


# >>>>>>>>>>>>> Question list detail create


# ------------- Question create --------
def question_create(request):
    """ Question create view """
    quiz = models.Quiz.objects.all()
    if request.method == 'POST':
        quiz = models.Quiz.objects.get(id=request.POST['quiz_id'])
        question = models.Question.objects.create(
            name=request.POST['name'],
            quiz_id=request.POST['quiz_id']
            )
        models.Option.objects.create(
            name = request.POST['correct_option'],
            question = question,
            is_correct = True
        )
        for option in request.POST.getlist('options'):
            models.Option.objects.create(
            name = option,
            question = question,
            is_correct = False
            )
        return redirect('quiz_detail', quiz.code)
    return render(request, 'question/create.html', {'quiz':quiz})


# ------------- Question detail --------
def question_detail(request, code):
    """ Question detail view """
    question = models.Question.objects.get(code=code)
    return render(request, 'question/detail.html', {'question':question,})


# ------------- Question list --------
def question_list(request):
    """ Question list view """
    questions = models.Question.objects.all()
    context = {
        'questions':questions
    }
    return render(request, 'question/list.html', context)

"""
Quiz Create +++, List +++, Detail +++
Question Create +++, Detail ---
Option Create +++ ---
"""