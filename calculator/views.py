from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView, CreateView, TemplateView
from .models import Referral, User, Contact
from django.core.mail import send_mail
# from django.contrib.auth.models import User
import threading
from threading import Thread
from django.core.mail import EmailMessage


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run (self):
        msg = EmailMessage(self.subject, self.html_content, 'pranklovecalculator2@gmail.com', self.recipient_list)
        msg.content_subtype = "html"
        msg.send()

def error_404(request, exception):
	data = {}
	response = render(request, 'calculator/404.html')
	return response


def error_500(request, *args, **kwargs):
	return render(request, 'calculator/404.html')

def error(request):
	return render(request, 'calculator/404.html')


def home(request):
	return render(request, 'calculator/home.html')


def contact(request):
	if request.method == 'POST':
		first_name = request.POST['fname']
		last_name = request.POST['lname']
		email = request.POST['email']
		comment = request.POST['comment']

		c = Contact(first_name=first_name, last_name=last_name ,email=email, comment=comment)
		c.save()

		return render(request, 'calculator/contact.html', {'contact': 'saved'})
	return render(request, 'calculator/contact.html')


# Create your views here.
@method_decorator(login_required, name='dispatch')
class Profile(TemplateView):
	template_name = 'calculator/profile.html'

	def get_context_data(self, **kwargs):
		context = TemplateView.get_context_data(self, **kwargs)		
		context['referrals'] = Referral.objects.filter(_from=self.request.user)
		context['n_referrals'] = len(context['referrals'])
		return context


def calculate(request, ref_id):
	try:
		user = User.objects.get(key=ref_id)
	except:
		return render(request, 'calculator/404.html')		# 404 page
	
	if request.method == 'POST':
		name = request.POST['name']
		crush = request.POST['crush']

		ref = Referral(_from=user, name=name, crush=crush)
		ref.save()

		#send mail or whatsapp to USER
		# send_mail(
		# 	'That’s your subject',
		# 	'That’s your message body',
		# 	'ashishpandagre4@gmail.com',
		# 	['ashishpandagre9@gmail.com'],
		# 	fail_silently=False,
		# )

		# EmailThread('subject', f'Congratulations, You have fooled {name} his/her crush name is {crush}. ', [user.email]).start()

		return render(request, 'calculator/pranked.html', {'name': f'{user.first_name} {user.last_name}' })
		# return HttpResponse(f'You are fooled by {user.first_name} {user.last_name }')	# u are fooled page.

	return render(request, 'calculator/calculator.html')
