from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	return render(request, 'htmltest/index.html', {})

def newsfeed(request):
	return render(request, 'htmltest/newsfeed.html', {})

def chatroom(request):
    return render(request, 'htmltest/chatroom.html', {})

