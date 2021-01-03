from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Messages(models.Model):
    msg_from=models.ForeignKey(User,on_delete=models.CASCADE)
    msg_to=models.ForeignKey(User,on_delete=models.CASCADE)
    msg_text=models.TextField()
    date_postdate=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.msg_text


