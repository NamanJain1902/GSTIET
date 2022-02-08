from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		field_names = [field_name for field_name, _ in self.fields.items()]
		for field_name in field_names:
			field = self.fields.get(field_name)
			field.widget.attrs.update({'placeholder': field.label, 'class': "input-control"})
		