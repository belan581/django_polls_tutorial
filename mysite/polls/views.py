from django.shortcuts import (
    render, get_object_or_404,
    redirect
)
from django.http import (
    HttpResponse, Http404, HttpResponseRedirect
)
from django.urls import reverse
from django.views.generic import ListView
from django.template import loader

from .models import Question, Choice
from .forms import QuestionForm

# Create your views here.

'''def index(request):
    questions = Question.objects.all()
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in questions])
    template = loader.get_template('polls/index.html')
    context = {
        'mensaje': "Lista de encuestas",
        'latest_questions': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
'''
class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_questions'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensaje'] = 'Lista de encuestas'
        return context

    def get_queryset(self):
        query = Question.objects.order_by('-pub_date')[:5]
        return query

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404("Question does not exist")
    context = {
        'mensaje': "Detalle de la encuesta",
        'question': question
    }
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def add_or_change_question(request, question_id=None):
    question = None
    if question_id:
        question = get_object_or_404(Question, pk=question_id)
        if request.method == "POST":
            form = QuestionForm(
            data=request.POST,
            files=request.FILES,
            instance=question
            )
            if form.is_valid():
                question = form.save()
                return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))
        else:
            form = QuestionForm(instance=question)
    context = {"question": question, "form": form}
    return render(request, "polls/polls_form.html", context)