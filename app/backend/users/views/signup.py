# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.mixins import AccountActivationTokenGenerator

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.forms import SignupForm

User = get_user_model()
account_activation_token = AccountActivationTokenGenerator()

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST, request.FILES)

		if form.is_valid():
			user_obj = form.save(commit=False)
			user_obj.is_active = False
			user_obj.save()
			# Default Group assign Start -------------------------------------------------------
			if Group.objects.filter(name='Customer'):
				user_obj.groups.add(Group.objects.filter(name='Customer')[0])

			else:
				Customer_group, created = Group.objects.get_or_create(name="Customer")
				# content_type = ContentType.objects.get_for_model(CustomUser)
				# CustomUser_permission = Permission.objects.filter(content_type=content_type)
				# for perm in CustomUser_permission:
				# 	if perm.codename == "view_customuser":
				# 		Customer_group.permissions.add(perm)
				user_obj.groups.add(Customer_group)

			
			current_site = get_current_site(request)
			subject = 'Activate Your Account'
			message = render_to_string('chrev/modules/account_activation/account_activation_email.html', {
					'user': user_obj,
					'domain': current_site.domain,
					'uid': urlsafe_base64_encode(force_bytes(user_obj.pk)),
					'token': account_activation_token.make_token(user_obj),
			})
			email = form.cleaned_data.get('email')
			name = form.cleaned_data.get('first_name')
			ReceiversList = [email]
			EmailSender = settings.EMAIL_HOST_USER
			try:
				send_mail(subject, message, EmailSender, ReceiversList, fail_silently=False)
				if user_obj.is_active == False:
					messages.warning(request,'Please confirm your email address to complete the registration.')
				return redirect('users:signup')
			except:
				messages.warning(request,'Email Not valid')
				user_obj.delete()

		else:
			messages.warning(request,'Form is not valid')
	else:
		if request.user.is_authenticated:
			return redirect('tokens:portfolio')
		form = SignupForm()
	return render(request, 'chrev/modules/signup.html', {'form': form})

