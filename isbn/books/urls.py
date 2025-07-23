from django.urls import path
from .views import ISBNLookupView

urlpatterns = [
    path('lookup/<str:isbn>/', ISBNLookupView.as_view()),
]
