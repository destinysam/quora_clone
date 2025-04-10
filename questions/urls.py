from django.urls import path
from . import views


urlpatterns = [
    path('post-question/', views.post_question, name='post_question'),
    path('question/<int:question_id>/', views.view_question, name='view_question'),
    path('like-answer/<int:answer_id>/', views.like_answer, name='like_answer'),
]