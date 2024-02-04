from django.urls import path
from persona.views import PersonaListView

app_name = "persona"

urlpatterns = [
  path('lista/',PersonaListView.as_view(), name='lista'),
]