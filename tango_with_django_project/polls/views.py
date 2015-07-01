from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import Context
from polls.models import Poll


def index(request):
    poll_list= Poll.objects.all()
    new_questions = Context({'poll_list':poll_list})
    return render_to_response('index.html',new_questions)


def details(request, poll_id):
    return render_to_response('details.html')


def results(request, poll_id):
    return render_to_response('results.html')


def vote(request, poll_id):
    return render_to_response('vote.html')