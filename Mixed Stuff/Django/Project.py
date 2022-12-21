import django

"""
#### Initialize
pip install django
type django-admin startproject + project name in cmd
starting webserver through cmd command: python manage.py runserver (connection to 127.0.0.1:8000 / localhost)
django administration through localhost:8000/admin
stopping server with ctr+c in cmd
new app through cmd: python manage.py startapp + name

##### Starting out
coding starts with blog -> views (Home function)
Then we need URL Mapping, so a new file in blog directory (urls.py like in django project)
In Project -> Urls File the mapping to the App Url has to be done once (so blog url in this case)

to create new page urls inside the app (blogs):
    1. within views add a function that handles the page
    2. Within the Blog Urls Model we need to setup a mapping for the path
    

##### Include more HTML Logic with Templates

    1. create a template directory in the app (blog) directory
    2. create a blog directory inside of the templates directory to store templates
    3. create html files in the template -> blog dir for the pages (home and about in this case)
    4. give a name within the html file inside head -> body as h1 
    5. Add Blog Application to the List of installed apps, so django looks for the template directory
        5.1 Copy BlogConfig into Project -> settings.py 
        5.2 into Installed_apps as string 'blog.apps.BlogConfig', (5.1 and 5.2 are done only once!)
        5.3 point to the blog by adding in blogs -> views to load the templates with django shortcuts
    6. Creating Dummy Blog Posts in blogs-> views.py and adding to the render function

##### Methods in Html Templates (see home.html / about.html)

    1. Write for loop in html home file with: {%for post in posts%}, end loop with {% endfor %}. In between elements
    can be accessed with e.g. <h1>{{post.title}}</h1> or <p>By {{post.author}} on {{ post.date_posted}}</p>
    2. Write Conditionals with {% if title %} {% else %} {% endif %}
    3. It makes sense to use template inheritance between different templates, so create a base.html and extend the different htmls files
    4. This base html has the main structure of all htmls on every page of the app. Specific changes to pages have to be then made in the 
    respective page html
    
##### Adding Bootstrap to our base template 

    1. copy Starter template inside <head> from https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template into base template head
    2. copy optional javascript until <body> into the body of base below content block into a <div class ="container">

##### Styling 
    
    1. For Navigation Bar copy code of navigation bar from snippets into base, above container (very top of body)
    2. Copy New main section for content block from snippets into base 
    3. For custom CSS Styles create a static folder in blog directory (where migration is too)
    4. Create subdirectory in static directory with same name as app (blogs)
    5. Create CSS File main.css and copy code
    6. Open up a Coblock at the top of base file to load in static
    7. Import as stylesheet in head of base <link rel="stylesheet" type = "text/css" href= "{% static 'blog/main.css'%}">
    8. Copy / Paste from Article Snipet into home for loop 
    
##### Admin Page

    1. /admin in link
    2. To login an admin user has to be first created
    3. python manage.py makemigrations
    4. python manage.py migrate
    5. python manage.py createsuperuser in CMD 
    6. hirnfrost / adby7834b 

##### Create Database Structure (Models)

    1. Models.py in App (Blog) Directory
    2. Create Class
    3. CMD: python manage.py makemigrations once done
    4. CMD: python manage.py migrate
    5. create __str__ Method in models
    


"""

