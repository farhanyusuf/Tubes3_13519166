import datetime

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