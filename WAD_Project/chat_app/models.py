from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
 

class Message_Data(models.Model):
	from_user = models.ForeignKey(User, related_name="from_user_rn", on_delete=models.CASCADE)
	to_user = models.ForeignKey(User,related_name="to_user_rn", on_delete=models.CASCADE)
	msg = models.CharField(max_length=2000)
	datetime_stamp = models.DateTimeField(auto_now_add=True)

	# from_user = models.CharField(max_length=200)
	# to_user = models.CharField(max_length=200)
	# msg = models.CharField(max_length=200)
	
	def __str__(self):
		t = self.datetime_stamp.strftime("%d %b %Y %I-%M-%S %p")
		return f'{t} : {self.msg}'
