from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.template import loader
from .forms import CustomUserCreationForm,FortuneDateForm
from .utils import Zhipu_AI_API
from lunarcalendar import Converter, Solar, Lunar
import datetime


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
    birth_type = "阳历"
    date = ""
    if request.method == 'POST':
        form = FortuneDateForm(request.POST)
        if form.is_valid():
            birth_year = form.cleaned_data['birth_year']
            birth_month = form.cleaned_data['birth_month']
            birth_day = form.cleaned_data['birth_day']
            birth_hour = form.cleaned_data['birth_hour']
            birth_date = f"{birth_year}年{birth_month}月{birth_day}日{birth_hour}时"
            birth_type = form.cleaned_data['birth_date_type']
            birth_type = "阳历" if birth_type == "solar" else "阴历"
            date = f"生日：{birth_date}  类型：{birth_type}"
        else:
            print(form.errors)
    else:
        print("empty")
        form = FortuneDateForm()
        
    # 获取今天的公历日期
    today = datetime.date.today()
    solar = Solar(today.year, today.month, today.day)
    
    # 将公历日期转换为农历日期
    lunar = Converter.Solar2Lunar(solar)
    lunar_date = f"{lunar.year}年{lunar.month}月{lunar.day}日"
        
    prompt = f"我出生于{birth_type}{birth_date}，今天是阴历{lunar_date}。请你结合我的生辰八字以及今天的日期，帮我详细地分析一下今天我的运势。"
    # print(prompt)
    fortune = ""
    fortune = Zhipu_AI_API(prompt)
    context = {
        'date': date,
        'fortune': fortune,
    }
    return HttpResponse(template.render(context, request))