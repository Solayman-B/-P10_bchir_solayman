from django.db import models
from authentication.models import User


class Project(models.Model):
	CHOICES = (
		('back-end', 'back-end'),
		('front-end,', 'front-end,'),
		('iOS', 'iOS'),
		('Android', 'Android')
	)
	title = models.CharField(max_length=99)
	description = models.CharField(max_length=999)
	type = models.CharField(max_length=99, choices=CHOICES)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_project')

	def __str__(self):
		return self.title

class Contributor(models.Model):
	CHOICES = (
		('Author', 'Author'),
		('Contributor', 'Contributor'),
	)

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	project = models.ForeignKey(Project, related_name='contributor', on_delete=models.CASCADE)
	permission = models.CharField(max_length=99, blank=True, null=True)
	role = models.CharField(max_length=99, choices=CHOICES, default='Contributor')

	def __str__(self):
		return self.user.username

class Issue(models.Model):
	CHOICES_TAG = (
		('BUG', 'BUG'),
		('AMÉLIORATION', 'AMÉLIORATION'),
		('TÂCHE', 'TÂCHE'),
	)

	CHOICES_PRIORITY = (
		('FAIBLE', 'FAIBLE'),
		('MOYENNE', 'MOYENNE'),
		('ÉLEVÉE', 'ÉLEVÉE'),
	)

	CHOICES_STATUS = (
		('À faire', 'À faire'),
		('En cours', 'En cours'),
		('Terminé', 'Terminé'),
	)

	title = models.CharField(max_length=99)
	description = models.CharField(max_length=999)
	tag = models.CharField(max_length=99, choices=CHOICES_TAG)
	priority = models.CharField(max_length=99, choices=CHOICES_PRIORITY)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='projected_issues')
	status = models.CharField(max_length=99, choices=CHOICES_STATUS)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_issues')
	assignee = models.ForeignKey(Contributor, on_delete=models.CASCADE)
	created_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Comment(models.Model):
	description = models.CharField(max_length=999)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
	created_time = models.DateTimeField(auto_now_add=True)