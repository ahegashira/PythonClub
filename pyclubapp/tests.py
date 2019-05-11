from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from .views import index, getResources, getMeeting
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class MeetingTest(TestCase):
    def test_string(self):
        meet = Meeting(meeting_location = "BE3179")
        self.assertEqual(str(meet), meet.meeting_location)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class ResourceTest(TestCase):
    def test_string(self):
        reso = Resource(resource_name = "treehouse")
        self.assertEqual(str(reso), reso.resource_name)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource_name')

class EventTest(TestCase):
    def test_string(self):
        eventt = Event(event_title = "")
        self.assertEqual(str(eventt), even.event_title)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event_title')

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class getResourcesTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('Resource'))
        self.assertEqual(response.status_code, 200)