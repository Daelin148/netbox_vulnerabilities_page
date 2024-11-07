from django.urls import path
from .views import VulnerabilitiesView


urlpatterns = [
    path("vulnerabilities/", VulnerabilitiesView.as_view(), name="vulnerabilities"),
]