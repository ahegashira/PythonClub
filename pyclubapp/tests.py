from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from .views import index, getResources, getMeeting
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import MeetingForm
import datetime

# Create your tests here.

# ---------- String & Table tests ----------

class MeetingTest(TestCase):
    def test_string(self):
        mt = Meeting(meeting_title = "Intro to Python")
        self.assertEqual(str(mt), mt.meeting_title)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class ResourcesTest(TestCase):
    def test_string(self):
        reso = Resource(resource_name = "treehouse")
        self.assertEqual(str(reso), reso.resource_name)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def test_string(self):
        event = Event(event_title = "testevent")
        self.assertEqual(str(event), event.event_title)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')


# ---------- Basic Views Testing ----------

class IndexViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class LoginMessageViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('loginmessage'))
        self.assertEqual(response.status_code, 200)

class LogoutMessageViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('logoutmessage'))
        self.assertEqual(response.status_code, 200)

class MeetingViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meeting'))
        self.assertEqual(response.status_code, 200)

class ResourcesViewTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, 200)

# ---------- Forms Tests ----------

class MeetingFormTest(TestCase):
    def test_typeform_is_valid(self):
        form=MeetingForm(
            data={
                'meeting_title' : "title1", 
                'meeting_date' : datetime.date(2020, 5, 10), 
                'meeting_time' : datetime.time(), 
                'meeting_location' : "some place", 
                'meeting_agenda' : "agenda1",
            }
        )
        self.assertTrue(form.is_valid())











