from django.shortcuts import render
# Create your views here.


posts = [

    {'author': 'Frank Kovmir',
     'title': 'Anleitung zur Nutzung der Platform',
     'content': '\ndddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\n'
                'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\n'
                'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\n'
                'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\n'
                'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\n'
                'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\n'
                'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\n'
                'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\n'
                'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\n'
                'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\n'
                'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\n'
                'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\n'
                'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\n'
                'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\n\n'
                'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\n'
                'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\n'
                'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\n\n'
                'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\n\n'
                'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\n\n\n'
                'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd\n\n\n\n',
     'date_posted': 'October 11, 2022'
     }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'dashboard/home.html', context) #3rd argument passes data into the template

def discrepancies(request):
    return render(request, 'dashboard/recon.html', {'title':'Discrepancies'})