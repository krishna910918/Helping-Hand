from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail #feedback is sent to mails

# Create your views here.

def feedback(request):
	return render(request,'feedback-page.html')

def accept_form(request):
	print("Name: ",request.POST['feedback_name'])
	print("Email ID: ",request.POST['feedback_email'])
	print("Message: ",request.POST['feedback_text'])
	mail_success = True
	d = {	'name'		:	request.POST['feedback_name'],
			'email_id'	:	request.POST['feedback_email'],
			'text'		:	request.POST['feedback_text']
		}
	print(d)
	try:
		mail_success = send_mail(
			'New Feedback on WAD Website',
			f"\"{request.POST['feedback_text']}\"\
				\nname: {d['name']}\
				\nfrom user mailid: {d['email_id']}",
			from_email='wadproject37@gmail.com',
			recipient_list=['wadproject37@gmail.com',
							'fawadmirza32@gmail.com',
							'saikrishnakotina@gmail.com',],#TODO:add more 3 more mails
		)
		print(mail_success,type(mail_success))
		if mail_success==1:
			d['feedback_status'] = "Your Feedback has been sent successfully!"
		else:
			d['feedback_status'] = "Sorry!, Couldn't send your feedback. Try again Later"
	except Exception as e:
		print("except block",e.message)
		d['feedback_status'] = "Something went wrong, couldn't send feedback"
	finally:
		print(d)
		return render(request,'submitted.html',d)

