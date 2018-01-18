from django.db import models


class Event(models.Model):
	date = models.DateTimeField()
	interval = models.TimeField()
	event = models.CharField(max_length=100)
	interval_1 = models.TimeField()
	event_1 = models.CharField(max_length=100)
	interval_2 = models.TimeField()
	event_2 = models.CharField(max_length=100)
	interval_3 = models.TimeField(null=True)
	event_3 = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.event

class Photos(models.Model):
	date = models.DateTimeField()
	google_url = models.CharField(max_length=500)

	def __str__(self):
		return "Data: {}".format(self.date)

class Videos(models.Model):
	date = models.DateTimeField()
	youtube_url = models.CharField(max_length=200)

	def __str__(self):
		return "Data: {}".format(self.date)