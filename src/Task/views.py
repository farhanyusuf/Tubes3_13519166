from django.shortcuts import render
from django.http import HttpResponse
from .utils import *
from django.db.utils import OperationalError
from .models import KeyWord, Task

# Create your views here.
def index(request):
    try:
        data = keyWord_getTipe("deadline")
        task_addTask("b","d","c","0")
        task_deleteTask(4)
        return HttpResponse(data[0])
    except OperationalError:
        return HttpResponse(Task.objects.model._meta.db_table)
