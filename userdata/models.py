from django.db import models
class userdata(models.Model):
    date_joied=models.DateField()
    last_active=models.DateField()
class user(models.Model):
    email=models.EmailField()
    username=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    dob=models.DateField()
    info=models.ForeignKey(userdata)
    def __unicode__(self):
        return self.first_name+" "+self.last_name
