# feedback_app/urls.py

from django.urls import path
from .views import FeedbackListCreate

urlpatterns = [
    path('feedback/', FeedbackListCreate.as_view(), name='feedback'),  # <- This defines /api/feedback/
]
