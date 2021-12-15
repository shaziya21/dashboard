
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from nav_dash.models import Post



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class pickerinput(ModelForm):
	class Meta:
		model = Post
		fields = '__all__'
