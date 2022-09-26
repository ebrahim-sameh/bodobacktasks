from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from user.models import User


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
         abstract = True


class SocialMediaTask(TimeStampModel):
	post_url = models.URLField()
	action = models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	quota = models.DateTimeField()
	reward = models.DecimalField(max_digits=5, decimal_places=2)


class SurveyTask(TimeStampModel):
	form_link = models.URLField()
	category = models.CharField(max_length=255)
	quota = models.DateTimeField()
	statistics = models.CharField(max_length=255)
	individual_response_view = models.CharField(max_length=255)
	reward = models.DecimalField(max_digits=5, decimal_places=2)


class InviteTask(TimeStampModel):
	quota = models.DateTimeField()
	reward = models.DecimalField(max_digits=5, decimal_places=2)


class Task(TimeStampModel):
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		try:
			if self.content_type.name == 'survey task':
				return f"{self.content_object.form_link} - {self.content_object.category} - {self.content_object.reward}"
			if self.content_type.name == 'invite task':
				return f"invite task - {self.content_object.reward}"
			if self.content_type.name == 'social media task':
				return f"{self.content_object.post_url} - {self.content_object.action} - {self.content_object.reward}"
		except Exception as e:
			print(str(e))
		return f"{self.id}"


class TaskUserRel(TimeStampModel):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	status = models.BooleanField(default=False)

	class Meta:
		unique_together = ("user", "task",)


	def __str__(self):
		return f"{self.user} - {self.task}"