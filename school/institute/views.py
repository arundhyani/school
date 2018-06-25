from django.shortcuts import render

# Create your views here.
from .forms import SchoolRegistrationForm
def register(request):
	if request.method == 'POST':
		user_form = SchoolRegistrationForm(request.POST)
		if user_form.is_valid():
			# Create a new user object but avoid saving it yet
			new_user = user_form.save(commit=False)
			# Set the chosen password
			#new_user.set_password(user_form.cleaned_data['password'])
			# Save the User object
			new_user.save()
			return render(request,'institute/register_done.html',{'new_user': new_user})
	else:
		user_form = SchoolRegistrationForm()
		return render(request,'institute/register.html',{'user_form': user_form})