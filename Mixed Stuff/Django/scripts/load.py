# some_file.py
import sys
from models import Prodcheck, Infoklasse
import csv



def run():
    with open(r'/Mixed Stuff/Mixed Stuff/Django/blog/testfile/testfile.csv', 'r',
              encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Prodcheck.objects.all().delete()
        Infoklasse.objects.all().delete()

        for row in reader:
            print(row)

            DetailInfo, _ = Infoklasse.objects.get_or_create(name=row[0])

            integrity = Prodcheck(Typ=row[1],
                        EventDay=row[6],
                        DetailInfo=DetailInfo)
            integrity.save()
