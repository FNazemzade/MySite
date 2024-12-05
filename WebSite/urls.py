from django.urls import path
from WebSite.views import *

urlpatterns = [
    path('',index_view),
    path('about',about_view),
    path('contact',contact_view)
]