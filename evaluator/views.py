from django.shortcuts import render, redirect
from evaluator.models import *
from django.contrib import messages
from django.utils import timezone


def home(request):
    return render(request, 'evaluator/home.html', {})


def evaluator(request):
    if request.method == 'POST':
        try:
            expression = request.POST['expression']
            ans = eval(expression)
            q = EvalData(expression=expression, ans=ans, pub_date=timezone.now())
            q.save()
            return render(request, 'evaluator/evaluator.html', {"data": [ans, expression]})
        except:
            messages.success(request, ('Error : Invalid Expression'))
            return redirect('evaluator')
    else:
        return render(request, 'evaluator/evaluator.html', {})


def history(request):
    q = EvalData.objects.all()
    return render(request, 'evaluator/history.html', {"data": q})

