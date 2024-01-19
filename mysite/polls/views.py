from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import context
from django.urls import reverse
from django.views import generic

# Create your views here.

from .models import Question, Choice
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class DetailView(generic.DetailView):
    model = Question
    template_name = "detail.html"

    def get_queryset(self):
        return


class ResultView(generic.DetailView):
    model = Question
    template_name = "results.html"


def index(request):
    latest_question_list = Question.objects.order_by("pub_date")[:3]
    output = ", ".join([q.question_text for q in latest_question_list])
    return render(request, 'index.html', {"latest_question_list": latest_question_list})


def detail(request, question_id):
    # 방법 1
    # try:
    #     question=Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question이 없어요")
    # response = "You're looking at the results of question %s."

    # 방법 2( 더 간단한 방법 )
    question = get_object_or_404(Question, pk=question_id)


    return render(request, "detail.html", {"question": question})
  #  return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
