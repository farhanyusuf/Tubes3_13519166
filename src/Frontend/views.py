from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect, reverse
from django.core import serializers
from django.http import HttpResponse
import re
from datetime import datetime
import datetime
import time
from .utils import *
from Frontend.models import Message

# Create your views here.
id = 0
class Main(View):
    template = 'main.html'

    def get(self, request):
        return render(request, self.template)

    # @csrf_exempt
    def post(self, request):
        msg1 = Message(name = "You", text = request.POST['message'])
        msg1.save()
        msg2 = inputUser(request.POST['message'])
        msg2.save()
        return redirect(reverse('main'))

class About(View):
    template = 'about.html'

    def get(self, request):
        return render(request, self.template)

class Delete(View):
    template = 'delete.html'

    def get(self, request):
        Message.objects.all().delete()
        return render(request, self.template)

class Messages(View):
    def get(self, request):
        all_message = Message.objects.all()
        all_message_list = serializers.serialize('json', all_message)
        return HttpResponse(all_message_list, content_type="text/json-comment-filtered") 

class task:
    task_count = 0
    def __init__(self, tanggal, kodematkul, jenistugas, topik) :
        self.id = task.task_count+1
        self.tanggal = tanggal
        self.kodematkul = kodematkul
        self.jenistugas = jenistugas
        self.topik = topik
        task.task_count += 1

    def getid(self):
        return self.id

    def gettanggal(self):
        return self.tanggal
    
    def getkodematkul(self):
        return self.kodematkul
    
    def getjenistugas(self):
        return self.jenistugas
    
    def gettopik(self):
        return self.topik
    
listkatapenting = [("tanggal","tanggal"), ("pada","tanggal"), ("topik", "topiktugas"), ("uas","jenistugas"),("uts","jenistugas"),("tucil","jenistugas"),("tubes","jenistugas"),("kuis","jenistugas"),("pr","jenistugas"),("kapan","tanggal"),("deadline","nontask"),("topik","topik")]

def isComponentOnTheList(element, listype):
    for i in range (len(listype)):
        if listype[i] == element:
            return True
    return False

def reacttoinput(listtype):
    if not isComponentOnTheList("tanggal",listtype):
        return 1
    elif  not isComponentOnTheList("jenistugas",listtype):
        return 2
    elif not isComponentOnTheList("topiktugas",listtype):
        return 3

def splitstring (text,ind):
    temp = ""
    for i in range (ind,len(text)-1):
        temp += text[i+1]
    return temp

def kmp(text,pattern):
    n = len(text)
    m = len(pattern)
    fail = computeFail(pattern)
    i=0
    j=0

    while (i < n) :
        if (pattern[j] == text[i]) :
            if (j == m - 1):
                return i - m + 1; # match
            i += 1
            j += 1
        elif (j > 0):
            j = fail[j-1]
        else:
            i += 1
    return -1 #no match

def regextanggal(text):
    x = re.findall("(\d?\d)/(\d?\d)/(\d\d\d\d)",text)
    date = []
    for i in range (len(x)):
        temp = x[i][0] + "/" + x[i][1] + "/" + x[i][2]
        date.append(temp)
    return date

def regexmatkul(text):
    x = re.findall("[A-Z][A-Z][0-9][0-9][0-9][0-9]",text)
    return x

def converdatefromstring(dateString):
    date = datetime.strptime(dateString,"%d/%m/%Y")
    return date

def computeFail(pattern):
    fail = [0] * len(pattern)
    fail[0] = 0
    m = len(pattern)
    j = 0
    i = 1

    while (i < m) :
        if (pattern[j] == pattern[i]): #j+1 chars match
            fail[i] = j + 1
            i += 1
            j += 1
        elif (j > 0): # j follows matching prefix
            j = fail[j-1]
        else: #no match
            fail[i] = 0
            i += 1
    return fail #end of computeFail()

def inputUser(text):
    global id
    if kmp(text,"deadline") != -1:
        if (kmp(text,"sejauh")!=-1):
            data = task_getTasks()
            msg = ""
            for i in range (len(data)):
                msg+=str(i+1)+". (ID:"+str(data[i][0])+") "+data[i][4].strftime("%d/%m/%Y")+" - "+data[i][1]+" - "+data[i][2]+" - "+data[i][3]+"<br>"
            return Message(name="Rick", text="[DAFTAR Deadline]<br>"+msg)
        elif (kmp(text,"sampai")):
            tgl=regextanggal(text)
            data = task_getTaskDurasi(converdatefromstring(tgl[0]), converdatefromstring(tgl[1]))
            msg = ""
            for i in range (len(data)):
                msg+=str(i+1)+". (ID:"+str(data[i][0])+") "+data[i][4].strftime("%d/%m/%Y")+" - "+data[i][1]+" - "+data[i][2]+" - "+data[i][3]+"<br>"
            return Message(name="Rick", text="[DAFTAR Deadline]<br>"+msg)
    elif kmp(text, "fitur") != -1 or kmp(text, "help") != -1:
        msg="[FITUR YANG TERSEDIA]<br>"
        msg+="1. Menambahkan task baru<br>"
        msg+="2. Melihat daftar task <br><br>"
        msg+="[DAFTAR KATA PENTING]<br>"
        msg+="1. kuis<br>2. uts<br>3. tucil<br>4. tubes<br>5. deadline<br>6. tanggal<br>7. pada<br>8. pr<br>9. topik"
        return Message(name="Rick", text=msg)
    else: #buat nambahin task
        listtype = []
        jenistugas = ""
        topik = ""
        for i in range (len(listkatapenting)):
            if kmp(text,listkatapenting[i][0]) != -1:
                listtype.append(listkatapenting[i][1])
                if listkatapenting[i][1] == "jenistugas":
                    jenistugas = listkatapenting[i][0]
                elif listkatapenting[i][1] == "topik":
                    topik = splitstring(text,kmp(text,"topik")+len("topik"))
        casein = reacttoinput(listtype)
        if casein == 1:
            return Message(name = "Rick", text = "Tanggal belum diinput")
        elif casein == 2:
            return Message(name = "Rick", text = "Jenis tugas belum diinput")
        elif casein == 3:
            return Message(name = "Rick", text = "Topik belum diinput")
        elif len(regexmatkul(text)) == 0:
            return Message(name = "Rick", text = "Kode matkul belum diinput")
        else:
            new_task = task(regextanggal(text)[0],regexmatkul(text)[0],jenistugas,topik)
            date_datetime = converdatefromstring(new_task.gettanggal())
            task_addTask(date_datetime, new_task.getkodematkul(), new_task.getjenistugas(), new_task.gettopik())
            id+=1
            return Message(name = "Rick",text = "[TASK BERHASIL DICATAT]<br> ID: " + str(id) +  " - " + new_task.gettanggal() + " - " + new_task.getjenistugas() + " - " + new_task.gettopik())
