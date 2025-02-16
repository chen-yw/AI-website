from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.template import loader
from .forms import CustomUserCreationForm,FortuneDateForm

def show_home(request):
    template = loader.get_template('blog/home.html')
    answer = "home example"
    context = {
        'home': answer,
    }
    return HttpResponse(template.render(context, request))

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def show_diary(request):
    template = loader.get_template('blog/diary.html')
    answer = "diary example"
    context = {
        'diary': answer,
    }
    return HttpResponse(template.render(context, request))

def show_fortune(request):
    template = loader.get_template('blog/fortune.html')
    answer = "fortune example"
    if request.method == 'POST':
        form = FortuneDateForm(request.POST)
        if form.is_valid():
            birth_year = form.cleaned_data['birth_year']
            birth_month = form.cleaned_data['birth_month']
            birth_day = form.cleaned_data['birth_day']
            birth_date = f"{birth_year}年{birth_month}月{birth_day}日"
            birth_type = form.cleaned_data['birth_type']
            answer = f"生日：{birth_date}，类型：{birth_type}"
    else:
        form = FortuneDateForm()
    context = {
        'fortune': answer,
    }
    return HttpResponse(template.render(context, request))