from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Contribution


# Create your views here.
def hello(request):
    return HttpResponse("Hello!, I'm the captain now")


def index(request):
    # Showing all the posts
    posts = Post.objects.order_by("created_date")
    contributions = Contribution.objects.order_by("contribute_date")

    return render(request,
                  template_name='web_mvc/index.html',
                  context={
                      'posts': posts,
                      'contributions': contributions
                  })
