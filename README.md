# Django - the fastest hand in the west

Welcome to the Coderun 2024 Django tutorial. This tutorial is meant to introduce you to the world of web development
in the context of Django.

## Why Django?
Django is a high-level, fast, scalable and secure web framework, with a clean and practical design. Many real world
platforms use Django, such as __Youtube__, __Instagram__, __Pinterest__, __Spotify__, and a lot more.

### BuT wHy NoT fLaSk?(or any other similar web framework)
Its popular use among big names that use it, like the above-mentioned should already partially answer
your questions. The critical aspect here is scalability. Django scales really well to apps that possibly have to support
millions of users. In comparison, Flask, for example, is a micro-framework, much more limited and more suitable for smaller projects.
Just as importantly, however, this is a framework that isn't very well covered in your usual university curricula, so
building apps in this one as well broadens your perspectives.

Having settled these, let's build stuff now!

## Installation
Django is a Python framework. You can download it from [here](https://www.python.org/downloads/).

## Creating a virtual environment (optional, but highly recommended)
```shell
pip install virtualenv
```
Now create a virtual environment
```shell
python -m venv venv
```
or similarly
```shell
virtualenv venv
```
:bulb: If you're using Pycharm, you have the option to have this automatically created for you.

Now activate the virtual environment
```shell
source venv/bin/activate
```
Or on windows
```shell
venv\Scripts\activate
```

This will isolate the current Python executable you use for this project only, so you won't tamper with the
global one and if you need to install something specific to this project only(with possibly conflicting versions with the system installation, for example)
then you can do it here only. This is simply good practice. But please *don't* upload this folder to your submissions,
I don't need it.

## And finally, we'll have Django
```shell
pip install Django
```
:bulb: pip is the basic Python package manager. It lets you download libraries and frameworks, etc. It's gonna do it in our local installation,
inside our virtual environment.

The following steps are automatically executed if you create a new Django app from Pycharm, but for clarity of exposition, it's
good for us to get through each step and to see how we create everything from scratch and not hide behind the big
shiny green button that just does everything for us.

```shell
django-admin startproject coderun
```
This will initialize a new project. A project can contain multiple apps. We'll add apps to this project as well. For now, the directory structure
should look something like: 
```
coderun
├── coderun
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

Let's see if it works:
```shell
python manage.py runserver
```

If you see the screen with the rocket, that means you're good to go :rocket:.

Let's create an app now:

```shell
python manage.py startapp demo
```
Now you should see something like this:
```
coderun
├── coderun
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── demo
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── manage.py
```

## Views, routing, URL-s
Django works with a specific version of the MVC(Model-View-Controller) pattern,
called MVT(Model-View-Template). Views are classes or functions that handle application logic. They generally receive
an HTTP request, handle it by possibly interacting with multiple subcomponents, models, etc. and return a response, generally
either as an HTTP page or as a JSON response. You can have multiple views for multiple use cases, and Django
decides what view to call based on routing. You'll hear more about routing a bit later.

Consider the following view:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1 style='background-color:skyblue;display:flex;justify-content:center;'>Hello, code runner.</h1>")
```
As you can see, we can return complete HTML code as a string. But that's a bit savage, and not very maintainable. We'll see how to improve on this, but let's
make this view accessible.
Add the following code to `demo/urls.py`:

```python
from .views import index
from django.urls import path

urlpatterns = [
    path('index/', index, name='index'),
]
```
Then, the project `views.py` should look like:

```python

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include('demo.urls')),
]
```
:bulb: Now at http://127.0.0.1:8000/demo/index your view should be accessible. `include` made sure that
all views defined in `demo/urls.py` are accessible under the demo prefix.
Exercise: if you simply add another view with another URL to `demo/urls.py`, it should be accessible
under `/demo/your-view` without modifying the project URL-s file again.

_Why are URL-s important?
Having a consistent and clear URL pattern scheme is important for multiple reasons. Search Engine Optimisation (SEO) is one big factor. Crawler bots parse your website, and look at your URLs and contents and index your website based on certain rules that favor clear and meaningful URLs over random and meaningless ones. This indexing helps your website show up higher on search pages.
Consistent, meaningful and well-structured URL-s also help the educated user and make your site easier to navigate, not mentioning the fact that such URL-s will make your
website seem a lot more trustworthy and credible. Be nice, and make the effort of using consistent URL structures._

Let's come back to the view we wrote earlier with that piece of HTML. Let's be honest, God had no hand in the creation of that abhorrence. It looks ugly, it is not maintainable,
and just imagine the amount of pain one might have to go through if it was a more complex and bigger piece of HTML code that had to be edited manually as the unholy
Python string that it is right now, should you ever have to change anything about it. And what would we do if we'd have to insert dynamic content? There has to be a better way.

### Templates to the rescue!
Django lets you write your HTML code with the possibility of inserting dynamic content, and then
reference these files from within the views. These are called templates. They extend regular HTML with so-called template tags, that help
you insert your dynamic content defined as regular Python variables. On this most auspicious of occasions, we can
also dive into what a request object contains that the view receives.
Let's add the following code to `demo/urls.py`:

```python
from django.shortcuts import render
... # the earlier views & imports

def inspect_request(request):
    return render(request, 'demo/index.html', context=dict(request=request))
```
then import and add this to the urlpatterns list of `demo/urls.py`:

```python
path('inspect/', inspect_request, name='inspect_request'),
```
Add a `demo` folder to `templates` and add the `index.html` file with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Proper Index page</title>
</head>
<body>
<h1>Hello, code runner</h1>
<div>
    {% if request.COOKIES %}
        <h2>I received some cookies</h2>
    {% else %}
        <h2> No cookies :(</h2>
    {% endif %}
</div>
<div>
    <h3>Path: <em>{{ request.path }}</em></h3>
    <h3>HTTP method: <em>{{ request.method }}</em></h3>
    <h3>Content-type: <em>{{ request.content_type }}</em></h3>
</div>
<div>
    <h3>Request params</h3>
    <ul>
        {% for param,value in request.GET.items %}
            <li>Param name: <b>{{ param }}</b> and Value: <b>{{ value }}</b></li>
        {% endfor %}
    </ul>
</div>

</body>
</html>
```
The content between the squiggles `{{ }}` is dynamic, while between `{% %}` you can add
control statements like ifs and fors, so that you can add dynamic content according to your needs. All these are
passed through the `context` parameter of the rendered view.
Access your website like http://127.0.0.1:8000/demo/inspect/?a=something&b=yesss and see how the
URL parameters show up.
