from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "Jingjing",
        "title":  "Top 3 Youtube chanels for learning programming languages",
        "content": "Today is a good day! Today is a good day! Today is a good day! Today is a good day! Today is a good day! Today is a good day! Today is a good day! Today is a good day! Today is a good day! Today is a good day! ",
        "date_posted": "8 August 2020"
    },
    {
        "author": "Michael",
        "title":  "Sports",
        "content": "I love to play tennis!",
        "date_posted": "6 August 2020"
    }
]


def home(request):
    context = {
        "posts": posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {"title": "About"})
