import json

from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView

from .forms import InquiryForm
from .models import Inquiry

from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template



class AjaxableResponseMixin(object):
	"""
	Mixin to add AJAX support to a form.
	Must be used with an object-based FormView (e.g. CreateView)
	"""
	def render_to_json_response(self, context, **response_kwargs):
		data = json.dumps(context)
		response_kwargs['content_type'] = 'application/json'
		return HttpResponse(data, **response_kwargs)

	def form_invalid(self, form):
		if self.request.is_ajax():
			return self.render_to_json_response(form.errors, status=400)
		else:
			return super(AjaxableResponseMixin, self).form_invalid(form)

	#adding e-mail adding functionality
	def send_email_to_user(self,form):
		from_email = 'Dev team <%s>'  % settings.PROJECT_EMAIL
		to = [form.instance.email_address,]
		subject = "Welcome to %s!" % settings.PROJECT_TITLE
		ctx = {'email':form.instance.email_address,'site':settings.PROJECT_TITLE}
		message = get_template('emails/registered.html').render(Context(ctx))
		msg = EmailMessage(subject, message, to=to, from_email=from_email)
		msg.content_subtype = 'html'
		msg.send()
		
	def form_valid(self, form):
		def create_inquiry(specification):
			return Inquiry.objects.create(**specification)
		#send email to user
		self.send_email_to_user(form)
		if self.request.is_ajax():
			data = {
				'first_name': form.instance.first_name,
				'last_name': form.instance.last_name,
				'email_address': form.instance.email_address,
			}

			newInquiry = {
				"first_name": form.instance.first_name,
				"last_name": form.instance.last_name,
				"email_address": form.instance.email_address,
				"ip_address": self.request.META['REMOTE_ADDR'],
			}
			create_inquiry(newInquiry)

			return self.render_to_json_response(data)
		else:
			return super(AjaxableResponseMixin, self).form_valid(form)
		


class HomeView(RedirectView):
	url = reverse_lazy('inquiry_create')


class InquiryCreate(AjaxableResponseMixin, CreateView):
	model = Inquiry
	form_class = InquiryForm
	success_url = reverse_lazy('inquiry_create_success')


class InquiryCreateSuccess(TemplateView):
	template_name = "launch_page/thanks.html"
