from django.db import models
class userdata(models.Model):
    date_joied=models.DateTimeField(auto_now_add=True, blank=True)
    last_active=models.DateTimeField(auto_now_add=True, blank=True)
class user(models.Model):
    user_id=models.IntegerField()
    email=models.EmailField()
    username=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    dob=models.DateField()
    vericode=models.CharField(max_length=50)
    def __unicode__(self):
        return self.first_name + self.last_name
