from django.db import models
from django.contrib.auth.models import User
import datetime
from pytz import timezone

class Message_Data(models.Model):
	from_user = models.ForeignKey(User, related_name="from_user_rn", on_delete=models.CASCADE)
	to_user = models.ForeignKey(User,related_name="to_user_rn", on_delete=models.CASCADE)
	msg = models.CharField(max_length=2000)
	datetime_stamp = models.DateTimeField(auto_now_add=True)

	# from_user = models.CharField(max_length=200)
	# to_user = models.CharField(max_length=200)
	# msg = models.CharField(max_length=200)
	
	def __str__(self):
		#format to display message time
		fmt = "%d %b %I:%M %p"
		# msg time in IST is offset of +5:30 wrt UTC
		offset = datetime.timedelta(hours=5, minutes=30)
		msg_time = self.datetime_stamp + offset
		t = msg_time.strftime(fmt).lower()
		
		return f'{self.from_user}|{self.to_user}|{t} * {self.msg}'
	
	def getTimeIST(self):
		# returns hour:minutes AM/PM string
		fmt = "%I:%M %p"
		# msg time in IST is offset of +5:30 wrt UTC
		offset = datetime.timedelta(hours=5, minutes=30)
		msg_time = self.datetime_stamp + offset
		t = msg_time.strftime(fmt)
		return t