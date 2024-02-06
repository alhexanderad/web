import qrcode
import base64
from io import BytesIO
from django.shortcuts import render
from persona.models import Persona,Sello

from django.views.generic import ListView, DetailView, View
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

class PersonaFindView(View):
  template_name = 'persona/buscar_persona.html'

  def get(self, request, dni, *args, **kwargs):
    try:
      persona = Persona.objects.get(dni=dni)
      return render(request, self.template_name, {'persona': persona})
    except Persona.DoesNotExist:
      return render(request, self.template_name, {'error_message': 'Persona no encontrada'})

class PersonaListView(ListView):
  model=Persona
  template_name = 'persona_list.html'

class PersonaDetailView(DetailView):
  model= Persona
  template_name='persona/detalle.html'
  slug_field = 'slug'
  slug_url_kwarg = 'slug'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    # Generar el código QR
    text = self.request.build_absolute_uri(self.object.get_absolute_url())
    print(text)
    img = qrcode.make(text)

    # Convertir la imagen del código QR a una cadena de datos en formato base64
    img_base64 = img_to_base64(img)

    context['qr_code'] = img_base64
    return context
  
  def get(self, request, *args, **kwargs):
    # Recupera el valor de certificado_slug almacenado en CertificadoBuscarView
    self.persona_slug = getattr(self, 'persona_slug', None)
    return super().get(request, *args, **kwargs)

def render_pdf_view(request, id):  
  imagen = Sello.objects.get(id=1)
  psicologia = Sello.objects.get(id=2)
  persona = Persona.objects.get(n_certificado=id)
  
  titulo= persona.n_certificado
  # Generar el código QR desde el slug
  text = request.build_absolute_uri(persona.get_absolute_url())
  img = qrcode.make(text)
  img_base64 = img_to_base64(img)
  
  template_path = 'persona/persona_pdf.html'
  context = {
    'persona':persona,
    'imagen': imagen,
    'psicologia':psicologia,
    'qr_code': img_base64,
    }
  
  # Create a Django response object, and specify content_type as pdf
  response = HttpResponse(content_type='application/pdf')
  response['Content-Disposition'] = 'attachment; filename="%s-IC.pdf"' % titulo
  
  # find the template and render it.
  template = get_template(template_path)
  html = template.render(context)

  # create a pdf
  pisa_status = pisa.CreatePDF(html, dest=response)
  
  # if error then show some funny view
  if pisa_status.err:
      return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
  return response

def img_to_base64(img):
    buffered = BytesIO()
    img.save(buffered)
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/png;base64,{img_str}"