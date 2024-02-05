from django.shortcuts import render
from persona.models import Persona,Sello

from django.views.generic import ListView
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

class PersonaListView(ListView):
  model=Persona
  template_name = 'persona_list.html'

def render_pdf_view(request):
  imagen = Sello.objects.get(id=1)
  psicologia = Sello.objects.get(id=2)
  print("logo de IC: ",imagen.nombre)
  template_path = 'persona/persona_pdf.html'
  context = {
    'myvar': 'this is your template context', 
    'imagen': imagen,
    'psicologia':psicologia,
    }
  
  # Create a Django response object, and specify content_type as pdf
  response = HttpResponse(content_type='application/pdf')
  response['Content-Disposition'] = 'attachment; filename="report.pdf"'
  
  # find the template and render it.
  template = get_template(template_path)
  html = template.render(context)

  # create a pdf
  pisa_status = pisa.CreatePDF(html, dest=response)
  
  # if error then show some funny view
  if pisa_status.err:
      return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
  return response