from django.contrib import admin
from .models import Scholar, Citation, Authored
from .forms import ScholarCreateForm
# Register your models here.

class ScholarCreateAdmin(admin.ModelAdmin):
  fields = ['id', 'name', 'designation', 'department']
  list_display = ['name', 'designation', 'department']
  # form = ScholarCreateForm
  # list_filter = ['department']  
  search_fields = ['name', 'designation']

class CitationAdmin(admin.ModelAdmin):
  fields =  ['citation_year', 'citation_title']
  list_display = ['citation_year', 'citation_title']


class AuthoredAdmin(admin.ModelAdmin):
  fields =  ['scholar', 'citation']
  list_display = ['scholar', 'citation']


admin.site.register(Scholar, ScholarCreateAdmin)
admin.site.register(Citation, CitationAdmin)
admin.site.register(Authored, AuthoredAdmin)
