from django.test import TestCase

# Create your tests here.

from my_nearest_points.models import Points
from my_nearest_points.views import getpoints
from django.test import Client
from django.contrib.gis.geos import GEOSGeometry
import json
from django.urls import reverse


class PointsTestCase(TestCase):
    def setUp(self):
        user1_location = GEOSGeometry('{ "type": "Point", "coordinates": [%s , %s]}'%('91799865.7', '790243'))
        user2_location = GEOSGeometry('{ "type": "Point", "coordinates": [%s , %s]}'%('1176852.6', '993282.5'))
        #user3_location is invalid 
        Points.objects.create(id=9999999, x = 9799865.7, y = 790243, location = user1_location)
        Points.objects.create(id=8888888, x = 1176852.6, y = 993282.5, location = user2_location)
        Points.objects.create(id=7777777, x = 1176354852.6, y = 99345343282.5, location = user3_location)

    def test_known_nearest_point(self):
        """Check if a well-known point is selected as the nearest or not"""
        sample_point = Points.objects.get(id=8888888)
        c = Client()
        args = {'xcoordinate': 1176852.7, 'ycoordinate': 993282.6, 'inputpoints': '1', 'operator': 'distance' }
        response_res = c.post('/getnpoints', content_type='application/x-www-form-urlencoded')
        #response_json = json.loads(response_res.content)
        #print(response_res)
        self.assertEqual(response_res.status_code, 200)
        self.assertTemplateUsed(response_res, 'results.html')

    def test_x_as_valid_coordinate(self):
        """X is set within accepted range of latitude """
        sample_point = Points.objects.get(id=9999999)
        self.assertLess(sample_point.x, 9999999, msg="Please enter a valid X coordinate according to WGS84")
