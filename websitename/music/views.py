from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from .models import Question, Choice
# Create your views here.
def index(request):
    # return HttpResponse("Hellow World. You are at the music index")
    #in the reverse order -pub_date from first five(not including five)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    #template = loader.get_template('music/index.html')
    # Disctionaries
    stuff_for_frontend = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context, request)) OR
    return render(request, 'music/index.html', stuff_for_frontend)

def detail(request, question_id):
    #return HttpResponse("You are looking at question %s." % question_id)

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'music/detail.html', {'question': question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'music/detail.html', {'question': question})

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'music/result.html', {'question': question})
    # response = "You are looking at the result of question %s."
    # return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'music/detail.html',{
            'question': question,
            'err_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('result', args=(question.id,)))
    #return render(request, 'music/vote.html',{'question' : question_id})
    #return HttpResponse("You are voting on question %s." % question_id)
