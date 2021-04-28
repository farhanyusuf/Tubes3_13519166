from django.shortcuts import render
from django.http import HttpResponse
from .utils import *
from django.db.utils import OperationalError
from .models import KeyWord, Task
import datetime

# Create your views here.
def index(request):
    try:
        #contoh get tipe
        data = keyWord_getTipe("deadline")
        #contoh add task
        date = datetime.datetime(2021, 2, 21)
        task_addTask(date,"d","c","0")
        #contoh get task durasi
        date_dari = datetime.datetime(2021,2,20)
        date_ke = datetime.datetime(2021, 2, 23)
        data_date = task_getTaskDurasi(date_dari, date_ke,"tanggal")

        #contoh get task normal
        data_task = task_getTask(5,"tanggal")
        #contoh deletetask by id
        task_deleteTask(4)
        return HttpResponse(data_date[0])
        
    except OperationalError:
        return HttpResponse(Task.objects.model._meta.db_table)
