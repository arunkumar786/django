from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# detail view
def detail(request, question_id,):
    return HttpResponse("you are looking at question %s" %question_id)

# results view
def results(request, question_id):
    response = "you are looking at question %s."
    return HttpResponse(response %question_id)

# vote view.
def vote(request, question_id):
    return HttpResponse("you're voting on question %s" %question_id)