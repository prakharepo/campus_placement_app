from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class company(models.Model):
    company_name = models.CharField(max_length=100)
    company_location = models.CharField(max_length=100)
    company_ctc = models.CharField(max_length=100)
    company_category = models.CharField(max_length=100)
    job_profile = models.CharField(max_length=100)
    job_eligibility = models.CharField(max_length=100)
    job_skills = models.CharField(max_length=100)
    job_details = models.TextField()

    def __str__(self):
        return self.company_name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class application(models.Model):
    name = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    applied_to = models.ManyToManyField(company, null=True, blank=True)

    def __str__(self):
        return f'{self.name.username} Application'