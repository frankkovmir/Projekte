from django.shortcuts import render
# Create your views here.


posts = [

    {'author': 'CoreyMS',
     'title': 'Blog Post 1',
     'content': 'First post content',
     'date_posted': 'November 05, 2022'
     },
    {'author': 'Jane Doe',
     'title': 'Blog Post 2',
     'content': 'Second post content',
     'date_posted': 'November 06, 2022'
     }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blogs/home.html', context) #3rd argument passes data into the template

def about(request):
    return render(request, 'blogs/about.html', {'title':'About'})