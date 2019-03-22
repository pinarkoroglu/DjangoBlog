from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from blog.models import Post

posts=[
    {
      'author':'CoreyMS',
      'title':'Blog Post 1',
      'content':'First post content',
      'date_posted':'August 27,2018'
    },
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27,2018'
    }

]
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

