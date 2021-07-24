from django import forms

from .models import Scholar

class ScholarCreateForm(forms.ModelForm):

    class Meta:
        model = Scholar
        fields = ['id', 'name', 'designation', 'department']
    
    def avoid_duplicacy(self):
        id = self.cleaned_data.get('id')
        for instance in Scolars.objects.all():
            if instance.id == id:
                raise forms.ValidationError(id + 'exists.')
        return id

class ScholarSearchForm(forms.ModelForm):
  
  class Meta:
    model = Scholar
    fields = ['name', 'designation', 'department']