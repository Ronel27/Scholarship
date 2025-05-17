from django.shortcuts import render, get_object_or_404
# import os.path
from .models import *
from datetime import date, timedelta

# Create your views here.
def index(request):
    # uploadedFile = UploadedFile.objects.all()
    return render(request,'index.html',)

def events(request):
    # Auto-delete overdue announcements
    auto_delete_overdue_announcements()
    # Exclude announcements where is_deleted is True
    announcements = Announcement.objects.filter(is_deleted=False).order_by('-id')
    return render(request, 'events.html', {'announcements': announcements})

def delete_Announcement(request, pk):
    announcements = get_object_or_404(Announcement, pk=pk)
    announcements.delete()
    return render(request, 'events.html', {'announcements': announcements})

def admin(request):
    return render(request, 'admin')

def auto_delete_overdue_announcements():
    """Automatically soft delete announcements 3 days after their due date."""
    # Calculate the threshold date (3 days after the due date)
    threshold_date = date.today() - timedelta(days=3)
    
    # Filter announcements where due_date is older than the threshold date and not already soft deleted
    overdue_announcements = Announcement.objects.filter(due_date__lt=threshold_date, is_deleted=False)
    
    # Soft delete the overdue announcements by setting is_deleted to True
    for announcement in overdue_announcements:
        announcement.is_deleted = True
        announcement.save()

def about(request):
    staffs = Staff.objects.all()
    return render(request, 'about.html', {'staffs' : staffs})

def courses(request):
    scholars = Scholar.objects.all()
    return render(request, 'courses.html', {'scholars' : scholars})

def contact(request):
    return render(request, 'contact.html')

def details(request):
    return render(request, 'course-details.html')