from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import GalleryMediaFile, Visitor, send_visitor_details_email, UniqueVisitorCount
from vfo__blog.models import BlogsDetail
from django.utils import timezone

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_visitor_logs(request):
    ip_address = get_client_ip(request)
    landing_page = request.build_absolute_uri()  # Get the current page URL

    # Check if there is an existing visitor record with the same IP address and no departure time
    existing_visitor = Visitor.objects.filter(ip_address=ip_address, departure_time__isnull=True).first()

    if existing_visitor:
        # Update the landing page and calculate time on the previous page
        existing_visitor.departure_time = timezone.now()
        existing_visitor.time_on_page = existing_visitor.departure_time - existing_visitor.visit_time
        existing_visitor.save()
        
        send_visitor_details_email(existing_visitor)
    
    new_visitor = Visitor.objects.create(ip_address=ip_address, landing_page=landing_page)
    unique_visitor_hit_count = Visitor.objects.filter(ip_address=ip_address).count()
    unique_visitor_hit(ip_address, unique_visitor_hit_count)
    return new_visitor

def unique_visitor_hit(ip, count):
    unique_visitor_count, created = UniqueVisitorCount.objects.get_or_create(ip_address=ip)
    
    # If it already exists, update the count
    if not created:
        unique_visitor_count.visit_count = count
        unique_visitor_count.save()

    return unique_visitor_count


def home__index(request):

    # Create a new visitor record for the current page
    visitor = get_visitor_logs(request)

    context = {
        'recents' : BlogsDetail.objects.all().filter(status=1).order_by('-created_at')[:6],
        'visitor' : visitor
    }
    return render(request, template_name="home/index.html", context=context)

def home__about(request):

    visitor = get_visitor_logs(request)

    context = {
        'visitor' : visitor
    }

    return render(request, template_name="home/about__us.html", context=context)

def home___about__shrikant(request):

    visitor = get_visitor_logs(request)

    context = {
        'visitor' : visitor
    }

    return render(request, template_name="home/shrikant__verma.html", context=context)

def home___about__veena(request):

    visitor = get_visitor_logs(request)

    context = {
        'visitor' : visitor
    }

    return render(request, template_name="home/veena__verma.html", context=context)

def home___about__abhishek(request):

    visitor = get_visitor_logs(request)

    context = {
        'visitor' : visitor
    }

    return render(request, template_name="home/abhishek__verma.html", context=context)

def home___about__anca(request):

    visitor = get_visitor_logs(request)

    context = {
        'visitor' : visitor
    }

    return render(request, template_name="home/anca__verma.html", context=context)

def home___about__nicolle(request):

    visitor = get_visitor_logs(request)

    context = {
        'visitor' : visitor
    }

    return render(request, template_name="home/nicolle__verma.html", context=context)

def home___contact(request):

    visitor = get_visitor_logs(request)

    context = {
        'visitor' : visitor
    }

    return render(request, template_name="home/contact__us.html", context=context)

def home___gallery(request):

    visitor = get_visitor_logs(request)

    context = {
        'galleries': GalleryMediaFile.objects.all(),
        'visitor' : visitor
    }
    return render(request, template_name="gallery/gallery___home.html", context=context)

def handle___unmatched(request, unmatched_path):


    context={
        'unmatched_path': unmatched_path,
    }
    return HttpResponseNotFound(HttpResponseNotFound(render(request, template_name='error404/not___found.html', context=context)))