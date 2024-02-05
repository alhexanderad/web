from django.urls import path
from persona.views import PersonaListView, render_pdf_view

app_name = "persona"

urlpatterns = [
  path('lista/',PersonaListView.as_view(), name='lista'),
  path('pdf/', render_pdf_view, name='pdf'),
]