from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    #  >>>>>>>> quiz list create detail
    path('quiz/create/', views.quiz_create, name='quiz_create'),
    path('quiz_detail/<str:code>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/list/', views.quiz_list, name='quiz_list'),

    #  >>>>>>>> question list create detail
    path('question/create/', views.question_create, name='question_create'),
    path('question_list/', views.question_list, name='question_list'),
    path('question_detail/<str:code>/', views.question_detail, name='question_detail'),

]