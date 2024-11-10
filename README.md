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
