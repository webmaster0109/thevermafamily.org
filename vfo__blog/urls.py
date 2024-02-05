from django.urls import path
from .views import blog___home, PostDetailView

urlpatterns = [
    path('', blog___home, name="blog___home"),
    path('<str:slug>', PostDetailView.as_view(), name="blog___detail"),
]
