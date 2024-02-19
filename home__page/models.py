from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime, timedelta
import pytz

# Create your models here.
class GalleryMediaFile(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title", null=True, blank=True)
    url = models.URLField(max_length=1000, verbose_name="URL")

    def __str__(self):
        return f"{str(self.id)} - {self.title}"


class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    visit_time = models.DateTimeField(auto_now_add=True)
    departure_time = models.DateTimeField(null=True, blank=True)
    landing_page = models.URLField(null=True, blank=True)
    time_on_page = models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.ip_address

class UniqueVisitorCount(models.Model):
    ip_address = models.GenericIPAddressField()
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(default="", null=True, blank=True)
    visit_count = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.ip_address


def convert_time_date(date_time):
    # visit time object
    visit_time_obj_utc = datetime.fromisoformat(date_time[:-6]).replace(tzinfo=pytz.utc)
    
    timezone_kolkata = pytz.timezone('Asia/Kolkata')
    
    # Convert visit time to Asia/Kolkata timezone
    timestamp_obj_kolkata = visit_time_obj_utc.astimezone(timezone_kolkata)

    # Extract visit date and time components
    date_component_kolkata = timestamp_obj_kolkata.date()
    time_component_kolkata = timestamp_obj_kolkata.time()
    visit_time_date = "Date: " + str(date_component_kolkata) + ", Time: " + str(time_component_kolkata)

    return visit_time_date

def convert_time_on_page(time):
    time_obj = datetime.strptime(time, "%H:%M:%S.%f")

    # Calculate minutes and seconds
    minutes = time_obj.minute
    seconds = time_obj.second + time_obj.microsecond / 1e6
    min_sec = f'{minutes} mins and {seconds} seconds'

    return min_sec

def send_visitor_details_email(visitor):

    visit_time = str(visitor.visit_time)
    visit_time_filter = convert_time_date(visit_time)

    departure_time = str(visitor.departure_time)
    departure_time_filter = convert_time_date(departure_time)

    min_sec = str(visitor.time_on_page)
    min_sec_filter = convert_time_on_page(min_sec)

    subject = f'New Visitor Details: {visitor.ip_address}'

    # Change the following line to the admin's email address
    recipient_email = 'admin@thevermafamily.org'

    html_message = render_to_string('email/template.html', {
        'user_email': recipient_email, 
        'ip_address': visitor.ip_address,
        'web_page' : visitor.landing_page,
        'visit_time': visit_time_filter,
        'departure_time': departure_time_filter,
        'time_on_page': min_sec_filter
    })

    message = strip_tags(html_message)

    send_mail(subject, message, from_email=settings.EMAIL_HOST_USER, recipient_list=[recipient_email], html_message=html_message)