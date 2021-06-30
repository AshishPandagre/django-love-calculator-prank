from allauth.account.forms import SignupForm 
from django import forms 


class CustomSignupForm(SignupForm): 
	first_name = forms.CharField(label='First Name', widget=forms.TextInput(
		attrs={'type': 'text',
				'placeholder': 'First Name'}
	))

	last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
		attrs={'type': 'text',
				'placeholder': 'Last Name'}
	))


	def save(self, request):
		user = super(CustomSignupForm, self).save(request)
		
		print('user object received')
		user.save()
		return user