from django.db import connection
from .models import *

def keyWord_getTipe(keyWord):
    with connection.cursor() as cursor:
        cursor.execute("SELECT tipe FROM Task_keyword WHERE word = \"%s\"" %keyWord)
        rows = cursor.fetchall()

    return rows

def task_addTask(tgl, kode, jenis, topik): #db name: Task_task
    newTask = Task.objects.create(tanggal=tgl, kodematakuliah=kode, jenistugas=jenis, topiktugas=topik)
    newTask.save()

def task_deleteTask(task_id):
    Task.objects.filter(id=task_id).delete()

def task_getTask(tipe, task_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Task_task WHERE id=\"%s\"" %task_id)
        row = cursor.fetchone()

    return row

def kmpString (input_text, kata_penting):
    counter = repeatPatternCounter(kata_penting)

    i = 0
    j = 0
    while (i < len(input_text)):
        if (kata_penting[j]==input_text[i]):
            if (j == len(kata_penting) - 1):
                return True
            i+=1
            j+=1
        elif (j>0):
            j = counter[j-1]
        else:
            i+=1

    return False

def repeatPatternCounter (pattern):
    counter = [0 for i in range (len((pattern)))]

    i = 1
    j = 0
    while (i < len(pattern)):
        if (pattern[j]==pattern[i]):
            counter[i] = j+1
            i+=1
            j+=1
        elif (j>0):
            j = counter[j-1]
        else:
            i+=1
    
    return counter