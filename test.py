import re
from datetime import datetime
#from src import task

class task:
    task_count = 0
    def __init__(self, tanggal, kodematkul, jenistugas, topik) :
        self.id = task.task_count+1
        self.tanggal = tanggal
        self.kodematkul = kodematkul
        self.jenistugas = jenistugas
        self.topik = topik
        task.task_count += 1

    def gettanggal(self):
        return self.tanggal
    
    def getkodematkul(self):
        return self.kodematkul
    
    def getjenistugas(self):
        return self.jenistugas
    
    def gettopik(self):
        return self.topik
    
listkatapenting = [("tanggal","tanggal"), ("pada","tanggal"), ("topik", "topiktugas"), ("uas","jenistugas"),("uts","jenistugas"),("tucil","jenistugas"),("tubes","jenistugas"),("kuis","jenistugas"),("pr","jenistugas"),("kapan","tanggal"),("deadline","nontask"),("topik","topik")]
text = "Reminder tubes matkul IF2210 strategi algoritma tanggal 12/12/2000 topik string-matching"

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
        print("tanggal belum diinput")
    elif casein == 2:
        print("jenis tugas belum diinput")
    elif casein == 3:
        print("topik tugas belum diinput")
    elif len(regexmatkul(text)) == 0:
        print("matkul belum diinput")
    else:
        new_task = task(regextanggal(text)[0],regexmatkul(text)[0],jenistugas,topik)
        print("\nTASK BARU BERHASIL DITAMBAHKAN")
        print("Tanggal :",new_task.gettanggal())
        print("Jenis Tugas :",new_task.getjenistugas())
        print("Kode Matkul :",new_task.getkodematkul())
        print("Topik :",new_task.gettopik())


inputUser(text)
#print(splitstring(text,72))

"""
print(len(regextanggal(text)))
print(regextanggal(text)[0])
print(converdatefromstring(regextanggal(text)[0]))
print(len(regexmatkul(text)))
print(regexmatkul(text)[0])

posn = kmp(text,pattern)

if (posn == -1):
    print("Pattern not found")
else:
    print("Pattern starts at posn "+ str(posn))
"""




"""
print(splitstring(text,67))

print(kmp(text,"topik"))
str = ""
str = str + text[67]
str = str + text[68]
str = str + text[69]
print(str)
"""
