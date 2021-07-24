from django.contrib import admin
from .models import Scholar, Citation
from .forms import ScholarCreateForm
# Register your models here.

class ScholarCreateAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'designation', 'department']
  form = ScholarCreateForm
  list_filter = ['department']  
  search_fields = ['name', 'designation']

admin.site.register(Scholar)
admin.site.register(Citation)