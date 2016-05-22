
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Answer


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = get_template('faqs/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        answer   = Answer.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Essa pergunta não foi feita ou ainda não foi respondida.")
    return render(request, 'faqs/detail.html', {'question': question, 'answer': answer})


def results(request, question_id):
    response = "Esse é o resultado da pergunta %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Vote na pergunta %s." % question_id)
