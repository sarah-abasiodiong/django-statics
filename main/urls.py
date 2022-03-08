from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns =[
    path("home/", views.home_page, name ="homepage"),
    path("about/", views.about_page, name ="aboutpage")
]


urlpatterns += staticfiles_urlpatterns()