from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Question, Tag, User, Answer, Like

TAGS = [
    {
        "title": f"tag#{i}",
        "number": i,
    } for i in range(20)
]
PAGINATION_SIZE = 10


def pagination(list_obj, request):
    paginator = Paginator(list_obj, PAGINATION_SIZE)
    page = request.GET.get('page')
    content = paginator.get_page(page)

    return content


def index(request):
    content = pagination(Question.objects.all().values(), request)
    tags = Tag.objects.all().values()
    return render(request, "index.html", {"questions": content, "tags": tags})


def ask(request):
    tags = Tag.objects.all().values()
    return render(request, "ask.html", {"tags": tags})


def authefication(request):
    tags = Tag.objects.all().values()
    return render(request, "authefication.html", {"tags": tags})


def registration(request):
    tags = Tag.objects.all().values()
    return render(request, "registration.html", {"tags": tags})


def hot(request):
    content = pagination(Question.objects.get_popular(), request)
    content = sorted(content, key=lambda question: question.likes, reverse=True)
    tags = Tag.objects.all().values()
    return render(request, "index.html", {"questions": content, "tags": tags})


def question(request, i: int):
    quest = Question.objects.get_question_by_id(i)[0]
    answers = pagination(Answer.objects.get_answers_by_question(i), request)
    tags = Tag.objects.all().values()
    tags_for_quest = quest.get_tags().values()
    return render(request, "question.html", {'question': quest, "answers": answers, "tags": tags,
                                                  "tags_for_quest": tags_for_quest})


def tags(request, i: int):
    tag = Tag.objects.get_tag_by_id(i)[0]
    return render(request, "inc/tags.html", {"tag": tag})


def questions_with_tags(request, tag_title):
    content = pagination(Question.objects.get_questions_by_tag_title(tag_title), request)
    tags = Tag.objects.all().values()
    return render(request, "index.html", {"questions": content, "tags": tags})


def settings(request):
    tags = Tag.objects.all().values()
    return render(request, "settings.html", {"tags": tags})