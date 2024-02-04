from django.shortcuts import render
from persona.models import Persona

from django.views.generic import ListView, DetailView

class PersonaListView(ListView):
  model=Persona
  template_name = 'persona_list.html'
