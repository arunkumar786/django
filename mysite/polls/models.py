from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')
    
    # for representing in string we use this.
    def __str__(self):
        return self.question
    # now adding custom python method
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    
    # for representing in string we use this.
    def __str__(self):
        return self.choice_text
