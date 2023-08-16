from django.urls import path
from . import views


urlpatterns = [
    # Static url paths
    path("january", views.index),
    path("february", views.february),
    path("march", views.march),
    # Dynamic url building
    path("<month>", views.monthly_challenge)
]