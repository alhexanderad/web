from django.contrib import admin
from persona.models import Persona
from import_export.admin import ImportExportModelAdmin

@admin.register(Persona)
class CursoAdmin(ImportExportModelAdmin):
  pass