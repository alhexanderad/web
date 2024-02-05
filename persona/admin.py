from django.contrib import admin
from persona.models import Persona,Sello
from import_export.admin import ImportExportModelAdmin

@admin.register(Persona,Sello)
class CursoAdmin(ImportExportModelAdmin):
  pass