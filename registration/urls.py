from django.urls import path

from registration.views import RegisterView

app_name = 'registration'

urlpatterns = [
    path('', RegisterView.as_view(), name='registration')
]
