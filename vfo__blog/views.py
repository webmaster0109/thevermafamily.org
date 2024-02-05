from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import BlogsDetail

from hitcount.views import HitCountDetailView
from django.db.models import Count



def blog___home(request):
    
    context = {
        'blogs' : BlogsDetail.objects.all().filter(status=1)
    }
    
    return render(request, template_name="blogs/blog__home.html", context=context)


class PostDetailView(HitCountDetailView):
    model = BlogsDetail
    template_name = 'blogs/detail.html'
    context_object_name = 'blog'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_posts': BlogsDetail.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context
