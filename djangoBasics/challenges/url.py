from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),   # challenges
    # Static url paths
    path("january", views.index),
    path("february", views.february),
    path("march", views.march),
    # Dynamic url building
    path("<int:month>", views.monthly_challenge_using_numbers),
    # path("<str:month>", views.monthly_challenge),
    path("<str:month>", views.monthly_challenge_dynamic_appending, name="monthly-challenge")
]