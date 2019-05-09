from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'pyclubapp/index.html')

def getResources(request):
    resources_list=Resource.objects.all()
    return render(request, 'pyclubapp/resources.html', {'resources_list' : resources_list})

def resourceDetails(request, id):
    resource = get_object_or_404(Resource, pk = id)
    context = {
        'resource' : resource
    }
    return render(request, 'pyclubapp/resourcedetails.html', context=context)

def getMeeting(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'pyclubapp/meeting.html', {'meeting_list' : meeting_list})

def meetingDetails(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    context={
       'meeting' : meeting
    }
    return render (request, 'pyclubapp/meetingdetails.html', context=context)

def loginmessage(request):
    return render(request, 'pyclubapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'pyclubapp/logoutmessage.html')