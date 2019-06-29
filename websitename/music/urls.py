from django.urls import path
from . import views

urlpatterns = [
    #   /music/
    path('',views.index,name='index'),
    #   /music/5/
    path('<int:question_id>/',views.detail,name='detail'),
    #   /music/5/results/
    path('<int:question_id>/result',views.result,name='result'),
    #   music/5/vote
    path('<int:question_id>/vote/',views.vote,name='vote'),

]