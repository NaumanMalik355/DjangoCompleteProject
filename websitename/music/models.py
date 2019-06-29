import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
# it has two columns question_text and pub_date
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    #its for user readable that is saved in database
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        # return self.pub_date >=timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <=now

# it has three columns
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
