from django import forms

from .models import Inquiry
from django.utils.translation import ugettext_lazy as _


class InquiryForm(forms.ModelForm):
	class Meta:
		model = Inquiry
		fields = ('email_address', 'first_name', 'last_name')

	#cleaning and checking whether the email address
	def clean_email_address(self):
		#cleaning the address provided by the user
		email = (self.cleaned_data['email_address']).strip()
		if '@' in email:
			local, host = email.split('@')
			email = local + '@' + host.lower()

		if Inquiry._default_manager.filter(email_address__iexact=email).exists():
			raise forms.ValidationError(
				_("It seems you have already registered your address!"))
		return email