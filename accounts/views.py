from django.shortcuts import render
from userena.decorators import secure_required
from userena.views import profile_detail as userena_profile_detail, \
    signup as userena_signup, signin as userena_signin, \
    email_change, profile_edit, password_change
from accounts.forms import CustomSignupForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

@secure_required
def signup(request):

	if request.method == "POST":
		form = CustomSignupForm(request.POST)
		if form.is_valid():
			pass
			#form.save()
	else:
		form = CustomSignupForm()

	args = {
		'form': form,
	}

	return userena_signup(request, CustomSignupForm, 'signup.html', None, args)

@secure_required
def signin(request):
    """
        Wraps Userena signin, and also allows an user to sign in
        with their extra email.
    """
    if request.method == 'POST':
        original_identification = unicode(request.POST.get('identification', ""))

        # Restore the original identification if the form fails to validate.
        form = AuthenticationForm(request.POST, request.FILES)
        if not form.is_valid():
            request.POST = request.POST.copy()
            request.POST['identification'] = original_identification

    # Note that it's ours AuthenticationForm, not Userena's.
    return userena_signin(request, template_name='signin.html',
                          auth_form=AuthenticationForm)


@login_required
def signup_complete(request, username):
    url = reverse('edit_profile', args=[username])
    return HttpResponseRedirect(url)

@login_required
def profile(request, username):
	"""
		User profile
	"""
	pass

@login_required
def edit_profile(request, username):
	if request.user.username == username:
	else:
		url = reverse('me')
		return HttpResponseRedirect(url)


