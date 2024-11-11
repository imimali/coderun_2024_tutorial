from django.http import HttpResponse
from django.shortcuts import render

from demo.forms import UserDataForm
from demo.models import User


def index(request):
    return HttpResponse(
        "<h1 style='background-color:skyblue;display:flex;justify-content:center;'>Hello, code runner.</h1>")


def inspect_request(request):
    return render(request, 'demo/index.html', context=dict(request=request))

def register_user(request):
    user_data_form = UserDataForm()
    if request.method == "POST":
        name = user_data_form.cleaned_data['user_name']
        email = user_data_form.cleaned_data['email']
        weight = user_data_form.cleaned_data['weight']
        gender = user_data_form.cleaned_data['gender']
        user = User(user_name=name, email=email, weight=weight, gender=gender)
        user.save()
        # TODO: querying the db on every request like this is very bad practice
    return render(request,'demo/user.html',context=dict(form=user_data_form, users=User.objects.all()))
