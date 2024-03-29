from django.urls import path
from persona.views import PersonaListView, detalleCerticado ,PersonaFindView,render_pdf_view

app_name = "persona"

urlpatterns = [
  path("buscar/<str:dni>/", PersonaFindView.as_view(), name="buscar"),
  path('lista/',PersonaListView.as_view(), name='lista'),
  path('pdf/<str:id>/', render_pdf_view, name='pdf'),
  path('<slug:slug>/',detalleCerticado, name='slug'),
  
]