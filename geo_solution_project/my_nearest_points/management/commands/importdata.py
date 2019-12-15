from collections import Counter
import csv
import os.path
from django.contrib.gis.geos import GEOSGeometry
from decimal import *
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from my_nearest_points import models

'''
class Command(BaseCommand):
    help = "Import points from csv"

    def add_arguments(self, parser):
        parser.add_argument("csvfile", type=str)


    def handle(self, *args, **options):
        self.stdout.write("Importing Points")
        c = Counter()
        f = open(options["csvfile"], "r")
        with f:
            csv_reader = csv.reader(f, delimiter=";")
            next(csv_reader)
            for row in csv_reader:
                print(row[0])
                print(row[1])
                print(row[2])
                point = models.Points.objects.get_or_create(id=row[0], x=row[1], y=row[2], location=GEOSGeometry('{ "type": "Point", "coordinates": [ %s, %s] }'%(row[1], row[2])))
'''

class Command(BaseCommand):
    help = "Import points from csv"

    def add_arguments(self, parser):
        parser.add_argument("csvfile", type=str)


    def handle(self, *args, **options):
        self.stdout.write("Importing Points")
        c = Counter()
        f = open(options["csvfile"], "r")
        with f:
            csv_reader = csv.reader(f, delimiter=";")
            next(csv_reader)
            for row in csv_reader:
                #the_point = Point(row[1], row[2], srid = 4326)
                models.Points.objects.get_or_create(id=row[0], x=row[1], y=row[2], location = Point( [Decimal(row[1]), Decimal(row[2])], srid = 3857))
