from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps.views import sitemap
from home__page.sitemaps import StaticSitemap
from home__page.views import handle___unmatched
from django.views.generic import TemplateView

sitemaps = {
    'static': StaticSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home__page.urls")),
    path('blogs/', include("vfo__blog.urls")),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('<str:unmatched_path>/', handle___unmatched, name='handle___unmatched'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += [re_path(r'^.*$', TemplateView.as_view(template_name='error404/not___found.html'), name='not___found')]