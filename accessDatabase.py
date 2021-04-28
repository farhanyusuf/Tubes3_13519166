from .django.db import connection

def getKeyWord():
    with connection.cursor() as cursor:
        cursor.execute("SELECT tipe FROM Task_keyword WHERE Word = %s", "deadline")
        row = cursor.fetchone()

    return row


print(getKeyWord())