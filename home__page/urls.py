from django.urls import path

from home__page.views import home__index, home__about, home___about__shrikant, home___about__veena, home___about__abhishek, home___about__anca, home___about__nicolle, home___contact, home___gallery

urlpatterns = [
    path('', home__index, name="home__index"),
    path('about-us', home__about, name="home__about"),
    path('late-shrikant-verma', home___about__shrikant, name="home___about__shrikant"),
    path('veena-verma', home___about__veena, name="home___about__veena"),
    path('abhishek-verma', home___about__abhishek, name="home___about__abhishek"),
    path('anca-verma', home___about__anca, name="home___about__anca"),
    path('nicolle-verma', home___about__nicolle, name="home___about__nicolle"),
    path('contact-us', home___contact, name="home___contact"),
    # gallery urls
    path('gallery', home___gallery, name="home___gallery"),
]
