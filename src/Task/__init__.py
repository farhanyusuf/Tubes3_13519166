from django.db import connection

def getKeyWord():
    with connection.cursor() as cursor:
        cursor.execute("SELECT tipe FROM KeyWord WHERE Word = %s", "deadline")
        row = cursor.fetchone()

    return row